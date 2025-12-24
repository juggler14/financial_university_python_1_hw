# 1 
# а)
def check_email(email):
    if '@' not in email:
        return False
    local, domain = email.split('@', 1)
    
    if not local or not domain:
        return False
    
    if '.' not in domain:
        return False
    
    allowed_chars_local = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._%+-')
    for char in local:
        if char not in allowed_chars_local:
            return False
    
    allowed_chars_domain = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    for part in domain.split('.'):
        if not part:
            return False
        for char in part:
            if char not in allowed_chars_domain:
                return False
    
    return domain.split('.')[-1].isalpha() and len(domain.split('.')[-1]) >= 2

# б)
def find_emails_in_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    
    words = text.replace(',', ' ').replace(';', ' ').split()
    emails = []
    
    for word in words:
        word = word.strip('.,:;!?()[]{}"\'')
        if '@' in word and '.' in word:
            if check_email(word):
                emails.append(word)
    
    return emails

# 2 
# а)
def check_phone(phone):
    digits = ''.join(c for c in phone if c.isdigit())
    
    if len(digits) == 11:
        if digits[0] == '7' or digits[0] == '8':
            return True
    elif len(digits) == 10:
        return True
    
    return False

# б)
def find_phones_in_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    
    words = text.split()
    phones = []
    digits = ''
    
    for char in text:
        if char.isdigit():
            digits += char
        else:
            if 10 <= len(digits) <= 11:
                if digits[0] == '7' or digits[0] == '8' or len(digits) == 10:
                    phones.append(digits)
            digits = ''
    
    if 10 <= len(digits) <= 11:
        phones.append(digits)
    
    return phones

# 3 
# а)
def check_url(url):
    return url.startswith('http://') or url.startswith('https://') or url.startswith('ftp://')

# б)
def find_urls_in_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    
    words = text.split()
    urls = []
    
    for word in words:
        if word.startswith('http://') or word.startswith('https://') or word.startswith('ftp://'):
            urls.append(word.strip('.,:;!?()[]{}"\''))
    
    return urls

