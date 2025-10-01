# import tkinter as tk
# from tkinter import filedialog, messagebox
# from steganography import hide_message_lsb

# def open_encoder_window():
#     window = tk.Toplevel()
#     window.title("Encoder - Hide Message")

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

#     tk.Label(window, text="Cover Image:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
#     entry_image_path = tk.Entry(window, width=50)
#     entry_image_path.grid(row=0, column=1, padx=5, pady=5)
#     tk.Button(window, text="Upload Photo", command=browse_image).grid(row=0, column=2, padx=5, pady=5)

#     tk.Label(window, text="Secret Message:").grid(row=1, column=0, sticky=tk.NW, padx=5, pady=5)
#     entry_message = tk.Text(window, width=50, height=5)
#     entry_message.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

#     tk.Label(window, text="Key (Optional):").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
#     entry_key = tk.Entry(window, width=50)
#     entry_key.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

#     tk.Button(window, text="Hide Message", command=hide).grid(row=3, column=1, pady=10)





# import os
# import cv2
# from tkinter import filedialog, messagebox, Text, Entry, Button, Label, Frame
# from steganography import hide_message_lsb

# def open_encoder_window(root, show_home_screen, clear_window):
#     clear_window()

#     def browse_image():
#         file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg")])
#         entry_image_path.delete(0, "end")
#         entry_image_path.insert(0, file_path)

#     def take_photo():
#         cap = cv2.VideoCapture(0)
#         if not cap.isOpened():
#             messagebox.showerror("Error", "Cannot access webcam.")
#             return

#         messagebox.showinfo("Info", "Press 's' to capture photo, 'q' to quit.")

#         while True:
#             ret, frame = cap.read()
#             if not ret:
#                 messagebox.showerror("Error", "Failed to capture image.")
#                 break

#             cv2.imshow('Camera - Press "s" to capture', frame)
#             key = cv2.waitKey(1)

#             if key & 0xFF == ord('s'):
#                 captured_path = "captured.png"
#                 cv2.imwrite(captured_path, frame)
#                 entry_image_path.delete(0, "end")
#                 entry_image_path.insert(0, os.path.abspath(captured_path))
#                 messagebox.showinfo("Success", f"Photo saved as {captured_path}")
#                 break
#             elif key & 0xFF == ord('q'):
#                 break

#         cap.release()
#         cv2.destroyAllWindows()

#     def hide():
#         image_path = entry_image_path.get()
#         message = entry_message.get("1.0", "end").strip()
#         key = entry_key.get().strip()
#         output_path = "stego.png"

#         if not image_path or not message:
#             messagebox.showwarning("Warning", "Select image or take photo and enter a message.")
#             return

#         try:
#             hide_message_lsb(image_path, message, output_path, key)
#             messagebox.showinfo("Success", f"Message hidden in {output_path}")
#         except Exception as e:
#             messagebox.showerror("Error", str(e))

#     Label(root, text="Encoder - Hide Message", font=('Arial', 14)).pack(pady=10)

#     frame = Frame(root)
#     frame.pack(pady=10)

#     Label(frame, text="Cover Image:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
#     entry_image_path = Entry(frame, width=40)
#     entry_image_path.grid(row=0, column=1, padx=5, pady=5)

#     Button(frame, text="Upload Photo", command=browse_image).grid(row=0, column=2, padx=5, pady=5)
#     Button(frame, text="Take Photo", command=take_photo).grid(row=0, column=3, padx=5, pady=5)

#     Label(frame, text="Secret Message:").grid(row=1, column=0, sticky="nw", padx=5, pady=5)
#     entry_message = Text(frame, width=50, height=5)
#     entry_message.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

#     Label(frame, text="Key (Optional):").grid(row=2, column=0, sticky="w", padx=5, pady=5)
#     entry_key = Entry(frame, width=40)
#     entry_key.grid(row=2, column=1, columnspan=3, padx=5, pady=5)

#     Button(root, text="Hide Message", command=hide).pack(pady=10)
#     Button(root, text="Back", command=show_home_screen).pack()











# import os
# import cv2
# import ttkbootstrap as tb
# from tkinter import filedialog, messagebox
# from steganography import hide_message_lsb

# def open_encoder_window(root, show_home_screen, clear_window):
#     clear_window()

#     def browse_image():
#         file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg")])
#         entry_image_path.delete(0, "end")
#         entry_image_path.insert(0, file_path)

