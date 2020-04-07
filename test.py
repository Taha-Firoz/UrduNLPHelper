import tkinter as tk


root = tk.Tk()

def clear():
    global trans_widget
    global hidden
    text = "Hello go\n"
    print(hidden)
    if hidden:
        print("here")
        trans_widget.pack()
        trans_widget.delete(1.0, tk.END)
        trans_widget.insert(tk.END, "{}\n".format(text))
    else:
        print("there")
        trans_widget.pack_forget()

    hidden = not(hidden)

hidden = False
trans_widget = tk.Text(root, height=5, width=50, font=("Helvetica", 32))
trans_widget.pack()

trans_var = tk.StringVar()
trans_var.set("To Roman Urdu")
button_trans = tk.Button(root, textvariable=trans_var, command=clear, height = 2, width = 15)
button_trans.pack()

root.mainloop() 
