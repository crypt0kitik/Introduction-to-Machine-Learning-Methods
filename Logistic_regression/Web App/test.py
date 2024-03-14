from tkinter import *

root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

mylist = Listbox(root, yscrollcommand=scrollbar.set)
for line in range(100):
    text_label = tk.Label(root, text="Let's check whether a customer takes deposit \n Please, fill in data below",
                          font=("Helvetica", 22), fg="white", bg="black")  # Set background to transparent
    text_label.place(relx=0.5, rely=0.1, anchor="center")

    # PART 2.3: question "How old is the client?"
    # Create a new frame `age_form` to contain the Label and Entry widgets
    age_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
    age_form.place(relx=0.5, rely=0.25, anchor="center")

    # Create the Label and Entry widgets for the first question
    lbl_age = tk.Label(master=age_form, text="How old is the client?")
    ent_age = tk.Entry(master=age_form)
    lbl_age.grid(row=0, column=0, sticky="e")
    ent_age.grid(row=0, column=1)

    # Bind the <Return> event to the ent_age Entry widget
    ent_age.bind("<Return>", lambda event: print("Age entered:", ent_age.get()))

mylist.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=mylist.yview)

# Adding a button below the listbox and scrollbar
button = Button(root, text="Click me")
button.pack(side=TOP)

mainloop()
