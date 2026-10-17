
import tkinter as tk

from gui.header import Header
from gui.sidebar import Sidebar
from gui.console import Console

from gui.pages.gaussian_page import GaussianPage
from gui.pages.pivoting_page import PivotingPage
from gui.pages.lu_page import LUPage
from gui.pages.simpson13_page import Simpson13Page
from gui.pages.simpson38_page import Simpson38Page
from gui.pages.euler_page import EulerPage
from gui.pages.error_page import ErrorPage


class Dashboard(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent, bg="#2E3A59")

        self.pack(fill="both", expand=True)

        self.current_page = "gaussian"

        self.create_layout()

    def show_page(self, page_name):

        if page_name not in self.pages:
            return

        self.current_page = page_name

        for page in self.pages.values():
            page.pack_forget()

        self.pages[page_name].pack(
            fill="both",
            expand=True
        )

    def reset_all(self):

        self.console.show_log("")

        page = self.pages[self.current_page]

        if hasattr(page, "reset_page"):
            page.reset_page()

    def clear_console(self):

        self.console.show_log("")

    def create_layout(self):

        self.header = Header(
            self,
            self.reset_all,
            self.clear_console
        )

        self.header.pack(fill="x")

        body = tk.Frame(self, bg="#2E3A59")
        body.pack(fill="both", expand=True)

        self.sidebar = Sidebar(
            body,
            self.show_page
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        self.workspace = tk.Frame(
            body,
            bg="#6D5478"
        )

        self.workspace.pack(
            side="left",
            fill="both",
            expand=True
        )

        self.console = Console(body)

        self.console.pack(
            side="right",
            fill="y"
        )

        self.pages = {}

        self.pages["gaussian"] = GaussianPage(
            self.workspace,
            self.console.show_log
        )

        self.pages["pivoting"] = PivotingPage(
            self.workspace,
            self.console.show_log
        )

        self.pages["lu"] = LUPage(
            self.workspace,
            self.console.show_log
        )

        self.pages["simpson13"] = Simpson13Page(
            self.workspace,
            self.console.show_log
        )

        self.pages["simpson38"] = Simpson38Page(
            self.workspace,
            self.console.show_log
        )

        self.pages["euler"] = EulerPage(
            self.workspace,
            self.console.show_log
        )

        self.pages["error"] = ErrorPage(
            self.workspace,
            self.console.show_log
        )

        self.show_page("gaussian")