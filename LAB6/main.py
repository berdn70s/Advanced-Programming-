import math

n = int(input("Enter the value of n: "))
x = int(input("Enter the value of x: "))

denominators = list(map(lambda i: math.factorial(i), range(x+1)))

numerators = list(map(lambda i: n**i, range(x+1)))

result = sum(list(map(lambda i, j: i/j, numerators, denominators)))

print(f"e = {result}")
print('here is 2nd question\n')
def recursive_function(n):


    global result2

    if n == 0:
        return

    recursive_function(n-1)
    result2 += n * ((-1)**(n+1))

result2 = 0

n = int(input("Enter the value of n: "))

recursive_function(n)

print(f"The sum of the given equation for the range of k from 1 to {n} is: {result2}")
