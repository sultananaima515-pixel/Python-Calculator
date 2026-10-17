import tkinter as tk
from methods.simpson38 import simpson_three_eighth


class Simpson38Page(tk.Frame):

    def __init__(self, parent, console_callback):
        super().__init__(parent, bg="#3A3350")

        self.console_callback = console_callback
        self.entries = []

        self.build_ui()

    def build_ui(self):

        card = tk.Frame(self, bg="#4F476D", padx=25, pady=25)
        card.pack(padx=30, pady=30, fill="both", expand=True)

        tk.Label(
            card,
            text="Simpson's 3/8 Rule",
            bg="#4F476D",
            fg="white",
            font=("Segoe UI", 22, "bold")
        ).pack(anchor="w")

        # # function input
        # tk.Label(card, text="f(x)", bg="#4F476D", fg="white").pack(anchor="w")
        # self.expr_entry = tk.Entry(card, font=("Segoe UI", 12))
        # self.expr_entry.pack(pady=5)
        #
        # # lower bound
        # tk.Label(card, text="Lower bound (a)", bg="#4F476D", fg="white").pack(anchor="w")
        # self.a_entry = tk.Entry(card)
        # self.a_entry.pack(pady=5)
        #
        # # upper bound
        # tk.Label(card, text="Upper bound (b)", bg="#4F476D", fg="white").pack(anchor="w")
        # self.b_entry = tk.Entry(card)
        # self.b_entry.pack(pady=5)
        #
        # # intervals
        # tk.Label(card, text="Number of intervals (odd n)", bg="#4F476D", fg="white").pack(anchor="w")
        # self.n_entry = tk.Entry(card)
        # self.n_entry.pack(pady=5)

        # function input
        tk.Label(card, text="Function f(x)", bg="#4F476D", fg="white",font=("Segoe UI",12,"bold")).pack(anchor="w")
        self.expr_entry = tk.Entry(card, font=("Segoe UI", 12),bg="#4F476D")
        self.expr_entry.pack(pady=10, padx=10)

        # lower bound
        tk.Label(card, text="Lower Limit(a)", bg="#4F476D", fg="white",font=("Segoe UI",12,"bold")).pack(anchor="w")
        self.a_entry = tk.Entry(card,font=("Segoe UI", 12),bg="#4F476D")
        self.a_entry.pack(pady=10, padx=10)

        # upper bound
        tk.Label(card, text="Upper Limit(b)", bg="#4F476D", fg="white",font=("Segoe UI",12,"bold")).pack(anchor="w")
        self.b_entry = tk.Entry(card,bg="#4F476D",font=("Segoe UI", 12))
        self.b_entry.pack(pady=10,padx=10)

        # intervals
        tk.Label(card, text="Number of intervals (odd n)", bg="#4F476D", fg="white",font=("Segoe UI",12,"bold")).pack(anchor="w")
        self.n_entry = tk.Entry(card,bg="#4F476D",font=("Segoe UI", 12))
        self.n_entry.pack(pady=10,padx=10)

        tk.Button(
            card,
            text="Solve",
            bg="#F76E82",
            fg="white",
            relief="flat",
            font=("Segoe UI", 11, "bold"),
            width=18,
            height=1,
            command=self.solve
        ).pack(pady=10)

        self.result_frame = tk.Frame(card, bg="#4F476D")
        self.result_frame.pack(pady=10)




    def solve(self):

        try:
            expr = self.expr_entry.get()
            a = float(self.a_entry.get())
            b = float(self.b_entry.get())
            n = int(self.n_entry.get())


        except:
            self.console_callback("Invalid numeric input!")
            return

        log, result = simpson_three_eighth(expr,a,b,n)

        self.console_callback(log)

        self.show_result(result)

    def show_result(self, result):

        for widget in self.result_frame.winfo_children():
            widget.destroy()

        tk.Label(
            self.result_frame,
            text="Result",
            bg="#4F476D",
            fg="white",
            font=("Segoe UI", 12, "bold")
        ).pack()

        tk.Label(
            self.result_frame,
            text=f"Integral ≈ {result:.6f}",
            bg="#3A3350",
            fg="white",
            font=("Courier", 12),
            padx=10,
            pady=5
        ).pack(pady=10)

        self.result_frame.update()

    def reset_page(self):

        # self.size_entry.delete(
        #     0,
        #     tk.END
        # )

        # clear inputs
        self.expr_entry.delete(0, tk.END)
        self.a_entry.delete(0, tk.END)
        self.b_entry.delete(0, tk.END)
        self.n_entry.delete(0, tk.END)

        # clear result
        for widget in self.result_frame.winfo_children():
            widget.destroy()