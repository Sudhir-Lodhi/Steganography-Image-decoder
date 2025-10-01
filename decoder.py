# import tkinter as tk
# from tkinter import filedialog, messagebox
# from steganography import extract_message_lsb

# def open_decoder_window():
#     window = tk.Toplevel()
#     window.title("Decoder - Extract Message")

#     def browse_image():
#         file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg")])
#         entry_image_path.delete(0, tk.END)
#         entry_image_path.insert(0, file_path)

#     def extract():
#         image_path = entry_image_path.get()
#         key = entry_key.get().strip()

#         if not image_path:
#             messagebox.showwarning("Warning", "Please select an image.")
#             return

#         try:
#             secret = extract_message_lsb(image_path, key)
#             messagebox.showinfo("Extracted Message", secret)
#         except Exception as e:
#             messagebox.showerror("Error", str(e))

#     tk.Label(window, text="Stego Image:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
#     entry_image_path = tk.Entry(window, width=50)
#     entry_image_path.grid(row=0, column=1, padx=5, pady=5)
#     tk.Button(window, text="Upload Photo", command=browse_image).grid(row=0, column=2, padx=5, pady=5)

#     tk.Label(window, text="Key (Optional):").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
#     entry_key = tk.Entry(window, width=50)
#     entry_key.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

#     tk.Button(window, text="Extract Message", command=extract).grid(row=2, column=1, pady=10)







# from tkinter import filedialog, messagebox, Entry, Button, Label, Frame
# from steganography import extract_message_lsb

# def open_decoder_window(root, show_home_screen, clear_window):
#     clear_window()

#     def browse_image():
#         file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg")])
#         entry_image_path.delete(0, "end")
#         entry_image_path.insert(0, file_path)

#     def extract():
#         image_path = entry_image_path.get()
#         key = entry_key.get().strip()

#         if not image_path:
#             messagebox.showwarning("Warning", "Please select an image.")
#             return

#         try:
#             secret = extract_message_lsb(image_path, key)
#             messagebox.showinfo("Extracted Message", secret)
#         except Exception as e:
#             messagebox.showerror("Error", str(e))

#     Label(root, text="Decoder - Extract Message", font=('Arial', 14)).pack(pady=10)

#     frame = Frame(root)
#     frame.pack(pady=10)

#     Label(frame, text="Stego Image:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
#     entry_image_path = Entry(frame, width=40)
#     entry_image_path.grid(row=0, column=1, padx=5, pady=5)

#     Button(frame, text="Upload Photo", command=browse_image).grid(row=0, column=2, padx=5, pady=5)

#     Label(frame, text="Key (Optional):").grid(row=1, column=0, sticky="w", padx=5, pady=5)
#     entry_key = Entry(frame, width=40)
#     entry_key.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

#     Button(root, text="Extract Message", command=extract).pack(pady=10)
#     Button(root, text="Back", command=show_home_screen).pack()









# import ttkbootstrap as tb
# from tkinter import filedialog, messagebox
# from steganography import extract_message_lsb

# def open_decoder_window(root, show_home_screen, clear_window):
#     clear_window()

#     def browse_image():
#         file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg")])
#         entry_image_path.delete(0, "end")
#         entry_image_path.insert(0, file_path)

#     def extract():
#         image_path = entry_image_path.get()
#         key = entry_key.get().strip()

#         if not image_path:
#             messagebox.showwarning("Warning", "Please select an image.")
#             return

#         try:
#             secret = extract_message_lsb(image_path, key)
#             messagebox.showinfo("Extracted Message", secret)
#         except Exception as e:
#             messagebox.showerror("Error", str(e))

#     # Outer frame centered
#     outer_frame = tb.Frame(root)
#     outer_frame.place(relx=0.5, rely=0.5, anchor="center")

#     # Title
#     tb.Label(outer_frame, text="🔓 Decoder - Extract Message", 
#              font=('Helvetica', 20, 'bold')).pack(pady=20)

#     # Main form frame
#     form_frame = tb.Frame(outer_frame)
#     form_frame.pack(pady=10)

#     # Stego Image
#     tb.Label(form_frame, text="Stego Image:", font=('Helvetica', 12)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
#     entry_image_path = tb.Entry(form_frame, width=50)
#     entry_image_path.grid(row=0, column=1, padx=5, pady=5)

#     tb.Button(form_frame, text="Upload Photo", bootstyle="info-outline", command=browse_image).grid(row=0, column=2, padx=5, pady=5)

#     # Key
#     tb.Label(form_frame, text="Key (Optional):", font=('Helvetica', 12)).grid(row=1, column=0, sticky="w", padx=5, pady=5)
#     entry_key = tb.Entry(form_frame, width=40, show="*")
#     entry_key.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

