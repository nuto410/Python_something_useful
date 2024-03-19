import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    filename = filedialog.askopenfilename(initialdir="/", title="Select Image File", filetypes=(("Image files", "*.jpg;*.jpeg;*.png;*.jfif"), ("All files", "*.*")))
    if filename:
        image = Image.open(filename)
        image.thumbnail((300, 300))
        photo = ImageTk.PhotoImage(image)
        canvas.create_image(150, 150, image=photo)
        canvas.photo = photo

def convert_image():
    if canvas.photo:
        formats = {"JPEG": "JPEG", "PNG": "PNG", "JFIF": "JPEG"}
        format_choice = format_var.get()
        if format_choice in formats:
            save_path = filedialog.asksaveasfilename(defaultextension=f".{format_choice.lower()}", filetypes=((f"{format_choice} files", f"*.{format_choice.lower()}"), ("All files", "*.*")), title=f"Save as {format_choice}")
            if save_path:
                # 將PhotoImage轉換為PIL Image
                image = ImageTk.getimage(canvas.photo)
                # 如果是PNG格式，保留RGBA模式
                if format_choice == "PNG":
                    image = image.convert("RGBA")
                else:
                    # 將圖像轉換為RGB模式
                    image = image.convert("RGB")
                # 將圖像保存到文件
                image.save(save_path, format=formats[format_choice])



root = tk.Tk()
root.title("Image Viewer")

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack()

format_var = tk.StringVar(root)
format_var.set("JPEG")  # 預設選擇 JPEG 格式
format_menu = tk.OptionMenu(root, format_var, "JPEG", "PNG", "JFIF")
format_menu.pack()

convert_button = tk.Button(root, text="Convert Image", command=convert_image)
convert_button.pack()

root.mainloop()
