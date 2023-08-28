import tkinter as tk
import random
import string

def generate_password():
    password_length = int(length_var.get())
    if password_length < 4:
        password_var.set("Minimum length is 4")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    password_var.set(password)

root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Password Length:")
length_label.pack()

length_var = tk.StringVar()
length_entry = tk.Entry(root, textvariable=length_var)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

password_var = tk.StringVar()
password_label = tk.Label(root, textvariable=password_var)
password_label.pack()

root.mainloop()
