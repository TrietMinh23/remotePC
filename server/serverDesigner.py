import tkinter as tk
from tkinter import Button

class ServerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Server")

        custom_font = ("Helvetica", 9)

        self.button1 = self.create_button("Mở server", custom_font, self.start_server)
        self.button1.pack(padx=10, pady=10)

    def create_button(self, text, font, command):
        button = tk.Button(self.root, text=text, font=font, command=command, relief=tk.GROOVE)
        button.bind("<Enter>", self.on_enter)
        button.bind("<Leave>", self.on_leave)
        return button

    def on_enter(self, event):
        event.widget.config(bg="#DDDDDD")  # Change background color on hover

    def on_leave(self, event):
        event.widget.config(bg="SystemButtonFace")  # Reset background color on leave