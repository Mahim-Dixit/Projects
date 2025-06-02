
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def move_image(dx, dy):
    # Move the image by dx (change in x) and dy (change in y)
    canvas.move(image_id, dx, dy)
    # Update the displayed position
    update_position()

def update_position():
    # Get the coordinates of the image
    coords = canvas.coords(image_id)
    position_label.config(text=f"Image position: ({int(coords[0])}, {int(coords[1])})")

# Initialize the Tkinter window
root = tk.Tk()
root.title("Move Image with Scrollbar")

# Create a Canvas widget
canvas = tk.Canvas(root, width=400, height=400, scrollregion=(0, 0, 800, 800))
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Add horizontal and vertical scrollbars
hbar = ttk.Scrollbar(root, orient=tk.HORIZONTAL, command=canvas.xview)
hbar.pack(side=tk.BOTTOM, fill=tk.X)
vbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
vbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)

# Load an image using PIL
image = Image.open("boy.jpg")
image = image.resize((150, 150))  # Resize the image if necessary
image_tk = ImageTk.PhotoImage(image)

# Add the image to the canvas and get its ID
image_id = canvas.create_image(200, 200, anchor=tk.NW, image=image_tk)

# Create buttons to move the image
move_up_button = tk.Button(root, text="Up", command=lambda: move_image(0, -10))
move_up_button.pack(side=tk.TOP)

move_down_button = tk.Button(root, text="Down", command=lambda: move_image(0, 10))
move_down_button.pack(side=tk.TOP)

move_left_button = tk.Button(root, text="Left", command=lambda: move_image(-10, 0))
move_left_button.pack(side=tk.TOP)

move_right_button = tk.Button(root, text="Right", command=lambda: move_image(10, 0))
move_right_button.pack(side=tk.TOP)

# Label to display the position of the image
position_label = tk.Label(root, text="")
position_label.pack(side=tk.TOP)

# Display initial position of the image
update_position()

root.mainloop()
