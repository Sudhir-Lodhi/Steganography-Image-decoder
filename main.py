# import os
# import cv2 
# from PIL import Image, ImageTk 
# import tkinter as tk
# from tkinter import filedialog, messagebox
# from steganography import hide_message_lsb, extract_message_lsb


# def browse_image():
#     file_path = filedialog.askopenfilename(
#         filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")]
#     )
#     entry_image_path.delete(0, tk.END)
#     entry_image_path.insert(0, file_path)


# def hide():
#     image_path = entry_image_path.get()
#     message = entry_message.get("1.0", tk.END).strip()
#     key = entry_key.get().strip()
#     output_path = "stego.png"

#     if not image_path or not message:
#         messagebox.showwarning("Warning", "Please select an image and enter a message.")
#         return

#     try:
#         hide_message_lsb(image_path, message, output_path, key)
#         messagebox.showinfo("Success", f"Message hidden in {output_path}")
#     except Exception as e:
#         messagebox.showerror("Error", str(e))


# def extract():
#     image_path = entry_image_path.get()
#     key = entry_key.get().strip()

#     if not image_path:
#         messagebox.showwarning("Warning", "Please select an image.")
#         return

#     try:
#         secret = extract_message_lsb(image_path, key)
#         messagebox.showinfo("Extracted Message", secret)
#     except Exception as e:
#         messagebox.showerror("Error", str(e))


# # ------------------------
# # GUI Setup
# # ------------------------
# root = tk.Tk()
# root.title("Image Steganography (LSB-based)")

# tk.Label(root, text="Cover Image:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
# entry_image_path = tk.Entry(root, width=50)
# entry_image_path.grid(row=0, column=1, padx=5, pady=5)
# tk.Button(root, text="Upload Photo", command=browse_image).grid(row=0, column=2, padx=5, pady=5)

# tk.Label(root, text="Secret Message:").grid(row=1, column=0, sticky=tk.NW, padx=5, pady=5)
# entry_message = tk.Text(root, width=50, height=5)
# entry_message.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

# tk.Label(root, text="Key (Optional):").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
# entry_key = tk.Entry(root, width=50)
# entry_key.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

# tk.Button(root, text="Hide Message", command=hide).grid(row=3, column=0, pady=10)
# tk.Button(root, text="Extract Message", command=extract).grid(row=3, column=1, pady=10)

# root.mainloop()



# import tkinter as tk
# from tkinter import filedialog, messagebox
# from steganography import hide_message_lsb, extract_message_lsb

# root = tk.Tk()
# root.title("Image Steganography (LSB-based)")
# root.geometry("600x400")

# def clear_window():
#     for widget in root.winfo_children():
#         widget.destroy()

# def show_home_screen():
#     clear_window()
#     tk.Label(root, text="Choose an Action", font=('Arial', 16)).pack(pady=20)

#     tk.Button(root, text="Encode Message", width=20, command=show_encoder_screen).pack(pady=10)
#     tk.Button(root, text="Decode Message", width=20, command=show_decoder_screen).pack(pady=10)

# def show_encoder_screen():
#     clear_window()

#     def browse_image():
#         file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg")])
#         entry_image_path.delete(0, tk.END)
#         entry_image_path.insert(0, file_path)

#     def hide():
#         image_path = entry_image_path.get()
#         message = entry_message.get("1.0", tk.END).strip()
#         key = entry_key.get().strip()
#         output_path = "stego.png"

#         if not image_path or not message:
#             messagebox.showwarning("Warning", "Please select an image and enter a message.")
#             return

#         try:
#             hide_message_lsb(image_path, message, output_path, key)
#             messagebox.showinfo("Success", f"Message hidden in {output_path}")
#         except Exception as e:
#             messagebox.showerror("Error", str(e))

#     tk.Label(root, text="Encoder - Hide Message", font=('Arial', 14)).pack(pady=10)

#     frame = tk.Frame(root)
#     frame.pack(pady=10)

#     tk.Label(frame, text="Cover Image:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
#     entry_image_path = tk.Entry(frame, width=40)
#     entry_image_path.grid(row=0, column=1, padx=5, pady=5)
#     tk.Button(frame, text="Upload Photo", command=browse_image).grid(row=0, column=2, padx=5, pady=5)

