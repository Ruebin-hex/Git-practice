def factorial_recursive(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    
    if n == 0 or n == 1:
        return 1
        
    return n * factorial_recursive(n - 1)

number = input("Enter a number: ")
print("--- Calculating Factorial for" + number+"!---")
print(factorial_recursive(number))
print("I was also here")