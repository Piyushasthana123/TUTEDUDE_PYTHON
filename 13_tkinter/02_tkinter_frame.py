import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("my application")
window.minsize(900,600)
my_frame = ttk.Frame()
my_frame.pack(side = "left" , fill = "both" , expand = True)

label1 = tk.Label(my_frame,text = "Hello World" , bg ="purple" )
label1.pack(side = "top",fill ="both",expand = True)

label2 = tk.Label(window,text = "How are you?" , bg = "red")
label2.pack(side="top",fill ="both", expand =True)

label3 = tk.Label(window,text = "Have a nice day!!",bg="skyblue")
label3.pack(side = "top",fill ="both", expand = True)

window.mainloop()
