import prime_numbers, odd_numbers, even_numbers

for i in range(1, 101):
    if prime_numbers.check_prime(i):
        if odd_numbers.check_odd(i):
            print(str(i) + " is both a prime and an odd number")
        elif even_numbers.check_even(i):
            print(str(i) + " is both a prime and an even number")
    else:
         if odd_numbers.check_odd(i):
            print(str(i) + " is an odd number")
         elif even_numbers.check_even(i):
            print(str(i) + " is an even number")
        
    
   
