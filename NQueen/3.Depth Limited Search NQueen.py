#!/usr/bin/env python
# coding: utf-8

# In[2]:


#nqueen using DLS
import tkinter as tk

class NQueensGame:
    def __init__(self, board_size):
        self.board_size = board_size
        self.solution = []

    def solve(self):
        self.solution = []
        for depth in range(self.board_size + 1):
            board = [[0] * self.board_size for _ in range(self.board_size)]
            if self._solve_recursive(board, 0, depth):
                return True
        return False

    def _solve_recursive(self, board, col, max_depth):
        if col == self.board_size:
            self.solution = [row[:] for row in board]
            return True

        if max_depth == 0:
            return False

        for row in range(self.board_size):
            if self.is_safe(board, row, col):
                board[row][col] = 1
                if self._solve_recursive(board, col + 1, max_depth - 1):
                    return True
                board[row][col] = 0

        return False

    def is_safe(self, board, row, col):
        for i in range(col):
            if board[row][i] == 1:
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        for i, j in zip(range(row, self.board_size), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        return True

class NQueensGUI:
    def __init__(self, root, game):
        self.root = root
        self.game = game
        self.canvas_size = 600
        self.square_size = self.canvas_size // game.board_size

        self.canvas = tk.Canvas(root, width=self.canvas_size, height=self.canvas_size)
        self.canvas.pack()

        self.solve_button = tk.Button(root, text="Solve", command=self.solve)
        self.solve_button.pack()

    # rest of the class remains the same


    def draw_board(self):
        self.canvas.delete("all")
        for row in range(self.game.board_size):
            for col in range(self.game.board_size):
                x1 = col * self.square_size
                y1 = row * self.square_size
                x2 = x1 + self.square_size
                y2 = y1 + self.square_size

                color = "black" if (row + col) % 2 == 0 else "gray"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

        for row in range(self.game.board_size):
            for col in range(self.game.board_size):
                if self.game.solution and self.game.solution[row][col] == 1:
                    x = (col + 0.5) * self.square_size
                    y = (row + 0.5) * self.square_size
                    self.canvas.create_oval(x - self.square_size * 0.3, y - self.square_size * 0.3, x + self.square_size * 0.3, y + self.square_size * 0.3, fill="lavender")


    def solve(self):
        self.game.solve()
        self.draw_board()

if __name__ == "__main__":
    board_size = 6  # Change the board size as desired

    game = NQueensGame(board_size)

    root = tk.Tk()
    root.title("N-Queens DLS")

    gui = NQueensGUI(root, game)

    gui.draw_board()

    root.mainloop()


# In[ ]:





# In[ ]:




