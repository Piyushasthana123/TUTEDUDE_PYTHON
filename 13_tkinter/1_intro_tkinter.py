import tkinter as tk
import tkinter.font as tfont
# import tkinter as ttk
from tkinter import ttk

#TK
# window = tk.Tk()
# window.title("first window")
# window.minsize(width = 800,height = 600)
#
# #label
# custom_font = tfont.Font(family="Times New Roman", size=20, slant= 'italic', weight='bold' )
# label = tk.Label(window, text="Hello, Tkinter World!\nhave a nice day!", font=custom_font)
# # label = tk.Label(window, text="Hello, Tkinter World!\nhave a nice day!")
# label.pack()
# # label.pack(expand = True)
# # label.config(font=("courier New",25 , "underline"))
# # label["text"]="Have a nice day!"
# label.config(text="My first app")
#
# # counter = 0
# # def function():
# #     global counter
# #     counter +=1
# #     label.config(text= f"Thanks for clicking on this button{counter} times")
#
# def function():
#     input_text = user_input.get()
#     label.config(text = input_text)
#
#
# # taking user input using Entry
# # user_input = tk.Entry(width=50, show="*")
# user_input = tk.Entry(width=50)
# user_input.pack()
#
#
# #Buttons
# button = tk.Button(text = "click me", command = function)
# button.pack()

# ttk module imported

window = tk.Tk()
window.title("First Application")
window.minsize(width = 800,height = 600)

#label
custom_font = tfont.Font(family="Times New Roman", size=20, slant= 'italic', weight='bold' )
label = ttk.Label(window, text="Hello, Tkinter World!\nhave a nice day!", font=custom_font)
# label = tk.Label(window, text="Hello, Tkinter World!\nhave a nice day!")
label.pack()
# label.pack(expand = True)
# label.config(font=("courier New",25 , "underline"))
# label["text"]="Have a nice day!"
label.config(text="My first app",padding = "15")

# counter = 0
# def function():
#     global counter
#     counter +=1
#     label.config(text= f"Thanks for clicking on this button{counter} times")

def function():
    input_text = user_input.get()
    label.config(text = input_text)


# taking user input using Entry
# user_input = tk.Entry(width=50, show="*")
user_input = ttk.Entry(width=50)
user_input.pack()


#Buttons
button = ttk.Button(text = "click me", command = function,padding = "15")
button.pack()
Quit_button = ttk.Button(text = "Quit", command = window.destroy)
Quit_button.pack()

# separator
sep = ttk.Separator(window, orient="horizontal")
sep.pack(fill="x")

#multiple line text
text = tk.Text(window, height = 20, width = 50)
text.pack(padx=20, pady=10)
text.focus() # for cursor

#insert default text ( 1.0 means 1 is line no and 0 is 0th character
text.insert("1.0","Hello World! thanks for writing")

def get_text():
    text_data = text.get("1.0", "end")
    print(text_data)
text_btn = ttk.Button(text = "fetch text", command = get_text)
text_btn.pack()

# text["state"] = "disabled"
#
# def enable_text():
#     text.config(state="normal")
#
# button = ttk.Button(text = "Enable text box", command = enable_text)
# button.pack()

window.mainloop()