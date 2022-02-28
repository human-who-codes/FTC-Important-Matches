# create a GUI for the matchmaker

# Use opponent_matches.py to get the opponent matches

# Use user input to create the matchesabs


import tkinter as tk

from tkinter import ttk

from tkinter import messagebox

from tkinter import filedialog
import opponent_matches
import getmatches


URL = "http://ftc-events.firstinspires.org/2021/USIACMPBLA/qualifications"
TEAM = "8672"

def main():

    root = init_window()
    add_components(root)

    root.mainloop()


# init main window

def init_window():

    root = tk.Tk()

    root.title('Matchmaker')

    root.geometry('800x800')

    root.columnconfigure(0, weight=100)

    root.columnconfigure(1, weight=100)

    root.columnconfigure(2, weight=100)

    root.columnconfigure(3, weight=100)

    root.columnconfigure(4, weight=100)

    root.columnconfigure(5, weight=10)

    # set the root's internal padding

    root['padx'] = 20

    return root


def add_components(root):
    url_input = add_url_input(root)

    team_input = add_team_input(root)

    get_matches_button = add_get_matches_button(root, url_input, team_input)

    get_matches_button.grid(column=4, columnspan=2, row=0, pady=5)

    url_input.grid(column=0, columnspan=3, row=0, pady=5)

    table = show_matches(root, url_input.get(), team_input.get())

    table.grid(column=0, columnspan=5, row=2, pady=5)


# add a input for a url in the center top of the window

def add_url_input(root):

    url_input = tk.Entry(root, width=60, justify="center", font=("Robot", 14))

    # url_input.grid(row=0, column=0, columnspan=2)

    url_input.insert(0,

                     URL)
    print(URL)

    return url_input

def add_team_input(root):
    team_input = tk.Entry(root, width=60, justify="center", font=("Robot", 14))
    team_input.grid(row=1, column=0, columnspan=2)
    team_input.insert(0,TEAM)
    return team_input

# add a button to get the matches

def add_get_matches_button(root, url_input, team_input):

    get_matches_button = tk.Button(root, text='Enter', command=lambda: refresh(root, url_input, team_input),
                                   font=("Robot", 15))

    # get_matches_button.grid(row=1, column=2)

    return get_matches_button


# refresh table
def refresh(root, url_input_box, team_input):
    global URL
    global TEAM
    url_input = url_input_box.get()
    team = team_input.get()
    for child in root.winfo_children():
        child.destroy()
    URL = url_input
    TEAM = team
    add_components(root)
# interact with other files' functions


def get_important_matches(root, url_input, team_input):
    all_matches = get_all_matches(url_input)

    matches = opponent_matches.get_important_matches(all_matches, team_input)
    return matches


def get_all_matches(url_input):

    return getmatches.get_matches(url_input)


# table full of matches using the functions ^---

def show_matches(root, url_input, team_input):
    all_matches = get_all_matches(url_input)
    important_matches = get_important_matches(root, url_input, team_input)
    textbox = tk.Text(root, width=70, height=20, font=("Robot", 14))
    add_text_to_table(textbox, all_matches, important_matches)
    # add a scrollbar
    scrollbar = tk.Scrollbar(root, command=textbox.yview)
    scrollbar.grid(row=2, column=5, sticky='nsew')
    textbox['yscrollcommand'] = scrollbar.set
    return textbox


def add_text_to_table(textbox, all_matches, important_matches):
    textbox.tag_configure('highlight', background='yellow')
    for i in range(len(all_matches)):
        for j in [0, 1, 2, 3, 4]:
            string = str(all_matches[i][j]) + '\t'
            if j == 4:
                string += "\n"
            if i + 1 in important_matches:
                # add tag to this line
                textbox.insert(tk.END, string, 'highlight')
            else:
                textbox.insert(tk.END, string)
            # check to see if row number is in important matches

# actually begin the window


if __name__ == '__main__':
    main()
