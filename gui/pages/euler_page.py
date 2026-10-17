import tkinter as tk
from methods.euler import euler_method


class EulerPage(tk.Frame):

    def __init__(self, parent, console_callback):
        super().__init__(parent, bg="#3A3350")

        self.console_callback = console_callback
        self.build_ui()

    def build_ui(self):

        card = tk.Frame(self, bg="#4F476D", padx=25, pady=25)
        card.pack(padx=30, pady=30, fill="both", expand=True)

        tk.Label(
            card,
            text="Euler Method",
            bg="#4F476D",
            fg="white",
            font=("Segoe UI", 22, "bold")
        ).pack(anchor="w")


        # Function input
        tk.Label(
            card,
            text="Function f(x,y)",
            bg="#4F476D",
            fg="white",
            font=("Segoe UI", 12)
        ).pack(anchor="w")

        self.func_entry = tk.Entry(
            card,
            font=("Segoe UI", 12),
            bg="#2E3A59",
            fg="white",
            insertbackground="white",
            width=30
        )
        self.func_entry.pack(anchor="w", pady=(5, 15))


        # Initial x0 and y0
        row1 = tk.Frame(card, bg="#4F476D")
        row1.pack(anchor="w", pady=5)

        tk.Label(
            row1,
            text="Initial x0",
            bg="#4F476D",
            fg="white"
        ).grid(row=0, column=0, padx=10)

        tk.Label(
            row1,
            text="Initial y0",
            bg="#4F476D",
            fg="white"
        ).grid(row=0, column=1, padx=10)

        self.x0_entry = tk.Entry(
            row1,
            width=12,
            bg="#2E3A59",
            fg="white",
            insertbackground="white"
        )

        self.y0_entry = tk.Entry(
            row1,
            width=12,
            bg="#2E3A59",
            fg="white",
            insertbackground="white"
        )

        self.x0_entry.grid(row=1, column=0, padx=10, pady=5)
        self.y0_entry.grid(row=1, column=1, padx=10, pady=5)


        # Step size and Target x
        row2 = tk.Frame(card, bg="#4F476D")
        row2.pack(anchor="w", pady=10)

        tk.Label(
            row2,
            text="Step size (h)",
            bg="#4F476D",
            fg="white"
        ).grid(row=0, column=0, padx=10)

        tk.Label(
            row2,
            text="Target x",
            bg="#4F476D",
            fg="white"
        ).grid(row=0, column=1, padx=10)

        self.h_entry = tk.Entry(
            row2,
            width=12,
            bg="#2E3A59",
            fg="white",
            insertbackground="white"
        )

        self.xn_entry = tk.Entry(
            row2,
            width=12,
            bg="#2E3A59",
            fg="white",
            insertbackground="white"
        )

        self.h_entry.grid(row=1, column=0, padx=10, pady=5)
        self.xn_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Button(
        card,
        text="Solve",
        bg="#F76E82",
        fg="white",
        relief="flat",
            width=20,
            font=("Segoe UI", 16, "bold"),
        command=self.solve
    ).pack(pady=10)

    # ONLY RESULT FRAME
        self.result_frame = tk.Frame(card, bg="#4F476D")
        self.result_frame.pack(pady=10)

    def solve(self):

        try:
            expr = self.func_entry.get()
            x0 = float(self.x0_entry.get())
            y0 = float(self.y0_entry.get())
            xn = float(self.xn_entry.get())
            h = float(self.h_entry.get())

        except:
            self.console_callback("Invalid input values!")
            return

        log, steps, final_value = euler_method(expr, x0, y0, h, xn)

        # console gets FULL iteration log
        self.console_callback(log)

        # GUI shows ONLY final result
        self.show_result(final_value)

    def show_result(self, final_value):

        for w in self.result_frame.winfo_children():
            w.destroy()

        tk.Label(
            self.result_frame,
            text="Final Result",
            bg="#4F476D",
            fg="white",
            font=("Segoe UI", 12, "bold")
        ).pack()

        tk.Label(
            self.result_frame,
            text=f"y(xn) ≈ {final_value:.6f}",
            bg="#3A3350",
            fg="white",
            font=("Courier", 14, "bold"),
            padx=10,
            pady=8
        ).pack(pady=10)

    def reset_page(self):

        self.func_entry.delete(0, tk.END)
        self.x0_entry.delete(0, tk.END)
        self.y0_entry.delete(0, tk.END)
        self.xn_entry.delete(0, tk.END)
        self.h_entry.delete(0, tk.END)

        for w in self.result_frame.winfo_children():
            w.destroy()