#     tk.Label(frame, text="Secret Message:").grid(row=1, column=0, sticky=tk.NW, padx=5, pady=5)
#     entry_message = tk.Text(frame, width=50, height=5)
#     entry_message.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

#     tk.Label(frame, text="Key (Optional):").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
#     entry_key = tk.Entry(frame, width=40)
#     entry_key.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

#     tk.Button(root, text="Hide Message", command=hide).pack(pady=10)
#     tk.Button(root, text="Back", command=show_home_screen).pack()

# def show_decoder_screen():
#     clear_window()

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

#     tk.Label(root, text="Decoder - Extract Message", font=('Arial', 14)).pack(pady=10)

#     frame = tk.Frame(root)
#     frame.pack(pady=10)

#     tk.Label(frame, text="Stego Image:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
#     entry_image_path = tk.Entry(frame, width=40)
#     entry_image_path.grid(row=0, column=1, padx=5, pady=5)
#     tk.Button(frame, text="Upload Photo", command=browse_image).grid(row=0, column=2, padx=5, pady=5)

#     tk.Label(frame, text="Key (Optional):").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
#     entry_key = tk.Entry(frame, width=40)
#     entry_key.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

#     tk.Button(root, text="Extract Message", command=extract).pack(pady=10)
#     tk.Button(root, text="Back", command=show_home_screen).pack()

# # Start app at home screen
# show_home_screen()
# root.mainloop()


#---------------------------------------------------------x  MAIN CODE  X------------------------------------------------------#
# import tkinter as tk
# from encoder import open_encoder_window
# from decoder import open_decoder_window

# root = tk.Tk()
# root.title("Image Steganography (LSB-based)")
# root.geometry("600x400")

# def clear_window():
#     for widget in root.winfo_children():
#         widget.destroy()

# def show_home_screen():
#     clear_window()
#     tk.Label(root, text="Image Steganography", font=('Arial', 16)).pack(pady=20)

#     tk.Button(root, text="Encode Message", width=20,
#               command=lambda: open_encoder_window(root, show_home_screen, clear_window)).pack(pady=10)
#     tk.Button(root, text="Decode Message", width=20,
#               command=lambda: open_decoder_window(root, show_home_screen, clear_window)).pack(pady=10)

# # Start at home screen
# show_home_screen()
# root.mainloop()
#---------------------------------------------------------x  MAIN CODE  X------------------------------------------------------#




#pyinstaller --onefile --noconsole --icon=ana-de-armas-beach-4k-gw.ico --name=ImageSteganography main.py




import ttkbootstrap as tb
from encoder import open_encoder_window
from decoder import open_decoder_window

# Create root window with dark theme
root = tb.Window(themename="vapor")
root.title("Image Steganography (LSB-based)")

# Set window icon (use .ico file)
root.iconbitmap('ana-de-armas-beach-4k-gw.ico')

# Fullscreen
root.state("zoomed")

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

def show_home_screen():
    clear_window()
    
    # Outer frame to center everything vertically & horizontally
    outer_frame = tb.Frame(root)
    outer_frame.place(relx=0.5, rely=0.5, anchor="center")
    
    # Title Label
    tb.Label(outer_frame, 
             text="🔒 Image Steganography", 
             font=('Helvetica', 28, 'bold')).pack(pady=30)
    
    # Frame for side-by-side buttons
    button_frame = tb.Frame(outer_frame)
    button_frame.pack(pady=20)
    
    # Encode Button
    tb.Button(button_frame, text="Encode Message", 
              width=25, 
              bootstyle="success-outline",
              command=lambda: open_encoder_window(root, show_home_screen, clear_window)
             ).pack(side="left", padx=20)
    
    # Decode Button
    tb.Button(button_frame, text="Decode Message", 
              width=25, 
              bootstyle="info-outline",
              command=lambda: open_decoder_window(root, show_home_screen, clear_window)
             ).pack(side="left", padx=20)
    
    # Exit Button (below)
    tb.Button(outer_frame, text="Exit", 
              width=20, 
              bootstyle="danger-outline",
              command=root.destroy).pack(pady=40)

# Start at home screen
show_home_screen()
root.mainloop()
