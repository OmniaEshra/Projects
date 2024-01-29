#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter
from tkinter import messagebox
from tkinter import * # to call all modules of tkinter
window = Tk() # class that makes object
window.title("Tic Tac Toe")
window.geometry('245x259+500+200') # to change size and location(widthxheight+left+top)
window.resizable(True,True) # to fix the size(width,height)
board = [[' ' for _ in range(3)] for _ in range(3)]
current_player = 'X' # to keep track of the current player
def handle_click(row, col):
    global current_player
    if board[row][col] == ' ':  # Check if the clicked cell is empty
        # Update the cell with the current player's symbol
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)

        # Check for a win
        if check_win(current_player):
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_game()
        elif check_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
        else:
            # Switch to the next player
            current_player = 'O' if current_player == 'X' else 'X'

# Function to check for a win
def check_win(player):
    # Check rows
    for row in board:
        if row.count(player) == 3:
            return True

    # Check columns
    for col in range(3):
        if [board[row][col] for row in range(3)].count(player) == 3:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# Function to check for a draw
def check_draw():
    for row in board:
        if ' ' in row:
            return False
    return True

# Function to reset the game
def reset_game():
    global current_player, buttons, board

    # Reset the current player
    current_player = 'X'

    # Clear the board
    board = [[' ' for _ in range(3)] for _ in range(3)]

    # Clear the button texts
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text=' ')

# Create the buttons
buttons = [[None for _ in range(3)] for _ in range(3)]
for row in range(3):
    for col in range(3):
        buttons[row][col] = Button(window, text=' ', width=10, height=5,
                                     command=lambda r=row, c=col: handle_click(r, c))
        buttons[row][col].grid(row=row, column=col)

# Run the main loop
window.mainloop()


# In[ ]:





# In[ ]:




