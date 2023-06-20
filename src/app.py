import random
import string
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Generator")
        self.geometry("300x200")
        self.resizable(False, False)

        self.password = tk.StringVar()
        self.password.set("")
        self.password_label = tk.Label(self, font=("Arial", 15), textvariable=self.password)
        self.password_label.pack()

        self.generate_button = tk.Button(self, text="Generate", command=self.generate)
        self.generate_button.pack()

        self.copy_button = tk.Button(self, text="Copy", command=self.copy)
        self.copy_button.pack()

    def generate(self, event=None):
        self.password.set("".join(random.choices(string.ascii_letters + string.digits, k=16)))

    def copy(self, event=None):
        self.clipboard_clear()
        self.clipboard_append(self.password.get())