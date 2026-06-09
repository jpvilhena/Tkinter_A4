import tkinter as tk
from tkinter import ttk, messagebox

from display import DataFrameViewer
from functions import QUERY_OPTIONS, run_query, close_database


class QueryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SQL Query Explorer")
        self.root.geometry("1000x600")
        self.root.minsize(800, 500)

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.main_frame = ttk.Frame(self.root)
        self.main_frame.grid(sticky="nsew")
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

        self.query_option = tk.StringVar()
        self.viewer = None
        self.back_button = None

        self.card = None
        self.button_frame = None

        self.build_query_panel()
        self.show_query_panel()

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def build_query_panel(self):
        self.card = ttk.Frame(self.main_frame, padding=20, relief="ridge", borderwidth=2)
        self.card.place(relx=0.5, rely=0.35, anchor="center", width=760, height=220)

        title = ttk.Label(self.card, text="SQL Query Options", font=("Segoe UI", 14, "bold"))
        title.pack(pady=(0, 10))

        selector_label = ttk.Label(self.card, text="Choose a saved query:")
        selector_label.pack(anchor="w")

        self.query_combo = ttk.Combobox(
            self.card,
            textvariable=self.query_option,
            values=list(QUERY_OPTIONS.keys()),
            state="readonly",
            width=74,
        )
        self.query_combo.pack(fill="x", pady=6)

        if QUERY_OPTIONS:
            self.query_combo.current(0)

        self.message_label = ttk.Label(self.card, text="", foreground="red")
        self.message_label.pack(anchor="w", pady=(6, 0))

        self.note_label = ttk.Label(
            self.card,
            text="When you run a query, this area will become the results viewer.",
            foreground="#555",
        )
        self.note_label.pack(anchor="w", pady=(10, 0))

        self.button_frame = ttk.Frame(self.main_frame)
        self.button_frame.place(relx=0.5, rely=0.78, anchor="center")

        run_button = ttk.Button(self.button_frame, text="Run Query", command=self.on_run_query)
        run_button.grid(row=0, column=0, padx=10)

        back_button = ttk.Button(
            self.button_frame,
            text="Back to Main Menu",
            command=self.show_query_panel,
        )
        back_button.grid(row=0, column=1, padx=10)

    def show_query_panel(self):
        self.clear_viewer()
        self.hide_back_button()
        self.clear_message()

        if self.card:
            self.card.place(relx=0.5, rely=0.35, anchor="center", width=760, height=220)
        if self.button_frame:
            self.button_frame.place(relx=0.5, rely=0.78, anchor="center")

    def on_run_query(self):
        query_name = self.query_option.get()
        if not query_name:
            self.message_label.configure(text="Please select a query first.")
            return

        sql = QUERY_OPTIONS.get(query_name)
        if not sql:
            self.message_label.configure(text="Selected query is not available.")
            return

        try:
            df = run_query(sql)
        except Exception as exc:
            messagebox.showerror("Query Error", f"Error while running query:\n{exc}")
            return

        self.show_dataframe(df)

    def show_dataframe(self, df):
        self.clear_message()
        self.card.place_forget()
        self.button_frame.place_forget()
        self.hide_back_button()

        if self.viewer:
            self.viewer.frame.destroy()

        self.viewer = DataFrameViewer(self.main_frame)
        self.viewer.display_dataframe(df)

        self.back_button = ttk.Button(
            self.main_frame,
            text="Back to Query Selection",
            command=self.show_query_panel,
        )
        self.back_button.pack(pady=10)

    def clear_viewer(self):
        if self.viewer:
            self.viewer.frame.destroy()
            self.viewer = None

    def hide_back_button(self):
        if self.back_button:
            self.back_button.destroy()
            self.back_button = None

    def clear_message(self):
        if self.message_label:
            self.message_label.configure(text="")

    def on_close(self):
        close_database()
        self.root.destroy()


def main():
    root = tk.Tk()
    app = QueryApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()