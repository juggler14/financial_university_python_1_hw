import math

# 1. Произведение компонент файла (действительные числа)
def task1(f_name):
    with open(f_name, 'r') as f:
        numbers = [float(x) for x in f.read().split()]
    prod = 1
    for num in numbers:
        prod *= num
    return prod

# 2. Разделить положительные и отрицательные числа
def task2(f_name, g_name):
    with open(f_name, 'r') as f:
        numbers = [int(x) for x in f.read().split()]
    
    positives = [x for x in numbers if x > 0]
    negatives = [x for x in numbers if x < 0]
    
    with open(g_name, 'w') as g:
        g.write(' '.join(map(str, positives + negatives)))

# 3. Получить точные квадраты
def task3(f_name, g_name):
    with open(f_name, 'r') as f:
        numbers = [int(x) for x in f.read().split()]
    
    squares = [x for x in numbers if int(math.sqrt(x))**2 == x]
    
    with open(g_name, 'w') as g:
        g.write(' '.join(map(str, squares)))

# 4. Сумма наибольшего и наименьшего значений
def task4(f_name):
    with open(f_name, 'r') as f:
        numbers = [float(x) for x in f.read().split()]
    return max(numbers) + min(numbers)

# 5. Найти год с наименьшим номером (даты в формате: день месяц год)
def task5(f_name):
    with open(f_name, 'r') as f:
        dates = [line.strip().split() for line in f]
    
    years = [int(date[2]) for date in dates if len(date) >= 3]
    return min(years) if years else None

# 6. Количество четных чисел
def task6(f_name):
    with open(f_name, 'r') as f:
        numbers = [int(x) for x in f.read().split()]
    return sum(1 for x in numbers if x % 2 == 0)

# 7. Проверить первые два символа
def task7(f_name):
    with open(f_name, 'r') as f:
        content = f.read().strip()
    
    if len(content) >= 2:
        first_two = content[:2]
        if first_two.isdigit():
            num = int(first_two)
            return True, num % 2 == 0
    return False, False

# 8. Получить четные числа
def task8(f_name, g_name):
    with open(f_name, 'r') as f:
        numbers = [int(x) for x in f.read().split()]
    
    evens = [x for x in numbers if x % 2 == 0]
    
    with open(g_name, 'w') as g:
        g.write(' '.join(map(str, evens)))

# 9. Наибольшее из значений модулей компонент с нечетными номерами
def task9(f_name):
    with open(f_name, 'r') as f:
        numbers = [float(x) for x in f.read().split()]
    
    odd_index_values = [abs(numbers[i]) for i in range(0, len(numbers), 2)]
    return max(odd_index_values)

# 10. Найти все весенние даты (март, апрель, май)
def task10(f_name):
    with open(f_name, 'r') as f:
        dates = [line.strip().split() for line in f]
    
    spring_dates = []
    for date in dates:
        if len(date) >= 3:
            month = int(date[1])
            if 3 <= month <= 5:
                spring_dates.append(date)
    return spring_dates

# 11. Числа, делящиеся на 3 и не делящиеся на 7
def task11(f_name, g_name):
    with open(f_name, 'r') as f:
        numbers = [int(x) for x in f.read().split()]
    
    result = [x for x in numbers if x % 3 == 0 and x % 7 != 0]
    
    with open(g_name, 'w') as g:
        g.write(' '.join(map(str, result)))

# 12. Наименьшее из значений компонент с четными номерами
def task12(f_name):
    with open(f_name, 'r') as f:
        numbers = [float(x) for x in f.read().split()]
    
    even_index_values = [numbers[i] for i in range(1, len(numbers), 2)]
    return min(even_index_values) if even_index_values else None

# 13. Разделить четные и нечетные числа
def task13(f_name, g_name, h_name):
    with open(f_name, 'r') as f:
        numbers = [int(x) for x in f.read().split()]
    
    evens = [x for x in numbers if x % 2 == 0]
    odds = [x for x in numbers if x % 2 != 0]
    
    with open(g_name, 'w') as g:
        g.write(' '.join(map(str, evens)))
    with open(h_name, 'w') as h:
        h.write(' '.join(map(str, odds)))

# 14. Числа без соседства одинаковых знаков
def task14(f_name, g_name):
    with open(f_name, 'r') as f:
        numbers = [int(x) for x in f.read().split()]
    
    result = []
    for i, num in enumerate(numbers):
        if i == 0:
            result.append(num)
        else:
            # Проверяем знак предыдущего числа
            if (num > 0 and result[-1] > 0) or (num < 0 and result[-1] < 0):
                # Пропускаем, чтобы не было двух подряд с одним знаком
                continue
            result.append(num)
    
    with open(g_name, 'w') as g:
        g.write(' '.join(map(str, result)))

# 15. Паттерн: два положительных, два отрицательных
def task15(f_name, g_name):
    with open(f_name, 'r') as f:
        numbers = [int(x) for x in f.read().split()]
    
    positives = [x for x in numbers if x > 0]
    negatives = [x for x in numbers if x < 0]
    
    result = []
    for i in range(0, len(numbers), 4):
        result.extend(positives[i:i+2])
        result.extend(negatives[i:i+2])
    
    with open(g_name, 'w') as g:
        g.write(' '.join(map(str, result)))

