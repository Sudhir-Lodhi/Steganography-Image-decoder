// Inventory Management System
class InventoryManager {
    constructor() {
        this.inventory = this.loadInventory();
        this.selectedItems = new Set();
        this.sortColumn = 'name';
        this.sortDirection = 'asc';
        this.editingItemId = null;
        
        this.initializeEventListeners();
        this.updateDisplay();
        this.updateStats();
    }

    // Load inventory from localStorage
    loadInventory() {
        const saved = localStorage.getItem('inventory');
        if (saved) {
            return JSON.parse(saved);
        }
        
        // Sample data for demonstration
        return [
            {
                id: this.generateId(),
                name: 'Wireless Headphones',
                sku: 'WH001',
                category: 'Electronics',
                quantity: 25,
                price: 79.99,
                minStock: 5,
                description: 'High-quality wireless headphones with noise cancellation',
                dateAdded: new Date().toISOString(),
                lastUpdated: new Date().toISOString()
            },
            {
                id: this.generateId(),
                name: 'Office Chair',
                sku: 'OC002',
                category: 'Furniture',
                quantity: 3,
                price: 149.99,
                minStock: 5,
                description: 'Ergonomic office chair with lumbar support',
                dateAdded: new Date().toISOString(),
                lastUpdated: new Date().toISOString()
            },
            {
                id: this.generateId(),
                name: 'Coffee Mug',
                sku: 'CM003',
                category: 'Kitchenware',
                quantity: 0,
                price: 12.99,
                minStock: 10,
                description: 'Ceramic coffee mug with company logo',
                dateAdded: new Date().toISOString(),
                lastUpdated: new Date().toISOString()
            }
        ];
    }

    // Save inventory to localStorage
    saveInventory() {
        localStorage.setItem('inventory', JSON.stringify(this.inventory));
    }

    // Generate unique ID
    generateId() {
        return Date.now().toString(36) + Math.random().toString(36).substr(2);
    }

    // Initialize event listeners
    initializeEventListeners() {
        // Add item button
        document.getElementById('addItemBtn').addEventListener('click', () => {
            this.showItemModal();
        });

        // Modal close buttons
        document.querySelectorAll('.close').forEach(closeBtn => {
            closeBtn.addEventListener('click', (e) => {
                const modal = e.target.closest('.modal');
                this.hideModal(modal);
            });
        });

        // Cancel buttons
        document.getElementById('cancelBtn').addEventListener('click', () => {
            this.hideModal(document.getElementById('itemModal'));
        });

        document.getElementById('bulkCancelBtn').addEventListener('click', () => {
            this.hideModal(document.getElementById('bulkEditModal'));
        });

        document.getElementById('confirmCancelBtn').addEventListener('click', () => {
            this.hideModal(document.getElementById('confirmModal'));
        });

        // Form submissions
        document.getElementById('itemForm').addEventListener('submit', (e) => {
            e.preventDefault();
            this.saveItem();
        });

        document.getElementById('bulkEditForm').addEventListener('submit', (e) => {
            e.preventDefault();
            this.applyBulkEdit();
        });

        // Search and filter
        document.getElementById('searchInput').addEventListener('input', (e) => {
            this.updateDisplay();
        });

        document.getElementById('categoryFilter').addEventListener('change', () => {
            this.updateDisplay();
        });

        document.getElementById('statusFilter').addEventListener('change', () => {
            this.updateDisplay();
        });

        // Select all checkbox
        document.getElementById('selectAll').addEventListener('change', (e) => {
            this.toggleSelectAll(e.target.checked);
        });

        // Bulk actions
        document.getElementById('bulkDeleteBtn').addEventListener('click', () => {
            this.showConfirmModal('Delete Selected Items', 
                `Are you sure you want to delete ${this.selectedItems.size} items? This action cannot be undone.`,
                () => this.deleteSelectedItems());
        });

        document.getElementById('bulkEditBtn').addEventListener('click', () => {
            this.showBulkEditModal();
        });

        // Export and import
        document.getElementById('exportBtn').addEventListener('click', () => {
            this.exportData();
        });

        document.getElementById('importBtn').addEventListener('click', () => {
            document.getElementById('importFile').click();
        });

        document.getElementById('importFile').addEventListener('change', (e) => {
            this.importData(e.target.files[0]);
        });

        // Sort functionality
        document.querySelectorAll('[data-sort]').forEach(sortBtn => {
            sortBtn.addEventListener('click', (e) => {
                const column = e.target.getAttribute('data-sort');
                this.sortInventory(column);
            });
        });

        // Click outside modal to close
        window.addEventListener('click', (e) => {
            if (e.target.classList.contains('modal')) {
                this.hideModal(e.target);
            }
        });
    }

