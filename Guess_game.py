import random
print("Wecome to Guess game...!\nGuess a number in 1-100")

correct_number=random.randint(1,100)

guess_number=int(input("Guess your number:\n"))

guess_count=0

while guess_number != correct_number:
    guess_count +=1
    if guess_number<correct_number:
       guess_number=int(input("Wrong..! Guess your number higher..:\n"))
    else:
        guess_number=int(input("Wrong..! Guess your number lower..:\n"))
   
print(f"Congratulatio..!, your guess is correct, The number is {correct_number}")    