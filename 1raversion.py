#Resolución de un sudoku con backtraking
#   Descripción: El algoritmo de backtracking para Sudoku intenta colocar números en lasceldas 
#   vacías siguiendo las reglas del Sudoku. Retrocede cuando se encuentra una violación delas reglas, 
#   tratando diferentes números hasta encontrar una solución válida.

# Explicación del código y funciones:
'''
1. solve_sudoku(board):
   - Es la función principal que resuelve el Sudoku usando backtracking.
   - Busca una celda vacía (con 0). Si no hay, el Sudoku está resuelto.
   - Prueba números del 1 al 9 en esa celda.
   - Si el número es válido (no rompe las reglas), lo coloca y sigue recursivamente.
   - Si no puede avanzar, borra el número (retrocede) y prueba el siguiente.

2. is_valid(board, num, pos):
   - Verifica si es válido colocar el número 'num' en la posición 'pos' (fila, columna).
   - Revisa que el número no esté repetido en la misma fila, columna ni en el subcuadro 3x3.

3. find_empty(board):
   - Busca la primera celda vacía (con 0) en el tablero.
   - Devuelve la posición (fila, columna) o None si no hay vacías.

4. print_board(board):
   - Imprime el tablero de Sudoku de forma visual y ordenada.
   - Muestra líneas para separar los subcuadros 3x3.

5. sudoku (variable):
   - Es un ejemplo de tablero de Sudoku con algunos números y espacios vacíos (0).
   - Puedes cambiar los valores para probar otros tableros.

6. El flujo principal:
   - Imprime el Sudoku original.
   - Llama a solve_sudoku para resolverlo.
   - Si hay solución, la imprime; si no, avisa que no hay solución.
'''
###################################################################################
# Algoritmo de backtracking para resolver Sudoku 9x9
# Busca una celda vacía, prueba números del 1 al 9 y retrocede si es necesario

def solve_sudoku(board):
    empty = find_empty(board)  # Busca la siguiente celda vacía
    if not empty:
        return True  # Si no hay vacías, el Sudoku está resuelto
    row, col = empty
    for num in range(1, 10):  # Prueba números del 1 al 9
        if is_valid(board, num, (row, col)):
            board[row][col] = num  # Coloca el número si es válido
            if solve_sudoku(board):  # Llama recursivamente
                return True
            board[row][col] = 0  # Si no funciona, borra y prueba otro
    return False

# Verifica si es válido colocar 'num' en la posición 'pos' (fila, columna)
def is_valid(board, num, pos):
    row, col = pos
    # Verifica que el número no esté en la misma fila
    for i in range(9):
        if board[row][i] == num and col != i:
            return False
    # Verifica que el número no esté en la misma columna
    for i in range(9):
        if board[i][col] == num and row != i:
            return False
    # Verifica que el número no esté en el subcuadro 3x3
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True

# Busca la primera celda vacía (con 0) en el tablero
def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)  # Devuelve la posición de la celda vacía
    return None  # Si no hay vacías, devuelve None

# Imprime el tablero de Sudoku de forma visual y ordenada
def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print('-' * 21)  # Línea separadora de subcuadros
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print('|', end=' ')  # Línea vertical separadora
            print(board[i][j] if board[i][j] != 0 else '.', end=' ')
        print()

# Ejemplo de uso:
sudoku = [ 
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

print('Sudoku original:')
print_board(sudoku)
if solve_sudoku(sudoku):
    print('\nSolución:')
    print_board(sudoku)
else:
    print('No hay solución.')
    
#########################################################################################

