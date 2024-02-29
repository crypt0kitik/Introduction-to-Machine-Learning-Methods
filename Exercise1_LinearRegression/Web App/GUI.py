# import libraries
from tkinter import *
import customtkinter
import customtkinter, tkinter
import tkinter as tk
import PIL
from PIL import Image
from PIL import ImageTk

# create a window
customtkinter.set_appearance_mode("dark")
root = customtkinter.CTk()
root.geometry("700x400")

image = PIL.Image.open("Image.png")
background_image = customtkinter.CTkImage(image, size=(700, 400))
# Define a function to resize the image
def resize_image(event=None):
    new_width = root.winfo_width()
    new_height = root.winfo_height()
    # if you have issues with ANTIALIAS
    # you need Pillow==9.5.0 version
    resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(resized_image)
    bg_lbl.configure(image=photo)
    bg_lbl.image = photo  # Keep a reference to avoid garbage collection

# Create a background label with the initial image
bg_lbl = customtkinter.CTkLabel(root, text="", width=700, height=400)
bg_lbl.place(x=0, y=0)

# Call the resize_image function when the window is resized
root.bind("<Configure>", resize_image)

# Initialize the image size
resize_image()

# place text label
text_label = tk.Label(root, text="Imagine that you want to develop a movie, \n but before you want to know whether the movie is going to be popular",
                      font=("Helvetica", 22), fg="white", bg="black")  # Set background to transparent
text_label.place(relx=0.5, rely=0.1, anchor="center")

################
optionmenu_var = customtkinter.StringVar(value="option 2")  # set initial value
def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)

combobox = customtkinter.CTkOptionMenu(master=root,
                                       values=["option 1", "option 2"],
                                       command=optionmenu_callback,
                                       variable=optionmenu_var)
combobox.pack(padx=20, pady=80)

#########
button = customtkinter.CTkButton(master=root, text="Check potential rating")
button.place(relx=0.5, rely=0.5, anchor=CENTER)



root.mainloop()
