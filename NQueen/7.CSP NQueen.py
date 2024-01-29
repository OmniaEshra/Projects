#!/usr/bin/env python
# coding: utf-8

# In[1]:


# nqueen using backtracking and forward checking
class NQueensCSP:
    def __init__(self, size):
        self.size = size
        self.variables = list(range(size)) #columns and domain is row
        self.domains = self.initialize_domains() # contain all possible values

    def initialize_domains(self):
        return [list(range(self.size)) for _ in range(self.size)]

    def solve_csp(self):
        return self.backtrack({})

    def backtrack(self, assignment):
        if len(assignment) == self.size:
            return [list(assignment.values())]

        var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var):
            if self.is_safe(assignment, var, value):
                assignment[var] = value
                updated_domains = self.forward_check(assignment, var, value)
                if updated_domains is not None:
                    result = self.backtrack(assignment)
                    if result:
                        return result
                del assignment[var]
        return []

    def select_unassigned_variable(self, assignment):
        for var in self.variables:
            if var not in assignment:
                return var

    def order_domain_values(self, var):
        return self.domains[var]

    def is_safe(self, assignment, row, col):
        for prev_row, prev_col in assignment.items():
            if prev_col == col or abs(prev_row - row) == abs(prev_col - col):
                return False
        return True

    def forward_check(self, assignment, var, value):
        updated_domains = {v: list(self.domains[v]) for v in self.variables if v not in assignment}
        for other_var in updated_domains:
            updated_domains[other_var] = [val for val in updated_domains[other_var] if val != value]
            if not updated_domains[other_var]:
                return None  # Domain wipeout, backtrack
        return updated_domains

    def print_board(self, solution):
        for row in range(self.size):
            print(" ---" * self.size)
            for col in range(self.size):
                p = "Q" if solution and solution[row] == col else " "
                print(f"| {p} ", end="")
            print("|")
        print(" ---" * self.size)


def main():
    print(".: N-Queens Problem (CSP) :.")
    size = int(input("Please enter the size of the board: "))
    n_queens_csp = NQueensCSP(size)

    csp_solutions = n_queens_csp.solve_csp()

    print("CSP Solutions:")
    for i, solution in enumerate(csp_solutions):
        print(f"CSP Solution {i + 1}:")
        n_queens_csp.print_board(solution)

    print(f"Total CSP solutions: {len(csp_solutions)}")


if __name__ == "__main__":
    main()


# In[ ]:




