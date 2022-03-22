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
Green_Teams = []
Yellow_Teams = []

def main():

    root = init_window()
    root["background"] = "#bacbf7"
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
    url_input.grid(column=0, columnspan=3, row=0, pady=5)

    team_input = add_team_input(root)
    team_input.grid(row=1, column=0, columnspan=3, pady=5)

    key = add_key_label(root)
    key.grid(column=1, columnspan=3, row=2, pady=5)

    get_matches_button = add_get_matches_button(root, url_input, team_input)
    get_matches_button.grid(column=4, columnspan=2, row=0, pady=5, rowspan=2)

    table = show_matches(root, url_input.get(), team_input.get())
    table.grid(column=0, columnspan=5, row=3, pady=5)




def add_key_label(root):

    key = tk.Text(root, font=("Robot", 13), width=70, height=3)
    
    key.tag_configure('green', background='lime green')
    key.tag_configure('yellow', background='yellow')
    key.tag_configure('blue', background='cyan')

    key.insert(tk.END, "Green", 'green')
    key.insert(tk.END,
    ' is yourself\n')
    key.insert(tk.END, 'Blue', 'blue')
    key.insert(tk.END, ' is a team you will be allied with at some point\n')
    key.insert(tk.END, 'Yellow', 'yellow') 
    key.insert(tk.END, ' is one of the opposing teams (of one of your matches)')
    

    return key

# add a input for a url in the center top of the window

def add_url_input(root):

    url_input = tk.Entry(root, width=60, justify="center", font=("Robot", 14))

    # url_input.grid(row=0, column=0, columnspan=2)

    url_input.insert(0,

                     URL)

    return url_input

def add_team_input(root):
    team_input = tk.Entry(root, width=60, justify="center", font=("Robot", 14))
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

    matches = opponent_matches.get_important_matches(all_matches, team_input, bool(ALLIANCEOROPPONENT))
    return matches


def get_all_matches(url_input):

    return getmatches.get_matches(url_input)


# table full of matches using the functions ^---

def show_matches(root, url_input, team_input):
    all_matches = get_all_matches(url_input)
    green_teams = [TEAM]
    yellow_teams = get_yellow_teams(all_matches, team_input)
    blue_teams = get_blue_teams(all_matches, team_input)

    textbox = tk.Text(root, width=70, height=20, font=("Robot", 14))
    add_text_to_table(textbox, all_matches, green_teams, yellow_teams, blue_teams)
    # add a scrollbar
    scrollbar = tk.Scrollbar(root, command=textbox.yview)
    scrollbar.grid(row=3, column=5, sticky='nsew')
    textbox['yscrollcommand'] = scrollbar.set
    return textbox


def add_text_to_table(textbox, all_matches, green_teams, yellow_teams, blue_teams):
    textbox.tag_configure('green', background='lime green')
    textbox.tag_configure('yellow', background='yellow')
    textbox.tag_configure('blue', background='cyan')


    for i in range(len(all_matches)):
        for j in [0, 1, 2, 3, 4]:
            string = str(all_matches[i][j])
            # don't include the '\t' in the conditions
            if string in green_teams:
                textbox.insert(tk.END, string, 'green')
            elif string in yellow_teams and not(string in blue_teams):
                textbox.insert(tk.END, string, 'yellow')
            elif string in blue_teams and not(string in yellow_teams):
                textbox.insert(tk.END, string, 'blue')
            elif string in blue_teams and string in yellow_teams:
                textbox.insert(tk.END, string, 'blue')
            else:
                textbox.insert(tk.END, string)
            textbox.insert(tk.END, '\t')
            # check to see if row number is in important matches
        textbox.insert(tk.END, '\n')
# actually begin the window
def get_yellow_teams(all_matches, team_input):
    return opponent_matches.get_yellow_teams(all_matches, team_input)
def get_blue_teams(all_matches, team_input):
    return opponent_matches.get_blue_teams(all_matches, team_input)
if __name__ == '__main__':
    main()
