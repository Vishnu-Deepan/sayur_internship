# 1.Write a program for Collatz_conjecture.
# Collatz_conjecture means -  start with the input number. 
# For even number , divide by 2 (n/2)
# For odd number - 3n + 1
# apply the above for the resulting number until the answer is 1.Eg, input is 8
# output 8, 4,2, 1
# input is 9
# output 9,28,14,7,22,11,34,17,52,26,13,40,20,10,5,16,8,4,2,1
# Get two numbers as input. Print the number that has less number of steps to reach 1.


#SOLUTION
def collatz_conjecture(n):
    steps = 0
    
    while n != 1:
        print(n, end=", ")
        
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        
        steps += 1
    
    print(1)  # Print the 1 finally
    return steps

# getting input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

steps1 = collatz_conjecture(num1)
steps2 = collatz_conjecture(num2)

# Printing the number with fewer steps
if steps1 < steps2:
    print(f"{num1} has fewer steps ({steps1}) to reach 1.")
elif steps2 < steps1:
    print(f"{num2} has fewer steps ({steps2}) to reach 1.")
else:
    print(f"{num1} and {num2} have the same number of steps ({steps1}).")

# Sample Outputs:
# Enter the first number: 8
# Enter the second number: 9
# 8, 4, 2, 1
# 9, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1
# 8 has fewer steps (3) to reach 1.
