def generate_string(s, k):
    # Сначала посчитаем минимальную и максимальную длину строки
    min_len = 0  # минимальная длина
    max_len = 0  # максимальная длина
    result = []  # итоговая строка

    # Пройдем по строке и учтем звездочки и вопросительные знаки
    i = 0
    while i < len(s):
        if i + 1 < len(s) and s[i + 1] in ['*', '?']:
            if s[i + 1] == '?':
                min_len += 0  # этот символ можно удалить
                max_len += 1  # или оставить один раз
                result.append(s[i])  # добавим символ как кандидат
            elif s[i + 1] == '*':
                min_len += 0  # этот символ можно удалить
                max_len += 200  # можно добавить сколько угодно раз (до лимита длины строки)
                result.append(s[i])  # добавим символ как кандидат
            i += 2  # пропускаем символ и модификатор
        else:
            min_len += 1  # если это обычный символ
            max_len += 1
            result.append(s[i])  # добавляем его в результат
            i += 1

    # Проверим, может ли строка быть длины k
    if k < min_len or k > max_len:
        return "Impossible"

    # Теперь попробуем построить строку длины k
    output = []
    current_len = 0

    for i in range(len(result)):
        if i + 1 < len(s) and s[i + 1] == '*':
            if current_len < k:
                # Добавляем столько символов, сколько нужно для достижения длины k
                needed = k - current_len
                output.append(result[i] * needed)
                current_len += needed
            i += 1  # Пропускаем символ и '*'
        elif i + 1 < len(s) and s[i + 1] == '?':
            if current_len < k:
                output.append(result[i])  # Оставляем символ
                current_len += 1
            # Если не нужно добавлять символ, просто пропускаем
            i += 1  # Пропускаем символ и '?'
        else:
            output.append(result[i])
            current_len += 1

    return ''.join(output)


# Пример использования:
s = input()  # Ввод строки с модификаторами
k = int(input())  # Ввод длины строки
print(generate_string(s, k))