#     def take_photo():
#         cap = cv2.VideoCapture(0)
#         if not cap.isOpened():
#             messagebox.showerror("Error", "Cannot access webcam.")
#             return

#         messagebox.showinfo("Info", "Press 's' to capture photo, 'q' to quit.")

#         while True:
#             ret, frame = cap.read()
#             if not ret:
#                 messagebox.showerror("Error", "Failed to capture image.")
#                 break

#             cv2.imshow('Camera - Press "s" to capture', frame)
#             key = cv2.waitKey(1)

#             if key & 0xFF == ord('s'):
#                 captured_path = "captured.png"
#                 cv2.imwrite(captured_path, frame)
#                 entry_image_path.delete(0, "end")
#                 entry_image_path.insert(0, os.path.abspath(captured_path))
#                 messagebox.showinfo("Success", f"Photo saved as {captured_path}")
#                 break
#             elif key & 0xFF == ord('q'):
#                 break

#         cap.release()
#         cv2.destroyAllWindows()

#     def hide():
#         image_path = entry_image_path.get()
#         message = entry_message.get("1.0", "end").strip()
#         key = entry_key.get().strip()
#         output_path = "stego.png"

#         if not image_path or not message:
#             messagebox.showwarning("Warning", "Select image or take photo and enter a message.")
#             return

#         try:
#             hide_message_lsb(image_path, message, output_path, key)
#             messagebox.showinfo("Success", f"Message hidden in {output_path}")
#         except Exception as e:
#             messagebox.showerror("Error", str(e))

#     # Outer frame centered
#     outer_frame = tb.Frame(root)
#     outer_frame.place(relx=0.5, rely=0.5, anchor="center")

#     # Title
#     tb.Label(outer_frame, text="🖼️ Encoder - Hide Message", 
#              font=('Helvetica', 20, 'bold')).pack(pady=20)

#     # Main form frame
#     form_frame = tb.Frame(outer_frame)
#     form_frame.pack(pady=10)

#     # Cover Image
#     tb.Label(form_frame, text="Cover Image:", font=('Helvetica', 12)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
#     entry_image_path = tb.Entry(form_frame, width=50)
#     entry_image_path.grid(row=0, column=1, padx=5, pady=5, columnspan=2)

#     tb.Button(form_frame, text="Upload Photo", bootstyle="info-outline", command=browse_image).grid(row=0, column=3, padx=5, pady=5)
#     tb.Button(form_frame, text="Take Photo", bootstyle="secondary-outline", command=take_photo).grid(row=0, column=4, padx=5, pady=5)

#     # Secret Message
#     tb.Label(form_frame, text="Secret Message:", font=('Helvetica', 12)).grid(row=1, column=0, sticky="nw", padx=5, pady=5)
#     entry_message = tb.Text(form_frame, width=50, height=6, font=('Consolas', 11))
#     entry_message.grid(row=1, column=1, columnspan=4, padx=5, pady=5)

#     # Key
#     tb.Label(form_frame, text="Key (Optional):", font=('Helvetica', 12)).grid(row=2, column=0, sticky="w", padx=5, pady=5)
#     entry_key = tb.Entry(form_frame, width=30, show="*")
#     entry_key.grid(row=2, column=1, columnspan=4, padx=5, pady=5)

#     # Buttons
#     button_frame = tb.Frame(outer_frame)
#     button_frame.pack(pady=20)

#     tb.Button(button_frame, text="Hide Message", bootstyle="success", width=20, command=hide).pack(side="left", padx=15)
#     tb.Button(button_frame, text="Back", bootstyle="danger-outline", width=15, command=show_home_screen).pack(side="left", padx=15)








#---------------------------------------------------------x  MAIN CODE  X------------------------------------------------------#
import os 
import cv2
import time
import traceback
from datetime import datetime
import ttkbootstrap as tb
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from steganography import hide_message_lsb

