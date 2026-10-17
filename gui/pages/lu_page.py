import tkinter as tk
from methods.lu import lu_decomposition


class LUPage(tk.Frame):

    def __init__(self, parent, console_callback):
        super().__init__(parent, bg="#3A3350")

        self.console_callback = console_callback
        self.matrix_entries = []

        self.build_ui()

    def build_ui(self):

        self.card = tk.Frame(
            self,
            bg="#4F476D",
            padx=25,
            pady=25
        )
        self.card.pack(
            padx=25,
            pady=25,
            fill="both",
            expand=True
        )

        tk.Label(
            self.card,
            text="LU Decomposition",
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
            width=30
        )
        self.size_entry.pack(pady=5)

        tk.Button(
            self.card,
            text="Create Matrix",
            bg="#F76E82",
            fg="white",
            relief="flat",
            font=("Segoe UI", 11, "bold"),
            command=self.create_matrix
        ).pack(pady=10)

        self.matrix_frame = tk.Frame(
            self.card,
            bg="#4F476D"
        )
        self.matrix_frame.pack()

        self.result_frame = tk.Frame(
            self.card,
            bg="#4F476D"
        )
        self.result_frame.pack(
            fill="both",
            expand=True,
            pady=10
        )

    def create_matrix(self):

        for widget in self.matrix_frame.winfo_children():
            widget.destroy()

        for widget in self.result_frame.winfo_children():
            widget.destroy()

        self.matrix_entries = []

        try:
            n = int(self.size_entry.get())

            if n <= 0:
                self.console_callback(
                    "Matrix size must be greater than 0."
                )
                return

        except ValueError:
            self.console_callback(
                "Invalid matrix size!"
            )
            return

        for i in range(n):

            row = []

            for j in range(n + 1):

                entry = tk.Entry(
                    self.matrix_frame,
                    width=10,
                    font=("Segoe UI", 12, "bold"),
                    justify="center"
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
            bg="#FF6B8A",
            fg="white",
            relief="flat",
            font=("Segoe UI", 14, "bold"),
            command=self.solve
        ).grid(
            row=n,
            column=0,
            columnspan=n + 1,
            pady=10
        )

    def solve(self):

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

        log, L, U, solution = lu_decomposition(matrix)

        if solution is None:

            self.console_callback(log)
            return

        self.console_callback(log)

        self.show_results(
            L,
            U,
            solution
        )

    def show_results(self, L, U, solution):

        for widget in self.result_frame.winfo_children():
            widget.destroy()

        def matrix_to_string(matrix):

            text = ""

            for row in matrix:

                text += " ".join(
                    f"{value:10.4f}"
                    for value in row
                )

                text += "\n"

            return text

        # # L Matrix Title
        # tk.Label(
        #     self.result_frame,
        #     text="L Matrix",
        #     bg="#4F476D",
        #     fg="white",
        #     font=("Segoe UI", 14, "bold")
        # ).pack()

        # # L Matrix Data
        # tk.Label(
        #     self.result_frame,
        #     text=matrix_to_string(L),
        #     bg="#3A3350",
        #     fg="white",
        #     font=("Courier New", 11),
        #     justify="left",
        #     padx=10,
        #     pady=10
        # ).pack(pady=5)

        # # U Matrix Title
        # tk.Label(
        #     self.result_frame,
        #     text="U Matrix",
        #     bg="#4F476D",
        #     fg="white",
        #     font=("Segoe UI", 14, "bold")
        # ).pack()

        # # U Matrix Data
        # tk.Label(
        #     self.result_frame,
        #     text=matrix_to_string(U),
        #     bg="#3A3350",
        #     fg="white",
        #     font=("Courier New", 11),
        #     justify="left",
        #     padx=10,
        #     pady=10
        # ).pack(pady=5)

        result_text = "Solution\n\n"

        for i, value in enumerate(solution):
            result_text += (
                f"x{i + 1} = {value:.6f}\n"
            )

        tk.Label(
            self.result_frame,
            text=result_text,
            bg="#3A3350",
            fg="white",
            font=("Courier New", 12, "bold"),
            padx=10,
            pady=10
        ).pack(pady=10)

    def reset_page(self):

        self.size_entry.delete(0, tk.END)

        for widget in self.matrix_frame.winfo_children():
            widget.destroy()

        for widget in self.result_frame.winfo_children():
            widget.destroy()

        self.matrix_entries.clear()