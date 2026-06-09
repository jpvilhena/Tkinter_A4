"""Display helper for showing pandas DataFrames in a Tkinter Treeview."""

import pandas as pd
import tkinter as tk
from tkinter import ttk

class DataFrameViewer:
    """Wraps a Treeview widget to show a DataFrame in a grid-like table."""
    def __init__(self, root):
        """Prepare the frame container used to display the DataFrame."""
        self.root = root
        # self.root.title("DataFrame Viewer")

        self.frame = ttk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.tree = None

    def display_dataframe(self, df):
        # Clear previous tree if exists
        if self.tree:
            self.tree.destroy()

        self.tree = ttk.Treeview(self.frame)

        # Define columns
        self.tree["columns"] = list(df.columns)
        self.tree["show"] = "headings"

        # Create headings
        for col in df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")

        # Insert rows
        for _, row in df.iterrows():
            self.tree.insert("", "end", values=list(row))

        # Add scrollbars
        scrollbar_y = ttk.Scrollbar(self.frame, orient="vertical", command=self.tree.yview)
        scrollbar_x = ttk.Scrollbar(self.frame, orient="horizontal", command=self.tree.xview)

        self.tree.configure(yscroll=scrollbar_y.set, xscroll=scrollbar_x.set)

        self.tree.grid(row=0, column=0, sticky="nsew")
        scrollbar_y.grid(row=0, column=1, sticky="ns")
        scrollbar_x.grid(row=1, column=0, sticky="ew")

        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)