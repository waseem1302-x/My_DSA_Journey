# Factorial of a number
# Iterative: multiply from 1 to n
# Recursive: factorial(n) = n * factorial(n-1)
# Example: n = 5 -> 120
# Time Complexity: Iterative O(n), Recursive O(n)

n = 5
result = 1
for i in range(1, n + 1):
    result  = result * i
print(result)


# recursive approach

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))
