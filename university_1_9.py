def task1(s): return len(s.split())
def task2(s): return sum(1 for word in s.split() if word and word[0] == word[-1])
def task3(s): return sum(1 for word in s.split() if 'А' in word)
def task4(s): return min((len(word) for word in s.split()), default=0)
def task5(s): return ' '.join(reversed(s.split()))
def task6(s): return ' '.join(sorted(s.split()))
def task7(C, S, S0): return S.replace(C, S0 + C)
def task8(s): return ' '.join(s.split())
def task9(s): return sum(1 for ch in s if ch.islower())
def task10(s): return max((len(word) for word in s.split()), default=0)
def task11(s): return s[1::2] + s[0::2][::-1]
def task12(S, N): return ('*' * N).join(S)
def task13(s): return '.'.join(s.split())
def task14(s):
    # Находим последний обратный слеш или обычный слеш
    last_sep = max(s.rfind('\\'), s.rfind('/'))
    filename = s[last_sep + 1:] if last_sep != -1 else s
    # Находим последнюю точку
    last_dot = filename.rfind('.')
    # Если точка есть и она не первая, возвращаем часть до нее
    if last_dot > 0:
        return filename[:last_dot]

    return filename
# Тест

def task15(s): 
    words = s.split()
    return max(reversed(words), key=len) if words else ''