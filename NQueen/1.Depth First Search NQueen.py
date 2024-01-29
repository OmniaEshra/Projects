#!/usr/bin/env python
# coding: utf-8

# In[1]:llll


#nqueen using DFS algorithm
import tkinter as tk

class NQueensGUI:
    def __init__(self, board_size):
        self.board_size = board_size
        self.solution = None  # used to store the solution

        self.window = tk.Tk()
        self.window.title("N-Queens DFS")
        self.canvas = tk.Canvas(self.window, width=40 * board_size, height=40 * board_size)
        self.canvas.pack()

    def draw_board(self):
        self.canvas.delete(tk.ALL)
        for row in range(self.board_size):
            for col in range(self.board_size):
                color = "black" if (row + col) % 2 == 0 else "gray"
                self.canvas.create_rectangle(col * 40, row * 40, (col + 1) * 40, (row + 1) * 40, fill=color)

        if self.solution is not None:  #draw queens when solution is found
            for col, row in enumerate(self.solution):
                self.canvas.create_text(col * 40 + 20, row * 40 + 20, text="Q", font=("italic", 20), fill="lavender")

        self.window.update()

    def is_safe(self, board, row, col):
        for i in range(col):
            if board[row][i] == 1:
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        for i, j in zip(range(row, self.board_size, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        return True

    def solve(self): #DFS function
        board = [[0] * self.board_size for _ in range(self.board_size)] # make 2D list with values=0

        def place_queens(board, col):
            if col == self.board_size: #if we placed queens in all coumns then the solution has been found
                return True

            for i in range(self.board_size):
                if self.is_safe(board, i, col):
                    board[i][col] = 1
                    if place_queens(board, col + 1):
                        return True
                    board[i][col] = 0 #backtracking 

            return False

        if not place_queens(board, 0): #to find a solution start from the first column.
            print("No solution exists.")
        else: #print index of queens
            self.solution = [board[i].index(1) for i in range(self.board_size)]
            print("Solution found:", self.solution)

        self.draw_board()
        self.window.mainloop()

if __name__ == "__main__":
    size = int(input("Enter the board size: "))
    gui = NQueensGUI(size)
    gui.solve()


# In[ ]:




