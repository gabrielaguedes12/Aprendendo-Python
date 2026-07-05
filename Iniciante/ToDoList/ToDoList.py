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
        
        #Cria um Frame para agrupar o campo de texto e o botão de adicionar lado a lado.
        input_frame = tk.Frame(self.root, bg="#f0f4f7")
        input_frame.pack(pady=10)
        
        #Entry é o widget de campo de texto — onde o usuário digita.
        self.task_entry = tk.Entry(
            input_frame,
            font = ("Helvetica", 12),
            width=30
        )
        
        self.task_entry.pack(side="left", padx=(0,10))
        
        add_button = tk.Button(
            input_frame,
            text= "Adicione tarefa",
            font=("Helvetica", 11, "bold"),
            bg= "#27ae60",
            fg="white",
            padx=10,
            command= self.add_task
        )        
        add_button.pack(side="left")
        
        list_frame = tk.Frame(self.root, bg="#f0f4f7")
        list_frame.pack(pady=10, fill="both", expand=True)
        
        self.task_listbox = tk.Listbox(
            list_frame,
            font=("Heveltica", 12),
            width= 45,
            height=10,
            activestyle="none"
        )