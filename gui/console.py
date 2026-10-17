
import tkinter as tk
class Console(tk.Frame):

    def __init__(self, parent):
        super().__init__(
            parent,
            bg="#2F5D83",
            width=400
        )

        self.pack_propagate(False)

        tk.Label(
            self,
            text="Iteration Console",
            bg="#2F5D83",
            fg="white",
            font=("Segoe UI", 16, "bold")
        ).pack(
            anchor="w",
            padx=15,
            pady=10
        )

        self.text = tk.Text(
            self,
            bg="#111827",
            fg="white",
            font=("Segoe UI", 11, "bold")
        )

        self.text.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )

    def show_log(self, log):
        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, log)
        self.text.see(tk.END)

    # ✅ Add this method to make Console callable
    def __call__(self, message):
        self.show_log(message)