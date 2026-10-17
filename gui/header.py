import tkinter as tk


class Header(tk.Frame):

    def __init__(self, parent, reset_callback, clear_callback):

        super().__init__(
            parent,
            bg="#4A5477",
            height=70
        )

        self.pack_propagate(False)

        tk.Label(
            self,
            text="Numerical Methods Calculator",
            bg="#4A5477",
            fg="white",
            font=("Segoe UI", 20, "bold")
        ).pack(
            side="left",
            padx=20
        )

        right = tk.Frame(
            self,
            bg="#4A5477"
        )

        right.pack(
            side="right",
            padx=20
        )

        tk.Button(
            right,
            text="↻ Reset",
            font=("Segoe UI", 18, "bold"),
            bd=0,
            bg="#4A5477",
            fg="white",
            command=reset_callback
        ).pack(
            side="left",
            padx=10
        )

        tk.Button(
            right,
            text="🗑 Clear",
            font=("Segoe UI", 18, "bold"),
            bd=0,
            bg="#4A5477",
            fg="white",
            command=clear_callback
        ).pack(
            side="left",
            padx=10
        )