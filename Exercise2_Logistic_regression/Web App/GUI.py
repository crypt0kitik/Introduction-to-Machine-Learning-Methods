# PART 1: Imports, load and test of the model

# import libraries
from joblib import load
import pandas as pd
from tkinter import *
import customtkinter
import customtkinter, tkinter
import tkinter as tk
import PIL
from PIL import Image
from PIL import ImageTk

lm = load("logmodel.joblib")

# tester_row = {
#     'age': 25,
#     'job': 2,
#     'marital': 1,
#     'education': 2,
#     'default': 1,
#     'balance': 5000,
#     'housing': 0,
#     'loan': 0,
#     'contact': 1,
#     'day': 5,
#     'month': 2,
#     'duration': 120,
#     'campaign': 1,
#     'pdays': -1,
#     'previous': 0,
#     'poutcome': 3,
# }
#
# # create a pandas DataFrame and scale the values
# tester_row = pd.DataFrame([tester_row])
#
# print("All probabilities by category:")
# print(lm.predict_proba(tester_row))
# print()
#
# # change these based on your original data
# labels = ["No", "Yes"]
#
# print("Does this customer take a deposit (Yes/No):")
# result = labels[logmodel.predict(tester_row)[0]]
# print(result)
# print("-------------------")

# PART 2: THE GUI
# create a window
customtkinter.set_appearance_mode("dark")
root = customtkinter.CTk()
root.geometry("700x400")

# PART 2.1: setting the background image
# open the image
image = PIL.Image.open("backimage.jpg")
background_image = customtkinter.CTkImage(image, size=(700, 400))

# Define a function to resize the background image
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

# PART 2.2: adding text about the goal of this GUI
# place text label
# the main text
text_label = tk.Label(root, text="Let's check whether a customer takes deposit or not \n Please, fill in data below",
                      font=("Helvetica", 22), fg="white", bg="black")  # Set background to transparent
text_label.place(relx=0.5, rely=0.1, anchor="center")

# PART 2.3: question "How old is the client?"
# Create a new frame `frm_form` to contain the Label and Entry widgets
frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
frm_form.place(relx=0.5, rely=0.25, anchor="center")

# Create the Label and Entry widgets for the first question
lbl_first_question = tk.Label(master=frm_form, text="How old is the client?")
ent_first_question = tk.Entry(master=frm_form)
lbl_first_question.grid(row=0, column=0, sticky="e")
ent_first_question.grid(row=0, column=1)

# PART 2.3: Choose a client's marital status
optionmenu_var = customtkinter.StringVar(value="divorced")  # set initial value

# button to choose - combobox
def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)

combobox = customtkinter.CTkOptionMenu(master=root,
                                       fg_color=("black"),
                                       bg_color=("black"),
                                       values=["divorced", "married", "single", "unknown"],
                                       command=optionmenu_callback,
                                       variable=optionmenu_var)

combobox.place(relx=0.5, rely=0.35, anchor="center")

# PART 2.4:Choose a client's education
optionmenu_var = customtkinter.StringVar(value="primary")  # set initial value

# button to choose - combobox
def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)

combobox = customtkinter.CTkOptionMenu(master=root,
                                       fg_color=("black"),
                                       bg_color=("black"),
                                       values=["primary", "secondary", "tertiary", "unknown"],
                                       command=optionmenu_callback,
                                       variable=optionmenu_var)

combobox.place(relx=0.5, rely=0.45, anchor="center")









# the function that is run when button is pressed
def set_text_by_button():

    # sample_text.get() contains the value in the textbox

    # inform the user if they provided wrong kind of data
    if not ent_first_question.get().isnumeric():
        result_var.set("Incorrect value, use integers.")
        ent_first_question.configure(foreground="red")
    else:
        ent_first_question.configure(foreground="black")

    # convert textbox value into integer if possible
    test_age = int(ent_first_question.get())

    # let's convert the user input into the
    # format that our model understands
    tester_row = {
        'age': test_age
    }

    # convert to pandas-format
    tester_row = pd.DataFrame([tester_row])

    # use our model to predict our tester_row data
    result = lm.predict(tester_row)[0]

    # set the result into the Label in the window
    result_var.set(f"Does this customer take a deposit: {round(float(result), 2)} $")


# helper function that allows us to press Enter to launch
# the button press function
def handle_enter(event):
    set_text_by_button()


# bind Enter-key from keyboard to helper function
root.bind("<Return>", handle_enter)

# Setting up the button, set_text_by_button()
# is passed as a command
set_up_button = tkinter.Button(root, height=1, width=16, text="Check the client",
                               command=set_text_by_button)

#set_up_button.place(relx=0.5, rely=1.9, anchor="center")
set_up_button.pack(pady=230)

root.mainloop()