def open_encoder_window(root, show_home_screen, clear_window):
    clear_window()

    preview_label = None
    preview_img = None

    def update_preview(image_path):
        nonlocal preview_img
        try:
            img = Image.open(image_path)
            img.thumbnail((400, 300))
            preview_img = ImageTk.PhotoImage(img)
            preview_label.config(image=preview_img)
            preview_label.image = preview_img
        except Exception as e:
            log_error(e)
            messagebox.showerror("Error", f"Cannot preview image: {e}")

    def log_error(e):
        with open("error_log.txt", "a") as f:
            f.write(traceback.format_exc() + "\n")

    def browse_image():
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            entry_image_path.delete(0, "end")
            entry_image_path.insert(0, file_path)
            update_preview(file_path)

    def take_photo():
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            messagebox.showerror("Error", "Cannot access webcam.")
            return

        messagebox.showinfo("Info", "Press 's' to capture photo, 'q' to quit.")

        while True:
            ret, frame = cap.read()
            if not ret:
                messagebox.showerror("Error", "Failed to capture image.")
                break

            cv2.imshow('Camera - Press "s" to capture', frame)
            key = cv2.waitKey(1)

            if key & 0xFF == ord('s'):
                filename = f"captured_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                cv2.imwrite(filename, frame)
                entry_image_path.delete(0, "end")
                entry_image_path.insert(0, os.path.abspath(filename))
                update_preview(filename)
                messagebox.showinfo("Success", f"Photo saved as {filename}")
                break
            elif key & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def simulate_progress():
        for i in range(1, 101, 5):
            progressbar['value'] = i
            root.update_idletasks()
            time.sleep(0.02)

    def hide():
        image_path = entry_image_path.get()
        message = entry_message.get("1.0", "end").strip()
        key = entry_key.get().strip()

        if not image_path or not message:
            messagebox.showwarning("Warning", "Select image or take photo and enter a message.")
            return

        if not image_path.lower().endswith(('.png', '.jpg', '.jpeg')):
            messagebox.showwarning("Invalid Format", "Please use a PNG or JPG image.")
            return

        output_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG Image", "*.png")],
            title="Save stego image as..."
        )
        if not output_path:
            return  # User cancelled

        try:
            progressbar['value'] = 0
            root.update_idletasks()
            simulate_progress()

            hide_message_lsb(image_path, message, output_path, key)

            progressbar['value'] = 100
            root.update_idletasks()

            update_preview(output_path)

            entry_message.delete("1.0", "end")
            entry_key.delete(0, "end")

            messagebox.showinfo("Success", f"Message hidden in {output_path}")
        except Exception as e:
            log_error(e)
            messagebox.showerror("Error", str(e))
            progressbar['value'] = 0

    # Outer frame centered
    outer_frame = tb.Frame(root)
    outer_frame.place(relx=0.5, rely=0.5, anchor="center")

    tb.Label(outer_frame, text="🖼️ Encoder - Hide Message", 
             font=('Helvetica', 20, 'bold')).pack(pady=20)

    preview_label = tb.Label(outer_frame)
    preview_label.pack(pady=10)

    progressbar = tb.Progressbar(
        outer_frame, orient="horizontal", 
        mode="determinate", length=400, bootstyle="info-striped"
    )
    progressbar.pack(pady=10)

    form_frame = tb.Frame(outer_frame)
    form_frame.pack(pady=10)

    tb.Label(form_frame, text="Cover Image:", font=('Helvetica', 12)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    entry_image_path = tb.Entry(form_frame, width=50)
    entry_image_path.grid(row=0, column=1, padx=5, pady=5, columnspan=2)

    tb.Button(form_frame, text="Upload Photo", bootstyle="info-outline", command=browse_image).grid(row=0, column=3, padx=5, pady=5)
    tb.Button(form_frame, text="Take Photo", bootstyle="secondary-outline", command=take_photo).grid(row=0, column=4, padx=5, pady=5)

    tb.Label(form_frame, text="Secret Message:", font=('Helvetica', 12)).grid(row=1, column=0, sticky="nw", padx=5, pady=5)
    entry_message = tb.Text(form_frame, width=50, height=6, font=('Consolas', 11))
    entry_message.grid(row=1, column=1, columnspan=4, padx=5, pady=5)

    tb.Label(form_frame, text="Key (Optional):", font=('Helvetica', 12)).grid(row=2, column=0, sticky="w", padx=5, pady=5)
    entry_key = tb.Entry(form_frame, width=30, show="*")
    entry_key.grid(row=2, column=1, columnspan=4, padx=5, pady=5)

    button_frame = tb.Frame(outer_frame)
    button_frame.pack(pady=15)

    tb.Button(button_frame, text="Hide Message", bootstyle="success", width=20, command=hide).pack(side="left", padx=15)
    tb.Button(button_frame, text="Back", bootstyle="danger-outline", width=15, command=show_home_screen).pack(side="left", padx=15)
#---------------------------------------------------------x  MAIN CODE  X------------------------------------------------------#