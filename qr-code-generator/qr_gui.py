import tkinter
from customtkinter import *
import os

st = CTk()
st.title("Generate Qr App")
st.geometry("500x500")
st.config(bg="black")

label = CTkLabel(st, text="Generate QR from Url",width=120, height=25,font=("Roboto", 20,"bold"), corner_radius=48)
label.place(relx=0.5, rely=0.10, anchor=tkinter.CENTER)

entry = CTkEntry(st,
                               placeholder_text="CTkEntry",
                               width=420,
                               height=50,
                               border_width=2,
                               corner_radius=30)
entry.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

button = CTkButton(st,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=38,
                                 text="CTkButton")
button.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)


st.mainloop()