# 4 
# а)
def check_date(date_str):
    if len(date_str) != 10 or date_str[2] != '.' or date_str[5] != '.':
        return False
    
    day = date_str[:2]
    month = date_str[3:5]
    year = date_str[6:]
    
    if not day.isdigit() or not month.isdigit() or not year.isdigit():
        return False
    
    day_num = int(day)
    month_num = int(month)
    year_num = int(year)
    
    if month_num < 1 or month_num > 12:
        return False
    
    days_in_month = [31, 29 if year_num % 4 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if day_num < 1 or day_num > days_in_month[month_num - 1]:
        return False
    
    return True

# б)
def find_dates_in_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    
    words = text.split()
    dates = []
    
    for word in words:
        word = word.strip('.,:;!?()[]{}"\'')
        if len(word) == 10 and word[2] == '.' and word[5] == '.':
            if check_date(word):
                dates.append(word)
    
    return dates

# 5 
# а)
def check_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    
    for part in parts:
        if not part.isdigit():
            return False
        num = int(part)
        if num < 0 or num > 255:
            return False
        if part[0] == '0' and len(part) > 1:
            return False
    
    return True

# б)
def find_ips_in_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    
    words = text.split()
    ips = []
    
    for word in words:
        word = word.strip('.,:;!?()[]{}"\'')
        if check_ip(word):
            ips.append(word)
    
    return ips

# 6 
# а)
def find_words_with_consonants(text):
    consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    words = text.split()
    result = []
    
    for word in words:
        count = 0
        for char in word:
            if char in consonants:
                count += 1
                if count >= 2:
                    result.append(word.strip('.,:;!?()[]{}"\''))
                    break
            else:
                count = 0
    
    return result

# б)
def replace_urls_in_file(input_filename, output_filename):
    with open(input_filename, 'r', encoding='utf-8') as f:
        text = f.read()
    
    words = text.split()
    result_words = []
    
    for word in words:
        if word.startswith('http://') or word.startswith('https://') or word.startswith('ftp://'):
            result_words.append('ссылка')
        else:
            result_words.append(word)
    
    new_text = ' '.join(result_words)
    
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(new_text)
    
    return new_text

# 7 
# а)
def check_phones_format(phones_str):
    phones = phones_str.split(',')
    results = []
    
    for phone in phones:
        phone = phone.strip()
        if len(phone) != 16:
            results.append(False)
            continue
        
        if (phone[0:2] == '+7' and phone[2] == '(' and phone[6] == ')' and 
            phone[10] == '-' and phone[13] == '-'):
            
            digits = phone[3:6] + phone[7:10] + phone[11:13] + phone[14:16]
            if digits.isdigit():
                results.append(True)
            else:
                results.append(False)
        else:
            results.append(False)
    
    return results

# б)
def find_month_year_in_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    
    words = text.split()
    results = []
    
    for word in words:
        word = word.strip('.,:;!?()[]{}"\'')
        if len(word) == 7 and word[2] == '-':
            month = word[:2]
            year = word[3:]
            if month.isdigit() and year.isdigit():
                month_num = int(month)
                if 1 <= month_num <= 12 and len(year) == 4:
                    results.append(word)
    
    return results

# 8 
# а)
def find_words_starting_with_consonant(text):
    consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    words = text.split()
    result = []
    
    for word in words:
        clean_word = word.strip('.,:;!?()[]{}"\'')
        if clean_word and clean_word[0] in consonants:
            result.append(clean_word)
    
    return result

# б)
def find_all_phones_in_file(filename):
    return find_phones_in_file(filename)

# 9 
# а)
def find_words_with_digits(text):
    words = text.split()
    result = []
    
    for word in words:
        clean_word = word.strip('.,:;!?()[]{}"\'')
        digit_count = 0
        for char in clean_word:
            if char.isdigit():
                digit_count += 1
                if digit_count >= 2:
                    result.append(clean_word)
                    break
            else:
                digit_count = 0
    
    return result

# б)
def replace_russian_to_english_in_file(input_filename, output_filename):
    dictionary = {
        'привет': 'hello',
        'мир': 'world',
        'кот': 'cat',
        'собака': 'dog',
        'дом': 'house'
    }
    
    with open(input_filename, 'r', encoding='utf-8') as f:
        text = f.read()
    
    words = text.split()
    result_words = []
    
    for word in words:
        clean_word = word.strip('.,:;!?()[]{}"\'')
        lower_word = clean_word.lower()
        
        if lower_word in dictionary:
            result_words.append(dictionary[lower_word])
        else:
            result_words.append(word)
    
    new_text = ' '.join(result_words)
    
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(new_text)
    
    return new_text

# 10 
# а)
def check_credit_cards(cards_str):
    cards = cards_str.split(',')
    results = []
    
    for card in cards:
        card = card.strip()
        if len(card) != 19:
            results.append(False)
            continue
        
        parts = card.split()
        if len(parts) != 4:
            results.append(False)
            continue
        
        all_digits = True
        for part in parts:
            if len(part) != 4 or not part.isdigit():
                all_digits = False
                break
        
        results.append(all_digits)
    
    return results

# б)
def find_money_in_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    
    words = text.split()
    results = []
    
    for word in words:
        clean_word = word.strip('.,:;!?()[]{}"\'')
        if clean_word.startswith('$'):
            amount = clean_word[1:]
            if amount.replace('.', '', 1).isdigit():
                results.append(clean_word)
    
    return results

# 11 
# а)
def check_all_words_capitalized(text):
    words = text.split()
    for word in words:
        if not word[0].isupper():
            return False
    return True

# б)
def change_date_format_in_file(input_filename, output_filename):
    with open(input_filename, 'r', encoding='utf-8') as f:
        text = f.read()
    
    words = text.split()
    result_words = []
    
    for word in words:
        clean_word = word.strip('.,:;!?()[]{}"\'')
        if len(clean_word) == 10 and clean_word[2] == '.' and clean_word[5] == '.':
            if check_date(clean_word):
                day = clean_word[:2]
                month = clean_word[3:5]
                year = clean_word[6:]
                new_date = f'{month}/{day}/{year}'
                result_words.append(new_date)
            else:
                result_words.append(word)
        else:
            result_words.append(word)
    
    new_text = ' '.join(result_words)
    
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(new_text)
    
    return new_text

# 12 
# а)
def check_emails_list(emails_str):
    emails = emails_str.split(',')
    results = []
    
    for email in emails:
        results.append(check_email(email.strip()))
    
    return results

# б)
def find_time_in_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    
    words = text.split()
    results = []
    
    for word in words:
        clean_word = word.strip('.,:;!?()[]{}"\'')
        if len(clean_word) == 5 and clean_word[2] == ':':
            hours = clean_word[:2]
            minutes = clean_word[3:]
            
            if hours.isdigit() and minutes.isdigit():
                hours_num = int(hours)
                minutes_num = int(minutes)
                
                if 0 <= hours_num <= 23 and 0 <= minutes_num <= 59:
                    results.append(clean_word)
    
    return results

# 13 
# а)
def find_words_ending_with_ing(text):
    words = text.split()
    result = []
    
    for word in words:
        clean_word = word.strip('.,:;!?()[]{}"\'')
        if clean_word.lower().endswith('ing'):
            result.append(clean_word)
    
    return result

# б)
def replace_digits_with_stars_in_file(input_filename, output_filename):
    with open(input_filename, 'r', encoding='utf-8') as f:
        text = f.read()
    
    new_text = ''
    for char in text:
        if char.isdigit():
            new_text += '*'
        else:
            new_text += char
    
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(new_text)
    
    return new_text

# 14 
# а)
def find_words_starting_with_vowel(text):
    vowels = set('aeiouAEIOU')
    words = text.split()
    result = []
    
    for word in words:
        clean_word = word.strip('.,:;!?()[]{}"\'')
        if clean_word and clean_word[0] in vowels:
            result.append(clean_word)
    
    return result

# б)
def find_all_emails_in_file(filename):
    return find_emails_in_file(filename)

# 15 
# а)
def find_words_with_vowels(text):
    vowels = set('aeiouAEIOU')
    words = text.split()
    result = []
    
    for word in words:
        clean_word = word.strip('.,:;!?()[]{}"\'')
        vowel_count = 0
        for char in clean_word:
            if char in vowels:
                vowel_count += 1
                if vowel_count >= 2:
                    result.append(clean_word)
                    break
            else:
                vowel_count = 0
    
    return result

# б)
def replace_english_to_russian_in_file(input_filename, output_filename):
    dictionary = {
        'hello': 'привет',
        'world': 'мир',
        'cat': 'кот',
        'dog': 'собака',
        'house': 'дом'
    }
    
    with open(input_filename, 'r', encoding='utf-8') as f:
        text = f.read()
    
    words = text.split()
    result_words = []
    
    for word in words:
        clean_word = word.strip('.,:;!?()[]{}"\'')
        lower_word = clean_word.lower()
        
        if lower_word in dictionary:
            result_words.append(dictionary[lower_word])
        else:
            result_words.append(word)
    
    new_text = ' '.join(result_words)
    
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(new_text)
    
    return new_text

# Тестирование
if __name__ == "__main__":
    # Тест 1а
    print("1a:", check_email("test@example.com"))
    print("1a:", check_email("invalid.email"))
    
    # Тест 2а
    print("\n2a:", check_phone("+79123456789"))
    print("2a:", check_phone("89123456789"))
    
    # Тест 3а
    print("\n3a:", check_url("https://example.com"))
    print("3a:", check_url("example.com"))
    
    # Тест 4а
    print("\n4a:", check_date("25.12.2023"))
    print("4a:", check_date("32.13.2023"))
    
    # Тест 5а
    print("\n5a:", check_ip("192.168.1.1"))
    print("5a:", check_ip("256.256.256.256"))
    
    # Тест 6а
    print("\n6a:", find_words_with_consonants("test hello world strong"))
    
    # Тест 7а
    print("\n7a:", check_phones_format("+7(912)345-67-89, +7(999)888-77-66"))
    
    # Тест 8а
    print("\n8a:", find_words_starting_with_consonant("apple banana cat dog"))
    
    # Тест 9а
    print("\n9a:", find_words_with_digits("abc123 def45 ghi6"))
    
    # Тест 10а
    print("\n10a:", check_credit_cards("1234 5678 9012 3456, 1111 2222 3333 4444"))
    
    # Тест 11а
    print("\n11a:", check_all_words_capitalized("Hello World Test"))
    print("11a:", check_all_words_capitalized("Hello world Test"))
    
    # Тест 12а
    print("\n12a:", check_emails_list("test@example.com, user@mail.ru"))
    
    # Тест 13а
    print("\n13a:", find_words_ending_with_ing("testing running walk"))
    
    # Тест 14а
    print("\n14a:", find_words_starting_with_vowel("apple egg ink orange"))
    
    # Тест 15а
    print("\n15a:", find_words_with_vowels("book soon read"))