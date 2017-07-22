def m_func(numbers):
    for i in range(0, len(numbers)):
        numbers[i] = (numbers[i] - 1) / 2
    return numbers

numbers = [x for x in range(1, 11)]
numbers = m_func(numbers)
for i in numbers:
    print(i)
