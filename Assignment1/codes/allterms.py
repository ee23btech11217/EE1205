import math

def x_n(n):
    if n <= 0:
        return 0
    else:
        return (-1) / math.factorial(n)

# Get N from the user
print("//This program will generate the terms of the sequence upto x(n)// \n")
N = int(input("Enter the value of n: "))

# Generate the sequence up to N

print("...\nx( -1 ) = 0\n")
for x in range(N+1):
    {    
        print("x(", x, ") = ", x_n(x), "\n")
    }
print("...")

