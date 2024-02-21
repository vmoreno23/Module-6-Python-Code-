import math

user_factorial = int(input("Which number do you wish to know factorial for?: "))
fact = 1

print("Using 'math.factorial' the factorial of", user_factorial, "is:", math.factorial(user_factorial))

for x in range(1, user_factorial + 1):
    fact = fact * x
print ("The factorial of", user_factorial, "using an alternative method is: ", end="")
print (fact)


#Victor Moreno
#2/20/24


#Problem 6: Use a 'for' statement to calulate the factorial of a user input. Print the value from input and the calculated value using factorial function in the math module.
