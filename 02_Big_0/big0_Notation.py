# -----------------------------------------
# Big O Notation -  Examples
# -----------------------------------------

# O(1) – Constant Time
# No matter how big the list is, this takes 1 step only

def constant_time_example(lst):
    print("O(1) Example:")
    print(lst[0])  # Always one step

constant_time_example([10, 20, 30, 40])


# O(n) – Linear Time
# It runs n times where n is the length of the list
def linear_time_example(lst):
    print("\nO(n) Example:")
    for item in lst:
        print(item)

linear_time_example([10, 20, 30, 40])


# O(n^2) – Quadratic Time
# Nested loops: runs n * n times
def quadratic_time_example(lst):
    print("\nO(n^2) Example:")
    for i in lst:
        for j in lst:
            print(i, j)

quadratic_time_example([1, 2, 3])


# O(log n) – Logarithmic Time
# Binary search cuts the list in half each step

list_01 = [1,3,5,7,9,11,13]
target = 7

def binary_search(list_01, target):
    print("Binary search for target", target)

    low = 0                      # Start of list  .... points to 1
    high = len(list_01) - 1          # End of list ....points to 13

    while low <= high:               # Keep searching until low > high
        mid = (low + high) // 2      # Middle index
        print(f"Checking: {list_01[mid]}")       

        if list_01[mid] == target:
            print("Found!")
            return True
        elif list_01[mid] < target:
            low = mid + 1
        else:
            high = mid - 1


        print("Not found")
    return False

binary_search(list_01, target)