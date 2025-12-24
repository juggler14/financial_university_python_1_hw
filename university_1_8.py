import copy

# Задача 1: Первый столбец с только нечетными числами
def task1(matrix):
    if not matrix: return 0
    for col in zip(*matrix):
        if all(x % 2 != 0 for x in col):
            return matrix[0].index(col[0]) + 1
    return 0

# Задача 2: Поменять min и max в каждой строке
def task2(matrix):
    result = [row.copy() for row in matrix]
    for row in result:
        mn, mx = min(row), max(row)
        i_min, i_max = row.index(mn), row.index(mx)
        row[i_min], row[i_max] = mx, mn
    return result

# Задача 3: Поменять строки с min и max элементами
def task3(matrix):
    if not matrix: return []
    flat = [item for row in matrix for item in row]
    min_idx = flat.index(min(flat)) // len(matrix[0])
    max_idx = flat.index(max(flat)) // len(matrix[0])
    result = matrix.copy()
    result[min_idx], result[max_idx] = result[max_idx], result[min_idx]
    return result

# Задача 4: Горизонтальное отражение
def task4(matrix):
    return matrix[::-1]

# Задача 5: Удалить строку с минимальным элементом
def task5(matrix):
    if not matrix: return []
    min_val = min(item for row in matrix for item in row)
    for i, row in enumerate(matrix):
        if min_val in row:
            return matrix[:i] + matrix[i+1:]

# Задача 6: Удалить столбец с максимальным элементом
def task6(matrix):
    if not matrix: return []
    max_val = max(item for row in matrix for item in row)
    for j in range(len(matrix[0])):
        if any(row[j] == max_val for row in matrix):
            return [[row[i] for i in range(len(row)) if i != j] for row in matrix]

# Задача 7: Вертикальное отражение
def task7(matrix):
    return [row[::-1] for row in matrix]

# Задача 8: Дублировать строку с максимальным элементом
def task8(matrix):
    if not matrix: return []
    max_val = max(item for row in matrix for item in row)
    for i, row in enumerate(matrix):
        if max_val in row:
            return matrix[:i+1] + [row] + matrix[i+1:]

# Задача 9: Количество элементов больше среднего в каждом столбце
def task9(matrix):
    if not matrix: return []
    return [sum(1 for x in col if x > sum(col)/len(col)) 
            for col in zip(*matrix)]

# Задача 10: Поменять левую верхнюю и правую нижнюю четверти
def task10(matrix):
    m, n = len(matrix), len(matrix[0])
    h_m, h_n = m//2, n//2
    result = copy.deepcopy(matrix)
    for i in range(h_m):
        for j in range(h_n):
            result[i][j], result[i+h_m][j+h_n] = result[i+h_m][j+h_n], result[i][j]
    return result

# Задача 11: Среднее арифметическое строк с нечетными номерами
def task11(matrix):
    return [sum(row)/len(row) for i, row in enumerate(matrix) if i % 2 == 0]

# Задача 12: Строка с наибольшей суммой и ее сумма
def task12(matrix):
    if not matrix: return 0, 0
    sums = [sum(row) for row in matrix]
    max_sum = max(sums)
    max_row_index = sums.index(max_sum) + 1  # +1 для нумерации с 1
    return max_row_index, max_sum

# Задача 13: Вставить строку нулей перед строкой с минимальным элементом
def task13(matrix):
    if not matrix: return []
    min_val = min(item for row in matrix for item in row)
    for i, row in enumerate(matrix):
        if min_val in row:
            zero_row = [0] * len(row)
            return matrix[:i] + [zero_row] + matrix[i:]

# Задача 14: Последняя строка с только четными числами
def task14(matrix):
    result = 0
    for i, row in enumerate(matrix, 1):
        if all(x % 2 == 0 for x in row):
            result = i
    return result

# Задача 15: Поменять 1-й столбец с последним положительным столбцом
def task15(matrix):
    if not matrix: return []
    cols = list(zip(*matrix))
    last_pos_col = None
    for j, col in enumerate(cols):
        if all(x > 0 for x in col):
            last_pos_col = j
    
    if last_pos_col is not None and last_pos_col != 0:
        result = copy.deepcopy(matrix)
        for i in range(len(result)):
            result[i][0], result[i][last_pos_col] = result[i][last_pos_col], result[i][0]
        return result
    return matrix

# Тестирование
if name == "__main__":
    # Тестовая матрица
    mat = [
        [1, 3, 5, 7],
        [2, 4, 6, 8],
        [9, 11, 13, 15],
        [0, -2, 4, 6]
    ]
    
    print("Исходная матрица:")
    for row in mat:
        print(row)
    
    print(f"\n1: {task1(mat)}")
    print(f"2: {task2(mat)}")
    print(f"3: {task3(mat)}")
    print(f"4: {task4(mat)}")
    print(f"5: {task5(mat)}")
    print(f"6: {task6(mat)}")
    print(f"7: {task7(mat)}")
    print(f"8: {task8(mat)}")
    print(f"9: {task9(mat)}")
    print(f"10: {task10(mat)}")
    print(f"11: {task11(mat)}")
    print(f"12: {task12(mat)}")
    print(f"13: {task13(mat)}")
    print(f"14: {task14(mat)}")
    print(f"15: {task15(mat)}")