""" 
    What does O(n) mean?

    The time taken grows directly with input size n.

    If you have 10 items → ~10 steps.

    If you have 1,000 items → ~1,000 steps.

    Think of reading a book: the more pages (n), the more time it takes. 
"""

# Traversing a list
nums = [10, 20, 30, 40, 50]
for num in nums:
    print(num)   # Runs n times → O(n)


# 2. Searching in an unsorted list (Linear Search)

nums = [3, 8, 2, 7, 5]
target = 7

found = False
for num in nums:
    if num == target:
        found = True
        break
print(num)
# Worst case → O(n) (if element is at end or not present)


# Rule of Thumb:  Whenever you see a single loop over all elements → O(n).