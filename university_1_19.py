# 1. 
def task1(input_file, output_file, K):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(lines[-K:])

# 2. 
def task2(filename, K):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(lines[:-K])

# 3. 
def task3(filename, K):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    with open(filename, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line[K:] if len(line) > K else '')

# 4. 
def task4(file1, file2):
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        lines1, lines2 = f1.readlines(), f2.readlines()
    with open(file1, 'w', encoding='utf-8') as f:
        for i in range(min(len(lines1), len(lines2))):
            f.write(lines1[i].rstrip('\n') + lines2[i])
        if len(lines1) > len(lines2):
            f.writelines(lines1[len(lines2):])

# 5. 
def task5(filename, K):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    if 1 <= K <= len(lines):
        with open(filename, 'w', encoding='utf-8') as f:
            f.writelines(lines[:K-1] + lines[K:])

# 6. 
def task6(input_file, output_file):
    import string
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    punct = ''.join(c for c in text if c in string.punctuation + '«»—')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(punct)

# 7. 
def task7(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        numbers = [int(line.strip()) for line in f]
    return len(numbers), sum(numbers)

# 8. 
def task8(filename, S):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    with open(filename, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(S + '\n' if line.strip() == '' else line)

# 9. 
def task9(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    with open(filename, 'w', encoding='utf-8') as f:
        for line in lines:
            line = line.rstrip('\n')
            if line:
                if len(line) % 2 == 1:
                    line = ' ' + line
                spaces = (50 - len(line)) // 2
                f.write(' ' * spaces + line + '\n')
            else:
                f.write('\n')

# 10. 
def task10(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f]
    count = 0
    in_paragraph = False
    for line in lines:
        if line:
            if not in_paragraph:
                count += 1
                in_paragraph = True
        else:
            in_paragraph = False
    return count

# 11. 
def task11(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    with open(filename, 'w', encoding='utf-8') as f:
        for line in lines:
            line = line.rstrip('\n')
            if line:
                spaces = 50 - len(line)
                f.write(' ' * spaces + line + '\n')
            else:
                f.write('\n')

# 12. 
def task12(file1, file2):
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        content1, content2 = f1.read(), f2.read()
    with open(file1, 'w', encoding='utf-8') as f:
        f.write(content2 + content1)

# 13. 
def task13(filename, K):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    if 1 <= K <= len(lines):
        lines.insert(K-1, '\n')
        with open(filename, 'w', encoding='utf-8') as f:
            f.writelines(lines)

# 14. 
def task14(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    with open(filename, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line)
            if line.strip() == '':
                f.write(line)

# 15. 
def task15(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(lines[1:-1])

