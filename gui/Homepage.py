import tkinter as tk

class HomePage:

    def __init__(self, root):

        self.root = root

        self.frame = tk.Frame(
            root,
            bg="#5A5278"
        )

        self.frame.pack(fill="both", expand=True)

        title = tk.Label(
            self.frame,
            text="Numerical Methods Calculator",
            font=("Helvetica", 42, "bold"),
            fg="white",
            bg="#5A5278"
        )

        title.pack(pady=(150, 20))

        subtitle = tk.Label(
            self.frame,
            text="Solve Engineering Problems Using Numerical Methods",
            font=("Helvetica", 16),
            fg="white",
            bg="#5A5278"
        )

        subtitle.pack()

        self.start_btn = tk.Button(
            self.frame,
            text="START CALCULATING",
            font=("Helvetica", 18, "bold"),
            bg="#FF6B8A",
            fg="white",
            relief="flat",
            padx=40,
            pady=15,
            cursor="hand2"
        )

        self.start_btn.pack(pady=80)