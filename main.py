import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql

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

    def addFrameFun(self):
        self.addFrame = tk.Frame(self.root, bd=5, relief="ridge", bg=self.color(150, 180, 250))
        self.addFrame.place(width=self.width/3, height=self.height-220, x=self.width/3+80, y=100)

        roll_label = tk.Label(self.addFrame, text="Roll No:", bg=self.color(150, 180, 250), font=("Arial", 15, "bold"))
        roll_label.grid(row=0, column=0, padx=20, pady=30)
        self.roll = tk.Entry(self.addFrame, width=18, font=("Arial", 15, "bold"), bd=3)
        self.roll.grid(row=0, column=1, padx=10, pady=30)

        name_label = tk.Label(self.addFrame, text="Name:", bg=self.color(150, 180, 250), font=("Arial", 15, "bold"))
        name_label.grid(row=1, column=0, padx=20, pady=30)
        self.name = tk.Entry(self.addFrame, width=18, font=("Arial", 15, "bold"), bd=3)
        self.name.grid(row=1, column=1, padx=10, pady=30)

        sub_label = tk.Label(self.addFrame, text="Subject:", bg=self.color(150, 180, 250), font=("Arial", 15, "bold"))
        sub_label.grid(row=2, column=0, padx=20, pady=30)
        self.sub = tk.Entry(self.addFrame, width=18, font=("Arial", 15, "bold"), bd=3)
        self.sub.grid(row=2, column=1, padx=10, pady=30)

        grade_label = tk.Label(self.addFrame, text="Grade:", bg=self.color(150, 180, 250), font=("Arial", 15, "bold"))
        grade_label.grid(row=3, column=0, padx=20, pady=30)
        self.grade = tk.Entry(self.addFrame, width=18, font=("Arial", 15, "bold"), bd=3)
        self.grade.grid(row=3, column=1, padx=10, pady=30)

        ok_button = tk.Button(self.addFrame, text="Enter", bd=3, relief="raised", font=("Arial", 20, "bold"), width=20)
        ok_button.grid(row=4, column=0, padx=20, pady=30, columnspan=2)

    def addFunc(self):
        roll_no = self.roll.get()
        name = self.name.get()
        subject = self.sub.get()
        grade = self.grade.get()

        if roll_no and name and subject and grade:
            r_no = int(roll_no)
            try:
                self.database()
                self.cur.execute(
                    "insert into student(roll, name, sub, grade) values(%s, %s, %s, %s)",
                    (r_no, name, subject, grade)
                )
                self.con.commit()
                tk.messagebox.showinfo("Success", f"Student {name} with Roll No: {r_no} is registered successfully")
                self.desAdd()

                self.cur.execute("select * from student where r_no = %s",r_no)
                row = self.cur.fetchone()
                self.table.delete(*self.table.get_children())
                self.table.insert('', tk.END, values=row)
                self.con.close()

            except Exception as e:
                tk.messagebox.showerror("Error", f"Error: {e}")
                self.desAdd()

        else:
            tk.messagebox.showerror("Error", "Please fill all input fields")

    def desAdd(self):
        self.addFrame.destroy()

    def database(self):
        self.con = pymysql.connect(host="localhost", user="root", password="80285290", database="db_mh")
        self.cur = self.con.cursor()

    def __init__(self, root):
        self.table = None
        self.root = root
        self.root.title("Students record")

        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.width}x{self.height}+0+0")

        title = tk.Label(self.root, text = "Students Record Management System",
                         bd = 4, relief = "raised", bg = "light blue",
                         font = ("Times New Roman", 50, "bold"))
        title.pack(side = "top", fill = "x")

        # option frame
        optFrame = tk.Frame(self.root, bd = 5, relief="ridge", bg=self.color(230, 150, 200))
        optFrame.place(width=self.width/3, height=self.height-180, x=50, y=100)

        # buttons
        addBtn = tk.Button(optFrame, command=self.addFrameFun, text="Add Student", bd=3, relief="raised", bg="light gray", width=20, font=("Arial", 20, "bold"))
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