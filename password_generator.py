import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_password():
    try:
        length = int(length_entry.get())

        if length < 6:
            messagebox.showwarning(
                "Warning",
                "Password must be at least 6 characters long."
            )
            return

        characters = ""

        if letters_var.get():
            characters += string.ascii_letters

        if numbers_var.get():
            characters += string.digits

        if symbols_var.get():
            characters += "!@#$%^&*()-_=+"

        if not characters:
            messagebox.showwarning(
                "Warning",
                "Please select at least one character type."
            )
            return

        password = "".join(
            random.choice(characters)
            for _ in range(length)
        )

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

        update_strength(password)

    except ValueError:
        messagebox.showerror(
            "Error",
            "Please enter a valid number."
        )


def update_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "!@#$%^&*()-_=+" for c in password):
        score += 1

    if score <= 2:
        strength_label.config(text="Strength: Weak")
    elif score <= 4:
        strength_label.config(text="Strength: Medium")
    else:
        strength_label.config(text="Strength: Strong")


def copy_password():
    password = password_entry.get()

    if not password:
        messagebox.showwarning(
            "Warning",
            "There is no password to copy."
        )
        return

    root.clipboard_clear()
    root.clipboard_append(password)

    messagebox.showinfo(
        "Copied",
        "Password copied to clipboard."
    )


root = tk.Tk()
root.title("Password Generator")
root.geometry("500x430")
root.resizable(False, False)

title_label = tk.Label(
    root,
    text="Password Generator",
    font=("Arial", 22, "bold")
)
title_label.pack(pady=20)

length_label = tk.Label(
    root,
    text="Password length:"
)
length_label.pack()

length_entry = tk.Entry(
    root,
    width=10,
    justify="center"
)
length_entry.insert(0, "12")
length_entry.pack(pady=5)

letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(
    root,
    text="Letters",
    variable=letters_var
).pack()

tk.Checkbutton(
    root,
    text="Numbers",
    variable=numbers_var
).pack()

tk.Checkbutton(
    root,
    text="Symbols",
    variable=symbols_var
).pack()

password_entry = tk.Entry(
    root,
    width=42,
    font=("Arial", 12),
    justify="center"
)
password_entry.pack(pady=15)

generate_button = tk.Button(
    root,
    text="Generate Password",
    command=generate_password,
    width=25
)
generate_button.pack()

copy_button = tk.Button(
    root,
    text="Copy Password",
    command=copy_password,
    width=25
)
copy_button.pack(pady=10)

strength_label = tk.Label(
    root,
    text="Strength: -",
    font=("Arial", 11, "bold")
)
strength_label.pack(pady=5)

root.mainloop()
