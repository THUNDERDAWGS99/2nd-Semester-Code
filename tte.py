import tkinter as tk
from tkinter import messagebox




def show_message():
    """Callback for the listbox selection and message box button."""
    try:
        selection = listbox.get(listbox.curselection())
        output_label.config(text=f"Selected: {selection}")
        messagebox.showinfo("Selection", f"You clicked on: {selection}")
    except tk.TclError:
        #happens whn nothing is selected
        messagebox.showwarning("Please select something ")

def update_label(event):
    #happens when user selects something
    selected_indices = listbox.curselection()
    if selected_indices:
        item = listbox.get(selected_indices[0])
        output_label.config(text=f"Listbox item selected: {item}")






#main window
root = tk.Tk()
root.title("GUI")
root.geometry("400x450")

#entry box
tk.Label(root, text="Enter something random").pack(pady=5)
entry_box = tk.Entry(root)
entry_box.pack(pady=5)

#output
output_label = tk.Label(root, text="Waiting for your selection", fg="blue")
output_label.pack(pady=10)

#listbox
tk.Label(root, text="Select an item:").pack(pady=5)
listbox = tk.Listbox(root)
items = ["Hotdogs", "Pizza", "Arbys Meat Mountain", "Roblox", "Chicken"]
for item in items:
    listbox.insert(tk.END, item)
listbox.pack(pady=5)
listbox.bind('<<ListboxSelect>>', update_label)

#message box
msg_button = tk.Button(root, text="Show message", command=show_message)
msg_button.pack(pady=10)

#quit
quit_button = tk.Button(root, text="Quit", command=root.destroy, bg="red", fg="white")
quit_button.pack(pady=20)




root.mainloop()