    // Show item modal
    showItemModal(item = null) {
        const modal = document.getElementById('itemModal');
        const title = document.getElementById('modalTitle');
        const form = document.getElementById('itemForm');
        
        if (item) {
            title.textContent = 'Edit Item';
            this.editingItemId = item.id;
            this.populateForm(item);
        } else {
            title.textContent = 'Add New Item';
            this.editingItemId = null;
            form.reset();
        }
        
        this.showModal(modal);
        document.getElementById('itemName').focus();
    }

    // Populate form with item data
    populateForm(item) {
        document.getElementById('itemName').value = item.name;
        document.getElementById('itemSku').value = item.sku;
        document.getElementById('itemCategory').value = item.category;
        document.getElementById('itemQuantity').value = item.quantity;
        document.getElementById('itemPrice').value = item.price;
        document.getElementById('itemMinStock').value = item.minStock;
        document.getElementById('itemDescription').value = item.description || '';
    }

    // Save item
    saveItem() {
        const formData = {
            name: document.getElementById('itemName').value.trim(),
            sku: document.getElementById('itemSku').value.trim(),
            category: document.getElementById('itemCategory').value.trim(),
            quantity: parseInt(document.getElementById('itemQuantity').value),
            price: parseFloat(document.getElementById('itemPrice').value),
            minStock: parseInt(document.getElementById('itemMinStock').value) || 5,
            description: document.getElementById('itemDescription').value.trim()
        };

        // Validation
        if (!formData.name || !formData.sku) {
            this.showToast('Please fill in all required fields', 'error');
            return;
        }

        // Check for duplicate SKU
        const existingSku = this.inventory.find(item => 
            item.sku === formData.sku && item.id !== this.editingItemId
        );
        if (existingSku) {
            this.showToast('SKU already exists. Please use a unique SKU.', 'error');
            return;
        }

        if (this.editingItemId) {
            // Update existing item
            const index = this.inventory.findIndex(item => item.id === this.editingItemId);
            if (index !== -1) {
                this.inventory[index] = {
                    ...this.inventory[index],
                    ...formData,
                    lastUpdated: new Date().toISOString()
                };
                this.showToast('Item updated successfully', 'success');
            }
        } else {
            // Add new item
            const newItem = {
                id: this.generateId(),
                ...formData,
                dateAdded: new Date().toISOString(),
                lastUpdated: new Date().toISOString()
            };
            this.inventory.push(newItem);
            this.showToast('Item added successfully', 'success');
        }

        this.saveInventory();
        this.updateDisplay();
        this.updateStats();
        this.updateCategoryFilter();
        this.hideModal(document.getElementById('itemModal'));
    }

    // Delete item
    deleteItem(id) {
        this.showConfirmModal('Delete Item', 
            'Are you sure you want to delete this item? This action cannot be undone.',
            () => {
                this.inventory = this.inventory.filter(item => item.id !== id);
                this.saveInventory();
                this.updateDisplay();
                this.updateStats();
                this.showToast('Item deleted successfully', 'success');
            });
    }

    // Update display
    updateDisplay() {
        const searchTerm = document.getElementById('searchInput').value.toLowerCase();
        const categoryFilter = document.getElementById('categoryFilter').value;
        const statusFilter = document.getElementById('statusFilter').value;

        let filteredInventory = this.inventory.filter(item => {
            const matchesSearch = item.name.toLowerCase().includes(searchTerm) ||
                                item.sku.toLowerCase().includes(searchTerm) ||
                                item.category.toLowerCase().includes(searchTerm);

            const matchesCategory = !categoryFilter || item.category === categoryFilter;

            let matchesStatus = true;
            if (statusFilter) {
                const status = this.getItemStatus(item);
                matchesStatus = status === statusFilter;
            }

            return matchesSearch && matchesCategory && matchesStatus;
        });

        // Sort inventory
        filteredInventory.sort((a, b) => {
            let aVal = a[this.sortColumn];
            let bVal = b[this.sortColumn];

            if (this.sortColumn === 'totalValue') {
                aVal = a.quantity * a.price;
                bVal = b.quantity * b.price;
            }

            if (typeof aVal === 'string') {
                aVal = aVal.toLowerCase();
                bVal = bVal.toLowerCase();
            }

            if (this.sortDirection === 'asc') {
                return aVal > bVal ? 1 : -1;
            } else {
                return aVal < bVal ? 1 : -1;
            }
        });

        this.renderTable(filteredInventory);
    }

