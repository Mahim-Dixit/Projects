import tkinter as tk
from tkinter import Scale, Label
from PIL import Image, ImageTk

class ImageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Resizer and Positioner")

        # Load the image
        self.original_image = Image.open("boy.jpg")  # Replace with your image path
        self.image = ImageTk.PhotoImage(self.original_image)

        # Create the label to display the image
        self.image_label = Label(root, image=self.image)
        self.image_label.place(x=50, y=50)  # Initial position

        # Create sliders for width and height
        self.width_slider = Scale(root, from_=100, to_=self.original_image.width, orient="horizontal", label="Width")
        self.width_slider.set(self.original_image.width)
        self.width_slider.pack()

        self.height_slider = Scale(root, from_=100, to_=self.original_image.height, orient="vertical", label="Height")
        self.height_slider.set(self.original_image.height)
        self.height_slider.pack(side="right")

        # Update button
        self.update_button = tk.Button(root, text="Update Image", command=self.update_image)
        self.update_button.pack()

        # Position label
        self.position_label = Label(root, text="Position: (50, 50)")
        self.position_label.pack()

    def update_image(self):
        # Get the current slider values
        new_width = self.width_slider.get()
        new_height = self.height_slider.get()

        # Resize the image
        resized_image = self.original_image.resize((new_width, new_height))
        self.image = ImageTk.PhotoImage(resized_image)

        # Update the image on the label
        self.image_label.config(image=self.image)

        # Update the position label
        x, y = self.image_label.winfo_x(), self.image_label.winfo_y()
        self.position_label.config(text=f"Position: ({x}, {y})")

# Create the main window
root = tk.Tk()
app = ImageApp(root)
root.mainloop()


