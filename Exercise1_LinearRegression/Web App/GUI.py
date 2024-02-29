# import libraries
from tkinter import *

import customtkinter
import customtkinter, tkinter
import tkinter as tk

# create a window
customtkinter.set_appearance_mode("dark")
root = customtkinter.CTk()
root.geometry("700x400")

# place text in front of pictures
text_label = tk.Label(root, text="Imagine that you want to develop a movie, \n but beofre you want to know whether is a movie going to be popular", font=("Helvetica", 22), fg="black", bg="white")
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
progressbar = customtkinter.CTkProgressBar(master=root)
progressbar.pack(padx=20, pady=90)

#########
button = customtkinter.CTkButton(master=root, text="Check potential rating")
button.place(relx=0.5, rely=0.5, anchor=CENTER)



root.mainloop()