    // Render table
    renderTable(items) {
        const tbody = document.getElementById('inventoryTableBody');
        
        if (items.length === 0) {
            tbody.innerHTML = `
                <tr>
                    <td colspan="10" style="text-align: center; padding: 40px; color: #a0aec0;">
                        <i class="fas fa-box-open" style="font-size: 2em; margin-bottom: 10px; display: block;"></i>
                        No items found
                    </td>
                </tr>
            `;
            return;
        }

        tbody.innerHTML = items.map(item => {
            const status = this.getItemStatus(item);
            const totalValue = item.quantity * item.price;
            const lastUpdated = new Date(item.lastUpdated).toLocaleDateString();

            return `
                <tr ${this.selectedItems.has(item.id) ? 'class="selected"' : ''}>
                    <td>
                        <input type="checkbox" ${this.selectedItems.has(item.id) ? 'checked' : ''} 
                               onchange="inventoryManager.toggleItemSelection('${item.id}', this.checked)">
                    </td>
                    <td><strong>${item.name}</strong></td>
                    <td><code>${item.sku}</code></td>
                    <td><span class="category-tag">${item.category}</span></td>
                    <td><strong>${item.quantity}</strong></td>
                    <td>${item.price.toFixed(2)}</td>
                    <td><strong>${totalValue.toFixed(2)}</strong></td>
                    <td>
                        <span class="status-badge status-${status}">
                            ${status.replace('-', ' ')}
                        </span>
                    </td>
                    <td>${lastUpdated}</td>
                    <td>
                        <div class="action-buttons">
                            <button class="btn btn-secondary btn-icon" 
                                    onclick="inventoryManager.showItemModal(inventoryManager.inventory.find(i => i.id === '${item.id}'))"
                                    title="Edit">
                                <i class="fas fa-edit"></i>
                            </button>
                            <button class="btn btn-primary btn-icon" 
                                    onclick="inventoryManager.quickUpdateQuantity('${item.id}')"
                                    title="Quick Update">
                                <i class="fas fa-plus-minus"></i>
                            </button>
                            <button class="btn btn-danger btn-icon" 
                                    onclick="inventoryManager.deleteItem('${item.id}')"
                                    title="Delete">
                                <i class="fas fa-trash"></i>
                            </button>
                        </div>
                    </td>
                </tr>
            `;
        }).join('');
    }

    // Get item status
    getItemStatus(item) {
        if (item.quantity === 0) return 'out-of-stock';
        if (item.quantity <= item.minStock) return 'low-stock';
        return 'in-stock';
    }

    // Update statistics
    updateStats() {
        const totalItems = this.inventory.reduce((sum, item) => sum + item.quantity, 0);
        const totalValue = this.inventory.reduce((sum, item) => sum + (item.quantity * item.price), 0);
        const lowStockCount = this.inventory.filter(item => 
            item.quantity > 0 && item.quantity <= item.minStock
        ).length;

        document.getElementById('totalItems').textContent = totalItems.toLocaleString();
        document.getElementById('totalValue').textContent = `${totalValue.toLocaleString('en-US', {minimumFractionDigits: 2})}`;
        document.getElementById('lowStockCount').textContent = lowStockCount;
    }

    // Update category filter
    updateCategoryFilter() {
        const categories = [...new Set(this.inventory.map(item => item.category))].sort();
        const select = document.getElementById('categoryFilter');
        const currentValue = select.value;
        
        select.innerHTML = '<option value="">All Categories</option>';
        categories.forEach(category => {
            const option = document.createElement('option');
            option.value = category;
            option.textContent = category;
            select.appendChild(option);
        });
        
        select.value = currentValue;

        // Update datalist for form
        const datalist = document.getElementById('categoryList');
        datalist.innerHTML = '';
        categories.forEach(category => {
            const option = document.createElement('option');
            option.value = category;
            datalist.appendChild(option);
        });
    }

    // Sort inventory
    sortInventory(column) {
        if (this.sortColumn === column) {
            this.sortDirection = this.sortDirection === 'asc' ? 'desc' : 'asc';
        } else {
            this.sortColumn = column;
            this.sortDirection = 'asc';
        }

        // Update sort indicators
        document.querySelectorAll('[data-sort] i').forEach(icon => {
            icon.className = 'fas fa-sort';
        });

        const currentIcon = document.querySelector(`[data-sort="${column}"] i`);
        if (currentIcon) {
            currentIcon.className = this.sortDirection === 'asc' ? 'fas fa-sort-up' : 'fas fa-sort-down';
        }

        this.updateDisplay();
    }

    // Toggle item selection
    toggleItemSelection(itemId, selected) {
        if (selected) {
            this.selectedItems.add(itemId);
        } else {
            this.selectedItems.delete(itemId);
        }
        
        this.updateBulkActionsBar();
        this.updateSelectAllCheckbox();
    }

    // Toggle select all
    toggleSelectAll(selected) {
        const visibleItems = document.querySelectorAll('#inventoryTableBody input[type="checkbox"]');
        
        visibleItems.forEach(checkbox => {
            const itemId = checkbox.getAttribute('onchange').match(/'([^']+)'/)[1];
            if (selected) {
                this.selectedItems.add(itemId);
                checkbox.checked = true;
            } else {
                this.selectedItems.delete(itemId);
                checkbox.checked = false;
            }
        });
        
        this.updateBulkActionsBar();
        this.updateDisplay();
    }

    // Update select all checkbox
    updateSelectAllCheckbox() {
        const selectAllCheckbox = document.getElementById('selectAll');
        const visibleCheckboxes = document.querySelectorAll('#inventoryTableBody input[type="checkbox"]');
        const checkedCount = Array.from(visibleCheckboxes).filter(cb => cb.checked).length;
        
        selectAllCheckbox.indeterminate = checkedCount > 0 && checkedCount < visibleCheckboxes.length;
        selectAllCheckbox.checked = checkedCount === visibleCheckboxes.length && visibleCheckboxes.length > 0;
    }

    // Update bulk actions bar
    updateBulkActionsBar() {
        const bulkActionsBar = document.getElementById('bulkActionsBar');
        const selectedCount = document.getElementById('selectedCount');
        
        if (this.selectedItems.size > 0) {
            bulkActionsBar.style.display = 'flex';
            selectedCount.textContent = `${this.selectedItems.size} item${this.selectedItems.size !== 1 ? 's' : ''} selected`;
        } else {
            bulkActionsBar.style.display = 'none';
        }
    }

    // Show bulk edit modal
    showBulkEditModal() {
        if (this.selectedItems.size === 0) {
            this.showToast('Please select items to edit', 'warning');
            return;
        }
        
        this.showModal(document.getElementById('bulkEditModal'));
        document.getElementById('bulkEditForm').reset();
    }

    // Apply bulk edit
    applyBulkEdit() {
        const category = document.getElementById('bulkCategory').value.trim();
        const priceAdjustment = parseFloat(document.getElementById('bulkPriceAdjustment').value) || 0;
        const minStock = parseInt(document.getElementById('bulkMinStock').value);

        let updatedCount = 0;

        this.selectedItems.forEach(itemId => {
            const item = this.inventory.find(i => i.id === itemId);
            if (item) {
                if (category) {
                    item.category = category;
                }
                
                if (priceAdjustment !== 0) {
                    item.price = Math.max(0.01, item.price * (1 + priceAdjustment / 100));
                    item.price = Math.round(item.price * 100) / 100; // Round to 2 decimal places
                }
                
                if (!isNaN(minStock)) {
                    item.minStock = minStock;
                }
                
                item.lastUpdated = new Date().toISOString();
                updatedCount++;
            }
        });

        if (updatedCount > 0) {
            this.saveInventory();
            this.updateDisplay();
            this.updateStats();
            this.updateCategoryFilter();
            this.showToast(`${updatedCount} items updated successfully`, 'success');
        }

        this.selectedItems.clear();
        this.updateBulkActionsBar();
        this.hideModal(document.getElementById('bulkEditModal'));
    }

    // Delete selected items
    deleteSelectedItems() {
        const itemsToDelete = Array.from(this.selectedItems);
        this.inventory = this.inventory.filter(item => !itemsToDelete.includes(item.id));
        
        this.selectedItems.clear();
        this.saveInventory();
        this.updateDisplay();
        this.updateStats();
        this.updateBulkActionsBar();
        this.showToast(`${itemsToDelete.length} items deleted successfully`, 'success');
    }

    // Quick update quantity
    quickUpdateQuantity(itemId) {
        const item = this.inventory.find(i => i.id === itemId);
        if (!item) return;

        const newQuantity = prompt(`Update quantity for ${item.name}:`, item.quantity);
        if (newQuantity !== null && !isNaN(newQuantity)) {
            const quantity = parseInt(newQuantity);
            if (quantity >= 0) {
                item.quantity = quantity;
                item.lastUpdated = new Date().toISOString();
                this.saveInventory();
                this.updateDisplay();
                this.updateStats();
                this.showToast('Quantity updated successfully', 'success');
            } else {
                this.showToast('Quantity cannot be negative', 'error');
            }
        }
    }

    // Export data
    exportData() {
        const dataStr = JSON.stringify(this.inventory, null, 2);
        const dataBlob = new Blob([dataStr], { type: 'application/json' });
        
        const link = document.createElement('a');
        link.href = URL.createObjectURL(dataBlob);
        link.download = `inventory-${new Date().toISOString().split('T')[0]}.json`;
        link.click();
        
        this.showToast('Inventory data exported successfully', 'success');
    }

    // Import data
    importData(file) {
        if (!file) return;

        const reader = new FileReader();
        reader.onload = (e) => {
            try {
                const importedData = JSON.parse(e.target.result);
                
                if (!Array.isArray(importedData)) {
                    throw new Error('Invalid file format');
                }

                // Validate data structure
                const isValid = importedData.every(item => 
                    item.name && item.sku && typeof item.quantity === 'number' && typeof item.price === 'number'
                );

                if (!isValid) {
                    throw new Error('Invalid data structure');
                }

                // Add IDs if missing
                importedData.forEach(item => {
                    if (!item.id) {
                        item.id = this.generateId();
                    }
                    if (!item.dateAdded) {
                        item.dateAdded = new Date().toISOString();
                    }
                    item.lastUpdated = new Date().toISOString();
                });

                this.showConfirmModal('Import Data', 
                    `This will replace all current inventory data with ${importedData.length} items. Continue?`,
                    () => {
                        this.inventory = importedData;
                        this.saveInventory();
                        this.updateDisplay();
                        this.updateStats();
                        this.updateCategoryFilter();
                        this.showToast('Inventory data imported successfully', 'success');
                    });

            } catch (error) {
                this.showToast('Failed to import data. Please check file format.', 'error');
            }
        };
        
        reader.readAsText(file);
        // Clear the file input
        document.getElementById('importFile').value = '';
    }

    // Show modal
    showModal(modal) {
        modal.style.display = 'block';
        document.body.style.overflow = 'hidden';
    }

    // Hide modal
    hideModal(modal) {
        modal.style.display = 'none';
        document.body.style.overflow = 'auto';
    }

    // Show confirmation modal
    showConfirmModal(title, message, onConfirm) {
        const modal = document.getElementById('confirmModal');
        const titleEl = document.getElementById('confirmTitle');
        const messageEl = document.getElementById('confirmMessage');
        const confirmBtn = document.getElementById('confirmBtn');
        
        titleEl.textContent = title;
        messageEl.textContent = message;
        
        // Remove existing event listeners
        confirmBtn.replaceWith(confirmBtn.cloneNode(true));
        const newConfirmBtn = document.getElementById('confirmBtn');
        
        newConfirmBtn.addEventListener('click', () => {
            onConfirm();
            this.hideModal(modal);
        });
        
        this.showModal(modal);
    }

    // Show toast notification
    showToast(message, type = 'info') {
        const toast = document.createElement('div');
        toast.className = `toast ${type}`;
        
        const icon = this.getToastIcon(type);
        
        toast.innerHTML = `
            <i class="${icon}"></i>
            <span>${message}</span>
            <span class="toast-close">&times;</span>
        `;
        
        const closeBtn = toast.querySelector('.toast-close');
        closeBtn.addEventListener('click', () => {
            this.removeToast(toast);
        });
        
        document.getElementById('toastContainer').appendChild(toast);
        
        // Auto remove after 5 seconds
        setTimeout(() => {
            if (toast.parentNode) {
                this.removeToast(toast);
            }
        }, 5000);
    }

    // Get toast icon
    getToastIcon(type) {
        const icons = {
            success: 'fas fa-check-circle',
            error: 'fas fa-exclamation-circle',
            warning: 'fas fa-exclamation-triangle',
            info: 'fas fa-info-circle'
        };
        return icons[type] || icons.info;
    }

    // Remove toast
    removeToast(toast) {
        toast.style.transform = 'translateX(100%)';
        toast.style.opacity = '0';
        setTimeout(() => {
            if (toast.parentNode) {
                toast.parentNode.removeChild(toast);
            }
        }, 300);
    }
}

// Initialize the inventory manager when the page loads
let inventoryManager;

document.addEventListener('DOMContentLoaded', () => {
    inventoryManager = new InventoryManager();
});