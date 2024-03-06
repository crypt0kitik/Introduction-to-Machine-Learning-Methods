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

# open the image
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

# Create a new frame `frm_form` to contain the Label and Entry widgets
frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
frm_form.place(relx=0.5, rely=0.25, anchor="center")

# Create the Label and Entry widgets for the first question
lbl_first_question = tk.Label(master=frm_form, text="In which year you want to publish your movie?")
ent_first_question = tk.Entry(master=frm_form)
lbl_first_question.grid(row=0, column=0, sticky="e")
ent_first_question.grid(row=0, column=1)

optionmenu_var = customtkinter.StringVar(value="option 2")  # set initial value

# button to choose - combobox
def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)

combobox = customtkinter.CTkOptionMenu(master=root,
                                       fg_color=("black"),
                                       bg_color=("black"),
                                       values=["option 1", "option 2", "option 3"],
                                       command=optionmenu_callback,
                                       variable=optionmenu_var)

combobox.place(relx=0.5, rely=0.35, anchor="center")

# button to submit and calculate the result
button = customtkinter.CTkButton(master=root, fg_color=("black"), text="Check potential rating")
button.place(relx=0.5, rely=0.5, anchor=CENTER)



root.mainloop()
