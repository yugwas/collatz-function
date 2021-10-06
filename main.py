
def collatz(number):
    print("Collatz sequence for", user_input)
    while number != 1:
        if number % 2 == 1:
            number = 3 * number + 1
            print(number)
        elif number % 2 == 0:
            number = (number//2)
            print(number)
        else:
            print("Enter a valid input.")
        continue

user_input = input("Please enter an integer: ")
user_input = collatz(int(user_input))


'''The output of this program could look something like this:

Enter number:  (if 3 is what is entered...)
3  
10  
5  
16  
8  
4  
2  
1  
'''