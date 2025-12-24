# 1а
def check_number(num_str):
    try:
        num = int(num_str)
        if num == 0:
            raise ZeroDivisionError("Число не может быть нулевым")
        elif num < 0:
            raise ValueError("Число должно быть положительным")
        return "Число введено корректно"
    except ValueError as e:
        if str(e) == "Число должно быть положительным":
            return str(e)
        return "Ошибка: введено не число"
    except ZeroDivisionError as e:
        return str(e)

# 1б
def check_age(age_str):
    try:
        age = int(age_str)
        if age < 18:
            raise Exception("Несовершеннолетний пользователь")
        elif age > 100:
            raise Exception("Неверный возраст")
        return "Возраст введен корректно"
    except ValueError:
        return "Ошибка: введено не число"
    except Exception as e:
        return str(e)

# 1в
def check_number_assert(num_str):
    try:
        num = int(num_str)
        assert num >= 0, "Число должно быть положительным"
        return "Число введено корректно"
    except ValueError:
        return "Ошибка: введено не число"
    except AssertionError as e:
        return str(e)

# 2а
def read_file_safe(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        return "Файл успешно прочитан"
    except FileNotFoundError:
        return "Файл не найден"
    except IOError:
        return "Ошибка чтения файла"

# 2б
def check_palindrome(s):
    try:
        if s != s[::-1]:
            raise Exception("Строка не является палиндромом")
        return "Строка является палиндромом"
    except Exception as e:
        return str(e)

# 2в
def read_file_assert(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            assert f.read(), "Файл не найден"
        return "Файл успешно прочитан"
    except (FileNotFoundError, AssertionError):
        return "Файл не найден"
    except Exception:
        return "Ошибка"

# 3а
def divide_numbers(a_str, b_str):
    try:
        a, b = int(a_str), int(b_str)
        if b == 0:
            raise ZeroDivisionError("Деление на ноль запрещено")
        return str(a / b)
    except ValueError:
        return "Ошибка: введены не числа"
    except ZeroDivisionError as e:
        return str(e)

# 3б
def check_prime(num_str):
    try:
        n = int(num_str)
        if n < 2:
            raise Exception("Число не является простым")
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                raise Exception("Число не является простым")
        return "Число является простым"
    except ValueError:
        return "Ошибка: введено не число"
    except Exception as e:
        return str(e)

# 3в
def divide_numbers_assert(a_str, b_str):
    try:
        a, b = int(a_str), int(b_str)
        assert b != 0, "Деление на ноль запрещено"
        return str(a / b)
    except ValueError:
        return "Ошибка: введены не числа"
    except AssertionError as e:
        return str(e)

# 4а
def check_filename(filename):
    invalid_chars = '<>:"/\\|?*'
    try:
        if any(char in filename for char in invalid_chars):
            raise Exception("Недопустимое имя файла")
        return "Имя файла введено корректно"
    except Exception as e:
        return str(e)

# 4б
def check_birthdate(date_str):
    try:
        day, month, year = date_str.split('.')
        if len(day) != 2 or len(month) != 2 or len(year) != 4:
            raise Exception("Неверный формат даты")
        if not (1 <= int(day) <= 31 and 1 <= int(month) <= 12 and 1900 <= int(year) <= 2100):
            raise Exception("Неверный формат даты")
        return "Дата введена корректно"
    except (ValueError, Exception) as e:
        return "Неверный формат даты"

# 4в
def check_coordinates(x_str, y_str):
    try:
        x, y = float(x_str), float(y_str)
        return "Координаты введены корректно"
    except ValueError:
        return "Некорректные координаты"

# 5а
def open_file_safe(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            if not filename.endswith('.txt'):
                raise TypeError("Файл не является текстовым")
            content = f.read()
        return "Файл успешно открыт"
    except FileNotFoundError:
        return "Файл не найден"
    except TypeError as e:
        return str(e)

# 5б
def check_if_number(s):
    try:
        float(s)
        return "Строка является числом"
    except ValueError:
        return "Строка не является числом"

# 5в
def open_file_assert(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            assert filename.endswith('.txt'), "Файл не является текстовым"
        return "Файл успешно открыт"
    except FileNotFoundError:
        return "Файл не найден"
    except AssertionError as e:
        return str(e)

# 6а
def power_number(base_str, exp_str):
    try:
        base, exp = int(base_str), int(exp_str)
        if exp < 0:
            raise ValueError("Отрицательная степень")
        return str(base ** exp)
    except ValueError as e:
        if str(e) == "Отрицательная степень":
            return str(e)
        return "Ошибка: введены не числа"

# 6б
def check_even(num_str):
    try:
        num = int(num_str)
        if num % 2 != 0:
            raise Exception("Число не является четным")
        return "Число является четным"
    except ValueError:
        return "Ошибка: введено не число"
    except Exception as e:
        return str(e)

# 6в
def power_number_assert(base_str, exp_str):
    try:
        base, exp = int(base_str), int(exp_str)
        assert exp >= 0, "Отрицательная степень"
        return str(base ** exp)
    except ValueError:
        return "Ошибка: введены не числа"
    except AssertionError as e:
        return str(e)

# 7а
def check_name(name):
    try:
        if not name.isalpha():
            raise Exception("Некорректное имя")
        return "Имя введено корректно"
    except Exception as e:
        return str(e)

# 7б
def check_phone(phone):
    try:
        if not (phone.startswith('+7') and len(phone) == 12 and phone[1:].isdigit()):
            raise Exception("Неверный формат номера")
        return "Номер введен корректно"
    except Exception as e:
        return str(e)

# 7в
def check_email(email):
    try:
        if '@' not in email or '.' not in email.split('@')[1]:
            raise Exception("Неверный формат email")
        return "Email введен корректно"
    except Exception as e:
        return str(e)

# 8а
def open_file_empty(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            if not content:
                raise EOFError("Файл пустой")
        return "Файл успешно открыт"
    except FileNotFoundError:
        return "Файл не найден"
    except EOFError as e:
        return str(e)

# 8б
def check_url(url):
    try:
        if not (url.startswith('http://') or url.startswith('https://')):
            raise Exception("Строка не является URL-адресом")
        return "Строка является URL-адресом"
    except Exception as e:
        return str(e)

# 8в
def open_file_empty_assert(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            assert content, "Файл пустой"
        return "Файл успешно открыт"
    except FileNotFoundError:
        return "Файл не найден"
    except AssertionError as e:
        return str(e)

# 9а
def factorial_safe(num_str):
    try:
        n = int(num_str)
        if n < 0:
            raise ValueError("Отрицательное число")
        result = 1
        for i in range(2, n + 1):
            result *= i
        return str(result)
    except ValueError as e:
        if str(e) == "Отрицательное число":
            return str(e)
        return "Ошибка: введено не число"

# 9б
def check_positive(num_str):
    try:
        num = int(num_str)
        if num <= 0:
            raise Exception("Число не является положительным")
        return "Число является положительным"
    except ValueError:
        return "Ошибка: введено не число"
    except Exception as e:
        return str(e)

# 9в
def factorial_assert(num_str):
    try:
        n = int(num_str)
        assert n >= 0, "Отрицательное число"
        result = 1
        for i in range(2, n + 1):
            result *= i
        return str(result)
    except ValueError:
        return "Ошибка: введено не число"
    except AssertionError as e:
        return str(e)

# 10а
def check_height(height_str):
    try:
        height = int(height_str)
        if height < 0 or height > 300:
            raise Exception("Некорректный рост")
        return "Рост введен корректно"
    except ValueError:
        return "Ошибка: введено не число"
    except Exception as e:
        return str(e)

# 10б
def check_weight(weight_str):
    try:
        weight = int(weight_str)
        if weight < 0 or weight > 500:
            raise Exception("Некорректный вес")
        return "Вес введен корректно"
    except ValueError:
        return "Ошибка: введено не число"
    except Exception as e:
        return str(e)

# 10в
def check_temperature(temp_str):
    try:
        temp = float(temp_str)
        if temp < -273.15:
            raise Exception("Некорректная температура")
        return "Температура введена корректно"
    except ValueError:
        return "Ошибка: введено не число"
    except Exception as e:
        return str(e)

# 11а
def open_file_chars(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            invalid_chars = '\x00\x01\x02\x03\x04\x05\x06\x07\x08\x0b\x0c\x0e\x0f'
            if any(char in content for char in invalid_chars):
                raise ValueError("Файл содержит недопустимые символы")
        return "Файл успешно открыт"
    except FileNotFoundError:
        return "Файл не найден"
    except ValueError as e:
        return str(e)

# 11б
def check_empty_string(s):
    try:
        if s.strip():
            raise Exception("Строка не является пустой")
        return "Строка является пустой"
    except Exception as e:
        return str(e)

# 11в
def open_file_chars_assert(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            invalid_chars = '\x00\x01\x02\x03\x04\x05\x06\x07\x08\x0b\x0c\x0e\x0f'
            assert not any(char in content for char in invalid_chars), "Файл содержит недопустимые символы"
        return "Файл успешно открыт"
    except FileNotFoundError:
        return "Файл не найден"
    except AssertionError as e:
        return str(e)

# 12а
def check_square(num_str):
    try:
        n = int(num_str)
        root = int(n ** 0.5)
        if root * root != n:
            raise Exception("Число не является квадратом целого числа")
        return "Число является квадратом целого числа"
    except ValueError:
        return "Ошибка: введено не число"
    except Exception as e:
        return str(e)

# 12б
def check_palindrome2(s):
    try:
        if s != s[::-1]:
            raise Exception("Строка не является палиндромом")
        return "Строка является палиндромом"
    except Exception as e:
        return str(e)

# 12в
def check_square_assert(num_str):
    try:
        n = int(num_str)
        root = int(n ** 0.5)
        assert root * root == n, "Число не является квадратом целого числа"
        return "Число является квадратом целого числа"
    except ValueError:
        return "Ошибка: введено не число"
    except AssertionError as e:
        return str(e)

# 13а
def check_age_range(age_str):
    try:
        age = int(age_str)
        if age < 0 or age > 150:
            raise Exception("Некорректный возраст")
        return "Возраст введен корректно"
    except ValueError:
        return "Ошибка: введено не число"
    except Exception as e:
        return str(e)

# 13б
def check_gender(gender):
    try:
        if gender not in ['м', 'ж']:
            raise Exception("Некорректный пол")
        return "Пол введен корректно"
    except Exception as e:
        return str(e)

# 13в
def check_name_assert(name):
    try:
        assert name.isalpha(), "Некорректное имя"
        return "Имя введено корректно"
    except AssertionError as e:
        return str(e)

# 14а
def check_power_of_two(num_str):
    try:
        n = int(num_str)
        if n <= 0 or (n & (n - 1)) != 0:
            raise Exception("Число не является степенью двойки")
        return "Число является степенью двойки"
    except ValueError:
        return "Ошибка: введено не число"
    except Exception as e:
        return str(e)

# 14б
def check_palindrome3(s):
    try:
        if s != s[::-1]:
            raise Exception("Строка не является палиндромом")
        return "Строка является палиндромом"
    except Exception as e:
        return str(e)

# 14в
def check_power_of_two_assert(num_str):
    try:
        n = int(num_str)
        assert n > 0 and (n & (n - 1)) == 0, "Число не является степенью двойки"
        return "Число является степенью двойки"
    except ValueError:
        return "Ошибка: введено не число"
    except AssertionError as e:
        return str(e)

# 15а
def check_name_not_empty(name):
    try:
        if not name or name.isspace():
            raise Exception("Некорректное имя")
        return "Имя введено корректно"
    except Exception as e:
        return str(e)

# 15б
def check_age_range2(age_str):
    try:
        age = int(age_str)
        if age < 0 or age > 120:
            raise Exception("Некорректный возраст")
        return "Возраст введен корректно"
    except ValueError:
        return "Ошибка: введено не число"
    except Exception as e:
        return str(e)

# 15в
def check_gender_assert(gender):
    try:
        assert gender in ['м', 'ж'], "Некорректный пол"
        return "Пол введен корректно"
    except AssertionError as e:
        return str(e)