lst = [5, -3, 12, 7, 0, -8, 15, 20, -12, 9, 11, 14, 25, 30, -3, 6]
k = 10

def task1(lst): return sorted([x for x in lst if x % 2 != 0], reverse=True)

def task2(lst): return sorted([x for x in lst if x > 0])

def task3(lst): return sorted([x for x in lst if x > 0], reverse=True)

def task4(lst): return sorted([x for x in lst if x % 2 == 0])

def task5(lst, k): return sorted([x for x in lst if x > k], reverse=True)

def task6(lst): return sorted([x for x in lst if x > 10])

def task7(lst): return sorted([x for x in lst if x % 5 == 0], reverse=True)

def task8(lst, k): return sorted([x for x in lst if x < k])

def task9(lst): return sorted([x for x in lst if x < 15], reverse=True)

def task10(lst): return sorted([x for x in lst if x % 3 == 0])

def task11(lst, k): return sorted([x for x in lst if x % k == 0], reverse=True)

def task12(lst): return sorted([x for x in lst if x < 0])

def task13(lst): return sorted([lst[i] for i in range(0, len(lst), 2)], reverse=True)

def task14(lst): return sorted([x for x in lst if 10 <= abs(x) <= 99])

def task15(lst): return sorted([lst[i] for i in range(1, len(lst), 2)])

# print("1:", task1(lst))
# print("2:", task2(lst))
# print("3:", task3(lst))
# print("4:", task4(lst))
# print("5:", task5(lst, k))
# print("6:", task6(lst))
# print("7:", task7(lst))
# print("8:", task8(lst, k))
# print("9:", task9(lst))
# print("10:", task10(lst))
# print("11:", task11(lst, k))
# print("12:", task12(lst))
# print("13:", task13(lst))
# print("14:", task14(lst))
# print("15:", task15(lst))