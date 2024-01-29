#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#nqueen using BFS
import tkinter as tk
from collections import deque

class NQueensGUI:
    def __init__(self, board_size):
        self.board_size = board_size
        self.solution = None

        self.window = tk.Tk()
        self.window.title("N-Queens BFS")
        
        # Adjust canvas size to fit the board
        canvas_size = board_size * 60
        self.canvas = tk.Canvas(self.window, width=canvas_size, height=canvas_size)
        self.canvas.pack()

    def draw_board(self):
        self.canvas.delete(tk.ALL)
        square_size = self.canvas.winfo_width() // self.board_size  # Calculate square size based on canvas width

        for row in range(self.board_size):
            for col in range(self.board_size):
                color = "black" if (row + col) % 2 == 0 else "gray"
                x0, y0 = col * square_size, row * square_size
                x1, y1 = (col + 1) * square_size, (row + 1) * square_size
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)

        if self.solution is not None:
            for col, row in enumerate(self.solution):
                x = col * square_size + square_size // 2
                y = row * square_size + square_size // 2
                self.canvas.create_text(x, y, text="Q", font=("Arial", 24), fill="lavender")

        self.window.update()

    def solve(self):
        def is_safe(board, row, col):
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

        def bfs_util(board):
            queue = deque([(board, 0)]) #The queue is used to keep track of different configurations of the chessboard.
             # 0 is the starting column
            while queue:
                curr_board, col = queue.popleft()

                if col == self.board_size: # if queens have been placed in all columns
                    self.solution = [0] * self.board_size
                    for i in range(self.board_size):
                        self.solution[i] = curr_board[i].index(1)
                    self.draw_board()
                    return True

                for row in range(self.board_size):
                    if is_safe(curr_board, row, col):
                        new_board = [row_list[:] for row_list in curr_board]
                        new_board[row][col] = 1
                        queue.append((new_board, col + 1))
                        self.draw_board()

            return False
        #backtracking
        board = [[0] * self.board_size for _ in range(self.board_size)] #Initializes the initial chessboard configuration with all values set to 0.
        bfs_util(board)

        if self.solution is None:
            print("No solution exists.")
        else:
            print("Solution found:", self.solution)

        self.window.mainloop()

if __name__ == "__main__":
    size = int(input("Enter the board size: "))
    gui = NQueensGUI(size)
    gui.solve()