#     # Buttons
#     button_frame = tb.Frame(outer_frame)
#     button_frame.pack(pady=20)

#     tb.Button(button_frame, text="Extract Message", bootstyle="success", width=20, command=extract).pack(side="left", padx=15)
#     tb.Button(button_frame, text="Back", bootstyle="danger-outline", width=15, command=show_home_screen).pack(side="left", padx=15)














#---------------------------------------------------------x  MAIN CODE  X------------------------------------------------------#
import time
import traceback
import ttkbootstrap as tb
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from steganography import extract_message_lsb

def open_decoder_window(root, show_home_screen, clear_window):
    clear_window()

    preview_label = None
    preview_img = None

    def log_error(e):
        with open("error_log.txt", "a") as f:
            f.write(traceback.format_exc() + "\n")

    def simulate_progress():
        for i in range(1, 101, 5):
            progressbar['value'] = i
            root.update_idletasks()
            time.sleep(0.02)

    def browse_image():
        nonlocal preview_img
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            entry_image_path.delete(0, "end")
            entry_image_path.insert(0, file_path)

            try:
                img = Image.open(file_path)
                img.thumbnail((400, 300))
                preview_img = ImageTk.PhotoImage(img)
                preview_label.config(image=preview_img)
                preview_label.image = preview_img
            except Exception as e:
                log_error(e)
                messagebox.showerror("Error", f"Cannot preview image: {e}")

    def show_message(secret):
        popup = tb.Toplevel(root)
        popup.title("Extracted Message")

        tb.Label(popup, text="📥 Extracted Message:", font=("Helvetica", 14, "bold")).pack(pady=10)

        text_box = tb.ScrolledText(popup, wrap="word", width=60, height=10, font=('Consolas', 11))
        text_box.insert("1.0", secret)
        text_box.config(state="disabled")
        text_box.pack(padx=20, pady=10)

        def copy_to_clipboard():
            root.clipboard_clear()
            root.clipboard_append(secret)
            root.update()

        tb.Button(popup, text="Copy to Clipboard", bootstyle="info", command=copy_to_clipboard).pack(pady=5)
        tb.Button(popup, text="Close", bootstyle="secondary", command=popup.destroy).pack(pady=5)

    def extract():
        image_path = entry_image_path.get()
        key = entry_key.get().strip()

        if not image_path:
            messagebox.showwarning("Warning", "Please select an image.")
            return

        if not image_path.lower().endswith(('.png', '.jpg', '.jpeg')):
            messagebox.showwarning("Invalid Format", "Only PNG and JPG images are supported.")
            return

        try:
            progressbar['value'] = 0
            root.update_idletasks()
            simulate_progress()

            secret = extract_message_lsb(image_path, key)

            progressbar['value'] = 100
            root.update_idletasks()

            show_message(secret)

            entry_image_path.delete(0, "end")
            entry_key.delete(0, "end")

        except Exception as e:
            log_error(e)
            messagebox.showerror("Error", str(e))
            progressbar['value'] = 0

    # --- UI Layout ---
    outer_frame = tb.Frame(root)
    outer_frame.place(relx=0.5, rely=0.5, anchor="center")

    tb.Label(
        outer_frame, 
        text="🔓 Decoder - Extract Message", 
        font=('Helvetica', 20, 'bold')
    ).pack(pady=20)

    preview_label = tb.Label(outer_frame)
    preview_label.pack(pady=10)

    progressbar = tb.Progressbar(
        outer_frame, orient="horizontal", 
        mode="determinate", length=400, bootstyle="info-striped"
    )
    progressbar.pack(pady=10)

    form_frame = tb.Frame(outer_frame)
    form_frame.pack(pady=10)

    entry_image_path = tb.Entry(form_frame, width=50)
    entry_image_path.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

    tb.Button(
        form_frame, text="Upload Photo", 
        bootstyle="info-outline", 
        command=browse_image
    ).grid(row=0, column=2, padx=5, pady=5)

    tb.Label(
        form_frame, text="Key (Optional – only if encryption used):", font=('Helvetica', 12)
    ).grid(row=1, column=0, sticky="w", padx=5, pady=5)
    
    entry_key = tb.Entry(form_frame, width=40, show="*")
    entry_key.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

    button_frame = tb.Frame(outer_frame)
    button_frame.pack(pady=20)

    tb.Button(
        button_frame, text="Extract Message", 
        bootstyle="success", width=20, 
        command=extract
    ).pack(side="left", padx=15)

    tb.Button(
        button_frame, text="Back", 
        bootstyle="danger-outline", width=15, 
        command=show_home_screen
    ).pack(side="left", padx=15)
#---------------------------------------------------------x  MAIN CODE  X------------------------------------------------------#