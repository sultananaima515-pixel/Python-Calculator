import tkinter as tk

class Sidebar(tk.Frame):

    def __init__(self,parent,show_page):

        super().__init__(
            parent,
            bg="#34495E",
            width=250
        )

        self.pack_propagate(False)

        buttons = [

            ("Gaussian Elimination","gaussian"),
            ("Partial Pivoting","pivoting"),
            ("LU Decomposition","lu"),
            ("Simpson's 1/3","simpson13"),
            ("Simpson's 3/8","simpson38"),
            ("Euler Method","euler"),
            ("Error Analysis","error")
        ]

        for text,page in buttons:

            tk.Button(
                self,
                text=text,
                bg="#F76E82",
                fg="white",
                relief="flat",
                font=("Segoe UI",11,"bold"),
                command=lambda p=page:
                show_page(p)
            ).pack(
                fill="x",
                padx=15,
                pady=8,
                ipady=12
            )