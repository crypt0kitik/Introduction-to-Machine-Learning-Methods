from joblib import load
import pandas as pd
from tkinter import *
import customtkinter
import customtkinter, tkinter
import tkinter as tk
import PIL
from PIL import Image
from PIL import ImageTk
root = customtkinter.CTk()
def slider_event(value):
    print(value)

slider = customtkinter.CTkSlider(root, from_=0, to=100, command=slider_event)

root.mainloop()