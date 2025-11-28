def solve_sudoku(board):
    """
    Решает судоку 9x9 с помощью алгоритма backtracking.
    Пустые клетки обозначены как 0.
    """
    # Находим первую пустую клетку
    empty = find_empty(board)

    # Если нет пустых клеток - судоку решено
    if not empty:
        return True

    row, col = empty

    # Пробуем числа от 1 до 9
    for num in range(1, 10):
        if is_valid(board, num, row, col):
            # Если число подходит, помещаем его в клетку
            board[row][col] = num

            # Рекурсивно пытаемся решить оставшуюся часть
            if solve_sudoku(board):
                return True

            # Если не получилось, откатываем изменения (backtrack)
            board[row][col] = 0

    # Если ни одно число не подошло, возвращаем False
    return False


def find_empty(board):
    """
    Находит первую пустую клетку (значение 0) на доске.
    Возвращает координаты (row, col) или None, если пустых клеток нет.
    """
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None


def is_valid(board, num, row, col):
    """
    Проверяет, можно ли разместить число num в клетке (row, col)
    без нарушения правил судоку.
    """
    # Проверка строки
    for j in range(9):
        if board[row][j] == num and j != col:
            return False

    # Проверка столбца
    for i in range(9):
        if board[i][col] == num and i != row:
            return False

    # Проверка квадрата 3x3
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3

    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num and (i != row or j != col):
                return False

    return True


def print_board(board):
    """
    Красиво выводит доску судоку.
    """
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


# Пример использования:
if __name__ == "__main__":
    # Пример сложного судоку
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

    print("Исходное судоку:")
    print_board(sudoku_board)
    print("\n" + "=" * 30 + "\n")

    if solve_sudoku(sudoku_board):
        print("Решенное судоку:")
        print_board(sudoku_board)
    else:
        print("Решение не найдено!")