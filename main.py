import tkinter as tk
from gui.Homepage import HomePage
from gui.dashboard import Dashboard

root = tk.Tk()
root.title("Numerical Methods Calculator")
root.geometry("1200x750")
root.configure(bg="#5A5278")

home = HomePage(root)

def open_dashboard():
    home.frame.destroy()

    dashboard = Dashboard(root)
    dashboard.pack(fill="both", expand=True)

home.start_btn.config(command=open_dashboard)

root.mainloop()