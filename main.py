import tkinter as tk
from tkinter import ttk

class student():

    def color(self, r, g, b):
        return f"#{r:02x}{g:02x}{b:02x}"
    
    def tabFun(self):
        tabFrame = tk.Frame(self.detFrame, bd=4, relief="sunken", bg="cyan")
        tabFrame.place(width=self.width/2, height=self.height-280, x=23, y=70)

        x_scroll = tk.Scrollbar(tabFrame, orient="horizontal")
        x_scroll.pack(side="bottom", fill="x")

        y_scroll = tk.Scrollbar(tabFrame, orient="vertical")
        y_scroll.pack(side="right", fill="y")

        self.table = ttk.Treeview(tabFrame, xscrollcommand=x_scroll.set,
                                  yscrollcommand=y_scroll.set,
                                  columns=("roll", "name", "sub", "grade"))

        x_scroll.config(command = self.table.xview)
        y_scroll.config(command = self.table.yview)

        self.table.heading("roll", text="Roll_No")
        self.table.heading("name", text="Name")
        self.table.heading("sub", text="Subject")
        self.table.heading("grade", text="Grade (CGPA)")
        self.table["show"]= "headings"

        self.table.pack(fill="both", expand=1)

    def __init__(self, root):
        self.root = root
        self.root.title("Students record")

        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.width}x{self.height}+0+0")

        title = tk.Label(self.root, text = "Student record management system",
                         bd = 4, relief = "raised", bg = "light blue",
                         font = ("Times New Roman", 50, "bold"))
        title.pack(side = "top", fill = "x")

        # option frame
        optFrame = tk.Frame(self.root, bd = 5, relief="ridge", bg=self.color(230, 150, 200))
        optFrame.place(width=self.width/3, height=self.height-180, x=50, y=100)

        # buttons
        addBtn = tk.Button(optFrame, text="Add Student", bd=3, relief="raised", bg="light gray", width=20, font=("Arial", 20, "bold"))
        addBtn.grid(row=0, column=0, padx=30, pady=25)

        searchBtn = tk.Button(optFrame, text="Search Student", bd=3, relief="raised", bg="light gray", width=20, font=("Arial", 20, "bold"))
        searchBtn.grid(row=1, column=0, padx=30, pady=25)

        updateBtn = tk.Button(optFrame, text="Update Record", bd=3, relief="raised", bg="light gray", width=20, font=("Arial", 20, "bold"))
        updateBtn.grid(row=2, column=0, padx=30, pady=25)

        allBtn = tk.Button(optFrame, text="Show All", bd=3, relief="raised", bg="light gray", width=20, font=("Arial", 20, "bold"))
        allBtn.grid(row=3, column=0, padx=30, pady=25)

        rmvBtn = tk.Button(optFrame, text="Remove Student", bd=3, relief="raised", bg="light gray", width=20, font=("Arial", 20, "bold"))
        rmvBtn.grid(row=4, column=0, padx=30, pady=25)

        # detail frame
        self.detFrame = tk.Frame(self.root, bd=5, relief="ridge", bg=self.color(150, 230, 120))
        self.detFrame.place(width=self.width/2+50, height=self.height-180, x=self.width/3+120, y=100)

        label1 = tk.Label(self.detFrame, text="Record Details", font=("Arial", 30, "bold"), bg=self.color(150, 230, 120))
        label1.pack(side="top", fill="x")

        self.tabFun()

root = tk.Tk()
object = student(root)
root.mainloop()