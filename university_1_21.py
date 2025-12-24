# test
lst = [5, -3, 12, 7, 0, -8, 15, 20, -12, 9, 11, 14, 25, 30, -3, 6]
k = 10

# 1. 
result = sorted([x for x in lst if x % 2 != 0], reverse=True)
print("1. Нечетные числа по убыванию:", result)

# 2. 
result = sorted([x for x in lst if x > 0])
print("2. Положительные числа по возрастанию:", result)

# 3. 
result = sorted([x for x in lst if x > 0], reverse=True)
print("3. Положительные числа по убыванию:", result)

# 4. 
result = sorted([x for x in lst if x % 2 == 0])
print("4. Четные числа по возрастанию:", result)

# 5. 
result = sorted([x for x in lst if x > k], reverse=True)
print(f"5. Числа больше {k} по убыванию:", result)

# 6. 
result = sorted([x for x in lst if x > 10])
print("6. Числа больше 10 по возрастанию:", result)

# 7. 
result = sorted([x for x in lst if x % 5 == 0], reverse=True)
print("7. Числа кратные 5 по убыванию:", result)

# 8. 
result = sorted([x for x in lst if x < k])
print(f"8. Числа меньше {k} по возрастанию:", result)

# 9. 
result = sorted([x for x in lst if x < 15], reverse=True)
print("9. Числа меньше 15 по убыванию:", result)

# 10. 
result = sorted([x for x in lst if x % 3 == 0])
print("10. Числа кратные 3 по возрастанию:", result)

# 11. 
result = sorted([x for x in lst if x % k == 0], reverse=True)
print(f"11. Числа кратные {k} по убыванию:", result)

# 12. 
result = sorted([x for x in lst if x < 0])
print("12. Отрицательные числа по возрастанию:", result)

# 13. 
result = sorted([lst[i] for i in range(0, len(lst), 2)], reverse=True)
print("13. Числа на нечетных позициях (1,3,5...) по убыванию:", result)

# 14. 
result = sorted([x for x in lst if 10 <= abs(x) <= 99])
print("14. Двузначные числа по возрастанию:", result)

# 15. 
result = sorted([lst[i] for i in range(1, len(lst), 2)])
print("15. Числа на четных позициях (2,4,6...) по возрастанию:", result)