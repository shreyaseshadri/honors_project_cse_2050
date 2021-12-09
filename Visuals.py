import tkinter as tk
from tkinter import messagebox
from RunGame import RunGame as rg


#create the window and title it
window = tk.Tk()
window.title("Are You The One?")

#create a frame for contestants and instructions
frm_contestants = tk.Frame(
    master = window, 
    relief = tk.RAISED, 
    borderwidth = 5, 
    bg = "#650D78"
)
game = rg()
frm_contestants.pack(fill = tk.BOTH, side = tk.TOP, expand = True)
lbl_meet_contestants = tk.Label(
    master = frm_contestants,
    text = 'Meet the contestants!', 
    font = ("Tahoma", 20), 
    bg = "#650D78", 
    fg = "white"
)
lbl_contestants = tk.Label(
    master = frm_contestants,
    text = '\n {}'.format(game.start_game()), 
    font = ("Harrington", 16, "bold"), 
    bg = "#650D78", 
    fg = "white"
)
lbl_meet_contestants.pack()
lbl_contestants.pack(padx = 2, pady = 2)
lbl_instructions = tk.Label(
    master = frm_contestants, 
    text = 'Use the box below to guess the matches!',
    font = ("Tahoma ", 20), 
    bg = "#650D78", 
    fg = "white"
)
lbl_instructions.pack(padx = 2, pady = 2)

#create a frame for guesses, with 16 entry slots for 8 pairs
frm_guesses = tk.Frame(
    master = window, 
    relief = tk.SUNKEN, 
    borderwidth = 2, 
    bg = "#650D78"
)
frm_guesses.pack(fill = tk.BOTH, side = tk.TOP, expand = True)
txt_guesses = tk.Text(
    master = frm_guesses, 
    height = 10, 
    width = 75
)
lbl_guesses_instructions = tk.Label(
    master = frm_guesses, 
    text = "\nNow, let's guess the pairs!\nEnter your guess by pair, each seperated by a comma (eg: Alice Bob, Cathryn David)\n", 
    font = ("Tahoma", 20),
    bg = "#650D78", 
    fg = "white"
)
frm_guesses.pack(fill = tk.BOTH, side = tk.TOP, expand = True)
lbl_guesses_instructions.pack(padx = 5, pady = 5)
txt_guesses.pack()

#create button and a frame below to get data from text box and test it 
frm_buttons = tk.Frame(
    master = window, 
    relief = tk.RAISED, 
    borderwidth = 5, 
    bg = "#650D78"
)

def check_guess():
    #clear the text box for a potential new answer
    user_guess = txt_guesses.get(1.0, tk.END)
    txt_guesses.delete(1.0, tk.END)
    #run the check to see how many they got right
    count_correct, result = game.continue_game(user_guess) 
    #if they win, create pop up to say they won
    if result == True: 
        messagebox.showinfo(
            title = "You Won!", 
            message = "Congratulations! You've matched the contestents successfully! To play again, please reload the program!"
        )
    #if they lose, display number of matches they got right
    else:
        messagebox.showinfo(
            title = "Keep Trying!", 
            message = "Results:\n You guessed {} pairs correctly. Re-enter your guesses and click the button to try again!".format(count_correct)
            )

btn_continue = tk.Button(
    master = frm_buttons, 
    text = "Check Guess!", 
    width = 40, 
    height = 5,
    border = 10,
    bg = '#09F4A8', 
    fg = 'black',
    font = ("Tahoma", 14, "bold"),
    command = check_guess
)

def show_answers(): 
    messagebox.showinfo(
        title = "Answers!", 
        message = "Drumroll please! The matches are ...\n{}".format(game._game._pairs)
    )

btn_show_answers = tk.Button(
    master = frm_buttons, 
    text = "Show Answers!", 
    width = 40, 
    height = 4, 
    border = 5,
    bg = '#09F4A8', 
    fg = 'black',
    font = ("Tahoma", 14, "bold"),
    command = show_answers
)
    

frm_buttons.pack(fill = tk.BOTH, side = tk.TOP, expand = True)
btn_continue.pack(padx = 5, pady = 5)
btn_show_answers.pack(padx = 5, pady = 5)


window.mainloop()