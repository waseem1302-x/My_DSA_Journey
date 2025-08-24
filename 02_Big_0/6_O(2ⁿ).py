# Time doubles every time we increase the input size by 1.


""" 

    n = 1 → ~2 operations
    n = 2 → ~4 operations
    n = 3 → ~8 operations
    n = 10 → ~1024 operations
    n = 20 → ~1,048,576 operations

"""


def subsets(nums):
    result = []

    def backtrack(i, path):
        # Trace: show depth i and current path
        print(f"i={i}, path={path}")

        # Base case: decided for all elements
        if i == len(nums):
            result.append(path[:])  # copy current subset
            print(f"  leaf -> add {path[:]}")
            return

        # Choice 1: EXCLUDE nums[i]
        backtrack(i + 1, path)

        # Choice 2: INCLUDE nums[i]
        path.append(nums[i])
        backtrack(i + 1, path)
        path.pop()  # undo (backtrack)

    backtrack(0, [])
    return result

subsets([1, 2, 3])

"""  
    Level 0:              []                (start, empty set)
                    /            \
    Level 1:    []                   [1]           (exclude 1, include 1)
                / \                /     \
    Level 2:    []  [2]           [1]     [1,2]        (decision on 2)
                / \   / \         / \     /   \
    Level 3:  [] [3] [2] [2,3] [1] [1,3] [1,2] [1,2,3]   (decision on 3)


"""