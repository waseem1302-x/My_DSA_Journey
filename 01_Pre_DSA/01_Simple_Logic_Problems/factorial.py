# Factorial of a number
# Iterative: multiply from 1 to n
# Example: n = 5 -> 120
# Time Complexity: Iterative O(n), Recursive O(n)

n = int(input("Enter Number: "))
result = 1
for i in range(1, n + 1):
    result  = result * i
print(result)