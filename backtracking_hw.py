class SudokuSolver:
    def __init__(self, board):
        # Inicializa el Sudoku, el tablero y las variables
        self.board = board
        self.variables = self.get_variables()
        self.domains = {var: list(range(1, 10)) for var in self.variables}
    
    def get_variables(self):
        # Las variables son las posiciones en el tablero
        variables = []
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:  # Las celdas vacías son las variables
                    variables.append((row, col))
        return variables
    
    def select_unassigned_variable(self, assignment):
        # Selecciona una variable no asignada (la primera que encuentre)
        for var in self.variables:
            if var not in assignment:
                return var
        return None
    
    def is_consistent(self, var, assignment):
        row, col = var
        value = assignment[var]
        
        # Verificar fila
        if value in [self.board[row][i] for i in range(9)]:
            return False
        
        # Verificar columna
        if value in [self.board[i][col] for i in range(9)]:
            return False
        
        # Verificar subcuadro 3x3
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.board[start_row + i][start_col + j] == value:
                    return False
        
        return True
    
    def backtracking_search(self, assignment={}):
        """Backtracking search to find a solution."""
        # Si la asignación es completa, devolver la asignación
        if len(assignment) == len(self.variables):
            return assignment
        
        # Seleccionar una variable no asignada
        var = self.select_unassigned_variable(assignment)
        
        # Intentar asignar cada valor en el dominio de la variable
        for value in self.domains[var]:
            new_assignment = assignment.copy()
            new_assignment[var] = value
            if self.is_consistent(var, new_assignment):
                print(f"Se asigna {value} a la celda {var} (row {var[0]}, col {var[1]})")  # Imprime el valor asignado
                result = self.backtracking_search(new_assignment)
                if result:
                    return result
                print(f"Se deshace la asignación de {value} a la celda {var}")  # Imprime el valor deshecho
            else:
                print(f"{value} no es válido para la celda {var}")  # Imprime los valores no válidos
        
        return None

    def solve(self):
        # Llamada a backtracking_search para resolver el Sudoku
        assignment = self.backtracking_search()
        
        if assignment is not None:
            # Colocar los valores resueltos en el tablero
            for (row, col), value in assignment.items():
                self.board[row][col] = value
            return self.board
        else:
            return None

    def print_board(self):
        for row in self.board:
            print(" ".join(str(num) if num != 0 else '.' for num in row))

# Ejemplo de tablero de Sudoku
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Crear el solucionador de Sudoku
solver = SudokuSolver(sudoku_board)

# Resolver el Sudoku
solved_board = solver.solve()

# Mostrar el tablero resuelto
if solved_board:
    print("Sudoku resuelto:")
    solver.print_board()
else:
    print("No se puede resolver el Sudoku.")
