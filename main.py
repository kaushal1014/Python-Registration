#By Kaushal Patil
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Resitration")
root.geometry("500x500")
text_input = StringVar()

def onclick():
    messagebox.showinfo("Hello", "You have successful registered.")


username = Label(root, text="New Username", height=1).place(x=160, y=100)
# for username
textbox1 = Text(root, height=1, width=15).place(x=265, y=100)

password = Label(root, text="New Password", height=1).place(x=160, y=130)
# for password
textbox2 = Text(root, height=1, width=15).place(x=265, y=130)

gender = Label(root, height=1, text="Gender:", pady=10).place(x=160, y=150)
radiobt = Radiobutton(root, variable=text_input, text="Female", value=1).place(x=300, y=158)
radiobt2 = Radiobutton(root, variable=text_input, text="Male", value=2).place(x=220, y=158)
radiobt3 = Radiobutton(root, variable=text_input, text="Other", value=3).place(x=380, y=158)

Yourcountry = Label(root, text="Your Country:", pady=10).place(x=160, y=190)
list_countries = ["India", "USA", "Canada", "Australia", "Russia", "Nepal", "England", "France"]
var2 = StringVar()
dropdown = OptionMenu(root, var2, *list_countries)
dropdown.config(width=10)
var2.set("Select")
dropdown.place(x=250, y=194)
