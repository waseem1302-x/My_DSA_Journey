# O(n²) → Quadratic Time Complexity

""" 
The time taken grows as the square of input size.
If n = 10, ~100 steps.
If n = 1000, ~1,000,000 steps 

"""


# Usually appear in Nested loops → a loop inside another loop.

nums = [1, 2, 3, 4]

for i in nums:
    for j in nums:
        print(i, j)   # n * n → O(n²)



numbers = [5,3,8,4,2]

for i in range(len(numbers)):

    for j in range(len(numbers) - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            print(numbers)
# Every element is compared with every other → O(n²).




num_1 = [1, 2, 3, 4, 2]

for i in range(len(num_1)):
    for j in range(i+1, len(num_1)):
        if num_1[i] == num_1[j]:
            print("Duplicate found:", num_1[i])
