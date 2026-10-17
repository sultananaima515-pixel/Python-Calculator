import tkinter as tk

from methods.gaussian import gaussian_naive


class GaussianPage(tk.Frame):

    def __init__(self, parent, console_callback):
        super().__init__(parent, bg="#3A3350")

        self.console_callback = console_callback
        self.matrix_entries = []

        self.build_ui()

    def build_ui(self):

        self.card = tk.Frame( self, bg="#4F476D", padx=25, pady=25 )
        self.card.pack( padx=30, pady=30, fill="both", expand=True)

        tk.Label(
            self.card,
            text="Gaussian Elimination",
            bg="#4F476D",
            fg="white",
            font=("Segoe UI", 22, "bold")
        ).pack(anchor="w")

        tk.Label(
            self.card,
            text="Number of Equations",
            font=("Segoe UI", 18, "bold"),
            bg="#4F476D",
            fg="white"
        ).pack(anchor="w", pady=(10, 10))

        self.size_entry = tk.Entry(
            self.card,
            font=("Segoe UI", 12),
            width=30,
            bg="#2E3A59",
            fg="white",
            insertbackground="white"
        )
        self.size_entry.pack(pady=5)

        tk.Button(
            self.card,
            text="Create Matrix",
            font=("Segoe UI", 14, "bold"),
            bg="#F76E82",
            fg="white",
            relief="flat",
            command=self.create_matrix
        ).pack(pady=10)

        #matrix area
        self.matrix_frame = tk.Frame(self.card, bg="#4F476D")

        self.matrix_frame.pack(pady=15)


       #Result area
        self.result_frame = tk.Frame(
            self.card,
            bg="#4F476D"
        )

        # self.matrix_frame.pack()

        # self.result_frame = tk.Frame(
        #     self.card,
        #     bg="#4F476D"
        # )

        self.result_frame.pack(
            fill="both",
            expand=True,
            pady=10
        )

        self.result_label = tk.Label(
            self.result_frame,
            text="",
            bg="#3A3350",
            fg="white",
            font=("Courier New", 12, "bold"),
            padx=10,
            pady=10,
            justify="left"
        )
        self.result_label.pack(pady=10)

    def create_matrix(self):

        for widget in self.matrix_frame.winfo_children():
            widget.destroy()

        self.result_label.config(text="")

        self.matrix_entries = []

        try:
            n = int(self.size_entry.get())

            if n <= 0:
                self.console_callback(
                    "Number of equations must be greater than 0."
                )
                return

        except ValueError:
            self.console_callback(
                "Invalid number of equations!"
            )
            return

        for i in range(n):

            row = []

            for j in range(n + 1):

                entry = tk.Entry(
                    self.matrix_frame,
                    width=10,
                    font=("Segoe UI", 12),
                    justify="center",
                    bg="#2E3A59",
                    fg="white",
                    insertbackground="white"
                )

                entry.grid(
                    row=i,
                    column=j,
                    padx=5,
                    pady=5
                )

                row.append(entry)

            self.matrix_entries.append(row)

        tk.Button(
            self.matrix_frame,
            text="Solve",
            font=("Segoe UI", 14, "bold"),
            bg="#FF6B8A",
            fg="white",
            relief="flat",
            command=self.solve
        ).grid(
            row=n,
            column=0,
            columnspan=n + 1,
            pady=10
        )

    def solve(self):

        self.result_label.config(text="")

        matrix = []
        n = len(self.matrix_entries)

        try:

            for i in range(n):

                row = []

                for j in range(n + 1):
                    row.append(
                        float(
                            self.matrix_entries[i][j].get()
                        )
                    )

                matrix.append(row)

        except ValueError:

            self.console_callback(
                "Invalid input detected!"
            )
            return

        log, solution = gaussian_naive(matrix)

        if solution is None:

            self.console_callback(log)
            return

        result_text = "Solution\n\n"

        for i, value in enumerate(solution):
            result_text += (
                f"x{i + 1} = {value:.6f}\n"
            )

        full_output = log +result_text

        self.console_callback(full_output)

        self.result_label.config(
            text=result_text,font=("Segoe UI", 14, "bold"),fg="#F76E82",bg="#2E3A59"
        )

    def reset_page(self):

        self.size_entry.delete(
            0,
            tk.END
        )

        for widget in self.matrix_frame.winfo_children():
            widget.destroy()

        self.matrix_entries.clear()

        self.result_label.config(text="")