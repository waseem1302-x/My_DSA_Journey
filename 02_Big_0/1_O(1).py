# -----------------------------------------
# Big O Notation -  Examples
# -----------------------------------------

# O(1) – Constant Time
# Operation takes the same amount of time, no matter how big the input is.

# O(1) is the fastest complexity possible.

def constant_time_example(lst):
    print("O(1) Example:")
    print(lst[0])  # Always one step

constant_time_example([10, 20, 30, 40])

# Example 2
nums = [10,20,30,40]
print(nums[1])
print(nums[3])   # still one step, no matter how large list is


# Dictionary (Hash Map) lookup

students = {"Alice": 85, "Bob": 90, "Charlie": 78}
print(students["Bob"])   # O(1) → direct access by key



# Set membership test

myset = {1, 2, 3, 4, 5}
print(3 in myset)   # O(1), hash lookup





""" 
When is O(1) useful?
Fast lookups in arrays, dicts, sets.
Stack & Queue operations (push, pop, enqueue, dequeue).
Hashing (e.g., password checks, caching). 

"""
