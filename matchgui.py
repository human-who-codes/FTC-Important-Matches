# create a GUI for the matchmaker
# Use opponent_matches.py to get the opponent matches
# Use user input to create the matchesabs

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import opponent_matches
import getmatches








def main():
    root = init_window()
    add_components(root)
    root.mainloop()


# init main window
def init_window():
    root = tk.Tk()
    root.title('Matchmaker')
    root.geometry('800x800')
    return root

def add_components(root):
    url_input = add_url_input(root)
    get_matches_button = add_get_matches_button(root, url_input.get())

    get_matches_button.pack(side="top")
    url_input.pack(pady=10)

# add a input for a url in the center top of the window
# large font
def add_url_input(root):
    url_input = tk.Entry(root, width=50, justify="center", font=("Robot", 14))
    # url_input.grid(row=0, column=0, columnspan=2)
    url_input.insert(0, 
    'ftc-events.firstinspires.org/2021/USIACMPBLA/qualifications')
    # check if url has http://
    if 'http://' not in url_input.get():
        url_input.insert(0, 'http://')
    return url_input

# add a button to get the matches
def add_get_matches_button(root, url_input):
    get_matches_button = tk.Button(root, text='Get Matches', command=lambda: get_matches(url_input),
                    font=("Robot", 15))
    # get_matches_button.grid(row=1, column=2)
    return get_matches_button

def get_matches(url_input):
    all_matches = getmatches.get_matches(url_input)
    matches = opponent_matches.get_important_matches(all_matches, team='8672')
    print(matches)
    
main()


