# create a GUI for the matchmaker
# Use opponent_matches.py to get the opponent matches
# Use user input to create the matchesabs

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog







def main():
    root = init_window()
    root.mainloop()


# init main window
def init_window():
    root = tk.Tk()
    root.title('Matchmaker')
    root.geometry('800x800')
    return root


