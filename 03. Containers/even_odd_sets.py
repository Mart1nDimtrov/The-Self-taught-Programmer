odd_set = {x for x in range(1, 11, 2)}
print(odd_set)
even_set = {x for x in range(2, 11, 2)}
print(even_set)
print(odd_set | even_set)
print(odd_set & even_set)
print(odd_set - even_set)
print(even_set - odd_set)
