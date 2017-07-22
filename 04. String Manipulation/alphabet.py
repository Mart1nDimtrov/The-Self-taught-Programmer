alphabet = "qwertyuiopasdfghjklzxcvbnm"
print(alphabet)

for c in alphabet:
    print(c)

alphabet = "+".join(alphabet)
print(alphabet)
print(alphabet.split("+"))
print("a" in alphabet)
print("-".join("abc" * 3))
