arr = [1,3,5,7,9,12]
target = 12

def two_pointers(arr):

    left = 0                 
    right = len(arr) - 1      

    while left < right:      
        curr_sum = arr[left] + arr[right]

        if curr_sum == target:
            return True 
        elif curr_sum < target:
            left += 1    # need a bigger sum → move left forward
        else:
            right -= 1   # need a smaller sum → move right backward

    return False  # no pair found


print(two_pointers(arr))


