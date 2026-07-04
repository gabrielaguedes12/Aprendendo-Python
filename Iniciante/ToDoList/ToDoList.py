import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-do List")
        self.root.geometry("500x450")
        self.root.resizable(False, False)
        self.root.configure(bg = "#f0f4f7")
        
        self.tasks = []
        self.setup_ui()
        
    def setup_ui(self):
        title_lable = tk.Label(
            self.root,
            text = "To-Do List",
            font = ("Helvetica", 22, "bold"),
            bg = "#f0f4f7",
            fg="#333"            
         )   
        title_lable.pack(pady=10)
        
        