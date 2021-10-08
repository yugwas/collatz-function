
def collatz(number):
    if number % 2 == 0:
        number = (number//2)
        print(number)
        return number
    elif number == 0:
        print("You cannot get the collatz of 0!")
    else:
        number = 3 * number + 1
        print(number)
        return number


print("Please enter an integer to get the collatz sequecne for it:  " )
try:
    user_input = int(input())
    while user_input != 1:
        user_input = collatz(user_input)
except ValueError:  
    print("Invalid argument! Please enter an integer.")
