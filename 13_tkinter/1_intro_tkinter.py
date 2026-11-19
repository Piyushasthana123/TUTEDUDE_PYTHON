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

#check button
check_option = tk.StringVar()
def check_option_task():
    print(check_option.get(),type(check_option.get()))

check_button = ttk.Checkbutton(text = "Agree with the term and condition", variable = check_option ,
                               command = check_option_task,onvalue = "yes" , offvalue = "no")
check_button.pack()

# redio button
def get_radio_value():
    print(radio_value.get())

radio_value = tk.StringVar()
option_1 = ttk.Radiobutton(text = "mango" , variable = radio_value, value = "mango", command = get_radio_value )
option_2 = ttk.Radiobutton(text = "orange", variable = radio_value, value = "orange", command = get_radio_value)
option_3 = ttk.Radiobutton(text = "Apple",  variable = radio_value, value = "Apple" ,command = get_radio_value)
option_1.pack()
option_2.pack()
option_3.pack()

#combox
selected_country = tk.StringVar()
countries = ttk.Combobox(textvariable = selected_country , values = ("india","canada","Austria","Australia"))
countries["state"] = "readonly"
countries.pack()

def display_country(event):
    msg = f"selceted_country is {selected_country.get()}"
    country_label = ttk.Label(text=msg)
    country_label.pack()
    # print(f"selected_country is {selected_country.get()}")

countries.bind("<<ComboboxSelected>>", display_country)

#Listbox
food_item = ("piza","garlic bread","burgar","nachos","salad")
fav_food = tk.StringVar(value=food_item)
food_list=tk.Listbox(listvariable = fav_food,height=5,selectmode="extended")
food_list.pack()

def get_fav_food(event):
    # print(fav_food.get())
    food_indices = food_list.curselection()
    for i in food_indices:
        print(food_list.get(i))

food_list.bind("<<ListboxSelect>>", get_fav_food)

#spinbox
def get_spin_value():
    print(f"carrent spin value: {spin_box.get()}")
counter = tk.IntVar(value = 10)
# spin_box = ttk.Spinbox(from_=0, to=20, textvariable = counter, wrap = True ,command = get_spin_value )
# spin_box = ttk.Spinbox(value = (10,15,20,25,30), textvariable = counter, wrap = True ,command = get_spin_value )
spin_box = ttk.Spinbox(value = tuple(range(5,105,5)), textvariable = counter, wrap = True ,command = get_spin_value )
spin_box.pack()
print(f"Initial value: {spin_box.get()}")

window.mainloop()