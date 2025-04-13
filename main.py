import tkinter as tk

class student():

    def color(self, r, g, b):
        return f"#{r:02x}{g:02x}{b:02x}"

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

        addBtn = tk.Button(optFrame, text="Add Student", bd=3, relief="raised", bg="light gray", width=20, font=("Arial", 20, "bold"))

        # detail frame
        detFrame = tk.Frame(self.root, bd=5, relief="ridge", bg=self.color(150, 230, 120))
        detFrame.place(width=self.width/2+40, height=self.height-180, x=self.width/3+120, y=100)


root = tk.Tk()
object = student(root)
root.mainloop()