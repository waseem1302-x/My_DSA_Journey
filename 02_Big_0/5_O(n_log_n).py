# The algorithm does some O(log n) work for each of the n elements.
# Total = n × log n.



def merge_sort(arr):

    if len(arr) <= 1:
        return arr
    


    # Step 1: Split the array into two halves

    mid = len(arr) // 2          # O(logn)......level
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Step 2
    return merge(left,right)

def merge(left, right):
    result = []
    i = j = 0


    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])

    return result


nums = [5,3,8,4,2]
print(merge_sort(nums))


""" 
Step 1: Splitting the array
    [5, 3, 8, 4, 2]  
        /        \
    [5, 3]     [8, 4, 2]

    [5, 3] → [5] [3]  
    [8, 4, 2] → [8] [4, 2]  
    [4, 2] → [4] [2]

    end  = [5] [3] [8] [4] [2]


Step 2: Merging the subarrays


    Merge [5] and [3] → [3, 5]
    Merge [4] and [2] → [2, 4]
    Merge [8] and [2, 4] → [2, 4, 8]
    Merge [3, 5] and [2, 4, 8] → [2, 3, 4, 5, 8] Final

"""