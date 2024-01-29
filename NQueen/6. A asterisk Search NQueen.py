#!/usr/bin/env python
# coding: utf-8

# In[7]:


# nqueen using A*
import tkinter as tk
import random

class NQueensGUI:
    def __init__(self, size):
        self.size = size
        self.solutions = []

        self.window = tk.Tk()
        self.window.title("N-Queens UCS")

        self.canvas = tk.Canvas(self.window, width=40 * size, height=40 * size)
        self.canvas.pack()

        self.solve_button = tk.Button(self.window, text="Solve", command=self.solve_a_star)
        self.solve_button.pack()

    def draw_board(self, queens):
        self.canvas.delete(tk.ALL)
        for row in range(self.size):
            for col in range(self.size):
                color = "black" if (row + col) % 2 == 0 else "gray"
                self.canvas.create_rectangle(col * 40, row * 40, (col + 1) * 40, (row + 1) * 40, fill=color)

        for row, col in queens:
            x = (col + 0.5) * 40
            y = (row + 0.5) * 40
            self.canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill="lavender")

    def solve_a_star(self):
        self.solutions = self.solve_nqueens_a_star(self.size)
        if not self.solutions:
            print("No solutions found.")
        else:
            self.draw_board(self.solutions[0])

    def random_heuristic(self):
        # Create a random heuristic for A* search
        return random.randint(0, self.size - 1)

    def conflict(self, queens):
        # Check if there are conflicts between queens
        for i in range(len(queens)):
            for j in range(i + 1, len(queens)):
                if queens[i][1] == queens[j][1] or abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
                    return True
        return False

    def solve_nqueens_a_star(self, size):
        if size < 1:
            return []

        solutions = []
        open_list = [{"queens": [], "cost": 0, "heuristic": self.random_heuristic()}]
        closed_list = set()

        while open_list:
            open_list.sort(key=lambda x: x["cost"] + x["heuristic"])
            current = open_list.pop(0)
            queens, cost, heuristic = current["queens"], current["cost"], current["heuristic"]

            if self.conflict(queens):
                continue

            row = len(queens)

            if row == size:
                solutions.append(queens)
                break

            for col in range(size):
                queen = [row, col]
                new_queens = queens + [queen]
                new_cost = cost + 1
                new_heuristic = self.random_heuristic()
                open_list.append({"queens": new_queens, "cost": new_cost, "heuristic": new_heuristic})

            closed_list.add(str(queens))

        return solutions

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    size = int(input("Enter the board size: "))
    gui = NQueensGUI(size)
    gui.run()


# In[ ]:




