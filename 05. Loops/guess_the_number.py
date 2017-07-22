import random
while True:
    guess = input("Type your guess or n to exit: ")
    if guess == "n":
        break
    rand_num = random.randint(1,10)
    if (int)(guess) == rand_num:
        print("Your guess is correct!")
    else:
        print("Unlucky")
    
    
                  
    
