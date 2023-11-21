import random
import math

while True:
    
   lower_bound = input("Enter a lower bound ")
   if not lower_bound.isdigit():
    print("Please enter a number.")
   else:
    lower_bound = int(lower_bound)
   
   upper_bound = input("Enter an upper bound ")
   if not upper_bound.isdigit():
    print("Please enter a number.")
   else:
    upper_bound = int(upper_bound) 
    break

x = random.randint(lower_bound,upper_bound)
print("\n\tYou've only ", 
      round(math.log(upper_bound-lower_bound + 1, 2)),
      " chances to guess the integer!\n")

# Initializing the number of guesses.
count = 0

# for calcultion of minimum number of 
# guesses dependes upon range

while count < math.log(upper_bound - lower_bound + 1, 2):
    count += 1
    
    # take the guess number from user
    guess = int(input("Guess a number:"))
    
    # Condition testing
    if x == guess:
        print("Congratulations you did it in ",
              count, "try")
        
        break
    elif x > guess:
        print("You guessed too small!")
        
    elif x < guess:
        print("You guessed too high!") 
        
     #If guessing is more than required guesses, show this output.
     
if count >= math.log(upper_bound -lower_bound + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")  