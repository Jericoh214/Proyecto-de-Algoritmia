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

##### SE USA UNA LIBRERIA (tkinter) para tener visualmente y en tiempo real un ejemlo de sudoku resuelto con backtracking ####
#########################################################################################
# Ejemplo visual usando tkinter para jugar y resolver Sudoku
'''Se implementa una interfaz gráfica con tkinter que permite al usuario jugar y resolver Sudoku.
   - El usuario puede ingresar números, resolver el Sudoku automáticamente o paso a paso.'''
import tkinter as tk  #importar tkinter como "tk"
from tkinter import messagebox

#comienza la definicion de la clase SudokuGUI
# Esta clase crea una interfaz gráfica para jugar y resolver Sudoku

class SudokuGUI:
    def __init__(self, root, board):
        self.root = root
        self.root.title('Sudoku')  # Título de la ventana
        self.board = [row[:] for row in board]  # Copia del tablero
        self.entries = []  # Lista para guardar los widgets de entrada
        self.solving = False  # Bandera para saber si está resolviendo
      
#forma en la que funsiona el programa 
        for i in range(9):
            row_entries = []
            for j in range(9):
                e = tk.Entry(root, width=2, font=('Arial', 18), justify='center')  # Celda de entrada ||se define la fuente ||y la justificacion (posicion(
                e.grid(row=i, column=j, padx=2, pady=2)
                if board[i][j] != 0:  #cuando board en i o j son diferentesa  0
                    e.insert(0, str(board[i][j]))  # Inserta el número inicial
                    e.config(state='disabled', disabledforeground='black')  # Desactiva la celda si ya tiene número
                row_entries.append(e)
            self.entries.append(row_entries)
        # Botón para resolver automáticamente
        solve_btn = tk.Button(root, text='Resolver', command=self.solve)
        solve_btn.grid(row=9, column=0, columnspan=3, sticky='we')
        # Botón para limpiar el tablero
        clear_btn = tk.Button(root, text='Limpiar', command=self.clear)
        clear_btn.grid(row=9, column=3, columnspan=3, sticky='we')
        # Botón para modo paso a paso
        step_btn = tk.Button(root, text='Paso a paso', command=self.start_step_by_step)
        step_btn.grid(row=9, column=6, columnspan=3, sticky='we')
        # Etiqueta para mostrar mensajes de estado
        self.status = tk.Label(root, text='', font=('Arial', 12))
        self.status.grid(row=10, column=0, columnspan=9)
        self.step_generator = None  # Generador para el modo paso a paso

    def get_board(self):
        # Obtiene el tablero actual desde la interfaz
        for i in range(9):
            for j in range(9):
                val = self.entries[i][j].get()
                self.board[i][j] = int(val) if val.isdigit() else 0
        return self.board

    def set_board(self, board):
        # Actualiza la interfaz con los valores del tablero
        for i in range(9):
            for j in range(9):
                if self.entries[i][j]['state'] == 'normal':
                    self.entries[i][j].delete(0, tk.END)
                    if board[i][j] != 0:
                        self.entries[i][j].insert(0, str(board[i][j]))

    def solve(self):
        # Resuelve el Sudoku automáticamente
        board = self.get_board()
        if solve_sudoku(board):
            self.set_board(board)
            self.status.config(text='¡Sudoku resuelto!', fg='green')
            messagebox.showinfo('Éxito', '¡Sudoku resuelto!')
        else:
            self.status.config(text='No hay solución para este Sudoku.', fg='red')
            messagebox.showerror('Error', 'No hay solución para este Sudoku.')

    def clear(self):
        # Limpia las celdas editables
        for i in range(9):
            for j in range(9):
                if self.entries[i][j]['state'] == 'normal':
                    self.entries[i][j].delete(0, tk.END)
        self.status.config(text='')

    def start_step_by_step(self):
        # Inicia el modo paso a paso
        self.get_board()
        self.step_generator = self.solve_sudoku_step_by_step()
        self.status.config(text='Modo paso a paso: presiona el botón para avanzar.', fg='blue')
        self.root.after(100, self.step_by_step)
        self.speed = 4000  # Tiempo entre pasos en milisegundos

    def step_by_step(self):
        # Ejecuta un paso del algoritmo y resalta la celda
        try:
            i, j, num, valid = next(self.step_generator)
            for x in range(9):
                for y in range(9):
                    if self.entries[x][y]['state'] == 'normal':
                        self.entries[x][y].config(bg='white')  # Restaura color
            if self.entries[i][j]['state'] == 'normal':
                color = 'lightgreen' if valid else 'salmon'
                self.entries[i][j].config(bg=color)  # Resalta celda
                if valid:
                    self.entries[i][j].delete(0, tk.END)
                    self.entries[i][j].insert(0, str(num))
            self.status.config(text=f'Probando {num} en ({i+1},{j+1}): {"Válido" if valid else "No válido"}', fg='blue')
            if valid:
                self.root.after(300, self.step_by_step)
            else:
                self.root.after(600, self.step_by_step)
        except StopIteration:
            self.status.config(text='¡Terminado el modo paso a paso!', fg='green')

    def solve_sudoku_step_by_step(self):
        # Generador que implementa el backtracking paso a paso
        def step(board):
            empty = find_empty(board)
            if not empty:
                return True
            row, col = empty
            for num in range(1, 10):
                valid = is_valid(board, num, (row, col))
                yield (row, col, num, valid)  # Devuelve el intento y si es válido
                if valid:
                    board[row][col] = num
                    result = yield from step(board)
                    if result:
                        return True
                    board[row][col] = 0  # Retrocede si no funciona
            return False
        yield from step(self.board)

if __name__ == '__main__':
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
    root = tk.Tk()
    gui = SudokuGUI(root, sudoku)
    root.mainloop()


