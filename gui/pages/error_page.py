import tkinter as tk
from methods.error_analysis import calculate_errors


class ErrorPage(tk.Frame):

    def __init__(self, parent, console_callback):
        super().__init__(parent, bg="#3A3350")

        self.console_callback = console_callback

        self.build_ui()

    def build_ui(self):

        card = tk.Frame(self, bg="#4F476D", padx=25, pady=25)
        card.pack(padx=30, pady=30, fill="both", expand=True)

        tk.Label(
            card,
            text="Error Analysis",
            bg="#4F476D",
            fg="white",
            font=("Segoe UI", 22, "bold")
        ).pack(anchor="w")

        input_frame = tk.Frame(card, bg="#4F476D")
        input_frame.pack(anchor="w", pady=10)

        tk.Label(input_frame, text="Exact Value", bg="#4F476D", fg="white",font=("Segoe UI",12,"bold")).grid(row=0, column=0, padx=5, pady=5)
        self.exact_entry = tk.Entry(input_frame, width=20)
        self.exact_entry.grid(row =0,column = 1,padx=5, pady=5)


        tk.Label(input_frame, text="Approx Value", bg="#4F476D", fg="white",font=("Segoe UI",12,"bold")).grid(row=1, column=0, padx=5, pady=5)
        self.approx_entry = tk.Entry(input_frame, width=20)

        self.approx_entry.grid(row=1,column=1,padx=5, pady=5)

        tk.Button(
            card,
            text="Calculate Error",
            bg="#F76E82",
            fg="white",
            relief="flat",
            font=("Segoe UI", 16, "bold"),
            width=20,
            command=self.solve
        ).pack(pady=10)

        self.result_frame = tk.Frame(card, bg="#4F476D")
        self.result_frame.pack(pady=10)

    def solve(self):

        try:
            exact = float(self.exact_entry.get())
            approx = float(self.approx_entry.get())
        except:
            self.console_callback("Invalid numeric input!")
            return

        log, abs_err, rel_err, percent_err = calculate_errors(exact, approx)

        self.console_callback(log)

        self.show_results(abs_err, rel_err, percent_err)

    def show_results(self, abs_err, rel_err, percent_err):

        for widget in self.result_frame.winfo_children():
            widget.destroy()

        tk.Label(
            self.result_frame,
            text="Error Results",
            bg="#4F476D",
            fg="white",
            font=("Segoe UI", 12, "bold")
        ).pack()

        result_text = (
            f"Absolute Error  : {abs_err:.6f}\n"
            f"Relative Error  : {rel_err:.6f}\n"
            f"Percentage Error: {percent_err:.2f}%"
        )

        tk.Label(
            self.result_frame,
            text=result_text,
            bg="#3A3350",
            fg="white",
            font=("Courier", 12),
            padx=10,
            pady=10,
            justify="left"
        ).pack(pady=10)

    def reset_page(self):

        # clear inputs
        self.exact_entry.delete(0, tk.END)
        self.approx_entry.delete(0, tk.END)

        # clear result display
        for widget in self.result_frame.winfo_children():
            widget.destroy()