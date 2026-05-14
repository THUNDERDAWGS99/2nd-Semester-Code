from tkinter import *
from tkinter import ttk










expr = ""
def press(key):
    global expr
    expr += str(key)
    display.set(expr)

def equal():
    global expr
    try:
        result = str(eval(expr))
        display.set(result)
        expr = result
    except:
        display.set("error")
        expr = ""

def clear():
    global expr
    expr = ""
    display.set("")

if __name__ == "__main__":
    #theme
    root = Tk()
    root.title("Calculator")
    root.geometry("320x380")
    #background
    root.configure(bg="#2c3e50")
    style = ttk.Style()
    style.theme_use('clam')

    display = StringVar()

  
    entry = Entry(root, textvariable=display, font=('Arial', 18), 
                  bg="#ecf0f1", fg="#2c3e50", borderwidth=0, justify='right')
    entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=20)

    #button order
    def create_button(text, row, col, cmd, span=1):
        btn = ttk.Button(root, text=text, command=cmd)
        btn.grid(row=row, column=col, columnspan=span, sticky="nsew", padx=3, pady=3)

    #button layout
    buttons = [
        ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
        ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
        ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
        ('0', 5, 0), ('.', 5, 1), ('C', 5, 2), ('+', 5, 3),
    ]

    for (txt, r, c) in buttons:
        if txt == 'C':
            create_button(txt, r, c, clear)
          
        else:
            create_button(txt, r, c, lambda t=txt: press(t))

    #equals button
    eq_btn = ttk.Button(root, text='=', command=equal)
    eq_btn.grid(row=6, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

    #spreads grid out evenly
    for i in range(4):
        root.grid_columnconfigure(i, weight=1)
    for i in range(7):
        root.grid_rowconfigure(i, weight=1)

    root.mainloop()
