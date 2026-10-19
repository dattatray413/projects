#tick tack toe game
import tkinter as tk
from tkinter import messagebox

#creating a game window
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("420x700")
root.resizable(False, False)

# colors
BG_COLOR = "#151522"
PANEL_COLOR = "#222235"
X_COLOR = "#00D9FF" 
O_COLOR = "#B388FF" 
TEXT_COLOR = "#FFFFFF" 
MUTED_COLOR = "#A0A0B8"
root.configure(bg=BG_COLOR)

title_lable = tk.Label(
    root,
    text= "Tic-Tac-Toe",
    font=("Arial",24,"bold"),
    bg= BG_COLOR,
    fg= TEXT_COLOR
)
title_lable.pack(pady=(25, 10))

turn_label = tk.Label( 
    root, 
    text="PLAYER X'S TURN", 
    font=("Arial", 12, "bold"), 
    bg=BG_COLOR, 
    fg=X_COLOR 
) 
turn_label.pack(pady=10)

score_frame = tk.Frame(
    root, 
    bg=BG_COLOR 
) 
score_frame.pack(pady=15)

x_frame = tk.Frame(
    score_frame, 
    bg=PANEL_COLOR, 
    width=150, 
    height=75 
)
x_frame.pack(side="left", padx=8)
x_frame.pack_propagate(False)

x_title = tk.Label( 
    x_frame, 
    text="PLAYER X", 
    font=("Arial", 10, "bold"), 
    bg=PANEL_COLOR, 
    fg=X_COLOR 
)
x_title.pack(pady=(10, 0))

x_score = tk.Label( 
    x_frame, 
    text="0",
    font=("Arial", 18, "bold"), 
    bg=PANEL_COLOR, 
    fg=TEXT_COLOR 
)
x_score.pack()

# Player O score panel 
o_frame = tk.Frame(
    score_frame, 
    bg=PANEL_COLOR, 
    width=150, 
    height=75
)
o_frame.pack(side="left", padx=8)
o_frame.pack_propagate(False)

o_title = tk.Label(
    o_frame, 
    text="PLAYER O",
    font=("Arial", 10, "bold"),
    bg=PANEL_COLOR,
    fg=O_COLOR 
)
o_title.pack(pady=(10, 0))

o_score = tk.Label(
    o_frame,
    text="0", 
    font=("Arial", 18, "bold"),
    bg=PANEL_COLOR,
    fg=TEXT_COLOR
) 
o_score.pack()

# GAME VARIABLES 

current_player = "X"
board = [""] * 9

buttons = []
score_x = 0
score_o = 0

winning_combinations = [(0, 1, 2),(3, 4, 5),(6, 7, 8),(0, 3, 6),
                    (1, 4, 7),(2, 5, 8),(0, 4, 8),(2, 4, 6)]

# check winner

def check_winner():

    for combination in winning_combinations:

        a, b, c = combination

        if (
            board[a] != ""
            and board[a] == board[b]
            and board[b] == board[c]
        ):
            return board[a], combination

    return None, None

# Click funtion 

def button_click(index):

    global current_player

    # Ignore clicks if its occupied
    if board[index] != "":
        return

    # current player's symbol
    board[index] = current_player

    # show which button has been clicked
    buttons[index].config(
        text=current_player,
        fg=X_COLOR if current_player == "X" else O_COLOR
    )
    
        # Check for a winner
    winner, winning_cells = check_winner()

    if winner:

        global score_x, score_o

        if winner == "X":
            score_x += 1
            x_score.config(text=str(score_x))
        else:
            score_o += 1
            o_score.config(text=str(score_o))

        turn_label.config(
            text=f"PLAYER {winner} WINS!",
            fg=X_COLOR if winner == "X" else O_COLOR
        )
        
        # Highlight winning cells
        for index in winning_cells:
            buttons[index].config(
                bg="#238636",
                disabledforeground=X_COLOR if winner == "X" else O_COLOR
            )

        for button in buttons:
            button.config(state="disabled")
            
        # Show popup message
        messagebox.showinfo(
            "Game Over",
            f"Player {winner} wins! 🎉"
        )
        return


    # Check for a draw
    if "" not in board:

        turn_label.config(
            text="IT'S A DRAW!",
            fg=TEXT_COLOR
        )

        # Stop further moves
        for button in buttons:
            button.config(state="disabled")
            
        messagebox.showinfo(
            "Game Over",
            "It's a draw! 🤝"
        )

        return

    # Switch players
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

    # changing the label
    turn_label.config(
        text=f"PLAYER {current_player}'S TURN",
        fg=X_COLOR if current_player == "X" else O_COLOR
    )

# ---------------- RESTART GAME ----------------

def restart_game():

    global current_player, board

    # Reset the current player
    current_player = "X"

    # Clear the board data
    board = [""] * 9

    # Reset all nine buttons
    for button in buttons:
        button.config(
            text="",
            state="normal",
            bg=PANEL_COLOR,
            fg=TEXT_COLOR
        )

    # Update the turn indicator
    turn_label.config(
        text="PLAYER X'S TURN",
        fg=X_COLOR
    )

# Game board

board_frame = tk.Frame(
    root,
    bg= BG_COLOR
)
board_frame.pack(pady=15)

# Creating 9 buttons
for row in range(3):
    for col in range(3):
        index = row * 3 + col
        button = tk.Button(
            board_frame,
            text="",
            font=("Arial", 28, "bold"),
            width=3, 
            height=1, 
            bg=PANEL_COLOR, 
            fg=TEXT_COLOR,
            activebackground="#34344F", 
            activeforeground=TEXT_COLOR,
            relief="flat",
            cursor="hand2",
            command=lambda i=index: button_click(i)
        )

        button.grid(
            row=row,
            column=col,
            padx=4,
            pady=4
        )
        buttons.append(button)
        
        # ---------------- RESTART BUTTON ----------------

restart_button = tk.Button(
     root,
    text="RESTART GAME",
    font=("Arial", 11, "bold"),
    bg="#34344F",
    fg=TEXT_COLOR,
    activebackground="#454568",
    activeforeground=TEXT_COLOR,
    relief="flat",
    cursor="hand2",
    command=restart_game
)
restart_button.pack(pady=15)
    




root.mainloop()

