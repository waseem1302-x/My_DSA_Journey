# 📘 Week 1 DSA Notes — Arrays (Binary Search + Two Pointers)

---

## 🔹 1. Problem-Solving Mindset

Whenever face a problem:

1. **Understand the problem** – restate in your own words.
2. **Think brute force** – how would I solve it slowly (nested loops)?
3. **Dry run** – test small input on paper.
4. **Optimize** – Can I use sorted property? Can I avoid nested loop?
5. **Code** – Write clean, structured solution.
6. **Check edge cases** – empty array, single element, duplicates, large inputs.

---

## 🔹 2. Binary Search — Core Pattern

* **When to use?** Sorted arrays or monotonic condition.
* **Goal?** Cut search space in half each step.
* **Key Loop Condition:** `while left <= right`

### Pattern Code

```python
left, right = 0, len(nums) - 1
while left <= right:
    mid = (left + right) // 2
    
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```

### Important Points:

* Use `<=`, not `<`, else last element may be skipped.
* `mid = (left + right) // 2` (Python handles overflow).
* Edge case: return `left` if inserting position.

### Problems Learned:

* **35. Search Insert Position** → insert location if not found.
* **704. Binary Search** → standard template.
* **278. First Bad Version** → use binary search on a boolean condition.
* **69. Sqrt(x)** → binary search on answer.
* **34. Find First & Last Position** → binary search variant to find boundaries.
* **33. Search in Rotated Sorted Array** → tricky conditions, check which half is sorted.

---

## 🔹 3. Two Pointers — Core Pattern

* **When to use?** Sorted arrays, reversing, palindromes, partitioning.
* **Goal?** Reduce complexity from O(n²) → O(n).
* **Key Loop Condition:** `while left < right`

### Pattern Code

```python
left, right = 0, len(nums) - 1
while left < right:
    if condition:
        left += 1
    else:
        right -= 1
```

### Important Points:

* Always check duplicates (skip them when needed).
* Careful with string reversal or palindrome check.
* Move pointers based on problem logic:

  * **Shrink window** → palindrome check.
  * **Expand/Shrink** → container water, two sum.

### Problems Learned:

* **167. Two Sum II** → move left/right depending on sum.
* **977. Squares of a Sorted Array** → compare absolute values.
* **344. Reverse String** → swap characters until middle.
* **125. Valid Palindrome** → ignore non-alphanumeric, compare left/right.
* **283. Move Zeroes** → in-place shift using slow/fast pointers.
* **11. Container With Most Water** → always move pointer with smaller height.

---

## 🔹 4. Brute Force → Optimized Thinking

* **Brute Force:**

  * Try every possibility (nested loop).
  * Good for clarity but bad for large inputs.
* **Dry Run:**

  * Write 1–2 examples.
  * Track pointer movements step by step.
* **Optimized:**

  * Ask: "Do I really need nested loops?"
  * Use sorted property, binary search, or two pointers.

---

## 🔹 5. Edge Cases to Always Test

* Empty array: `[]`
* Single element: `[1]`
* Target not found: `[1,3,5], target=2`
* All duplicates: `[2,2,2,2]`
* Negative numbers included.

---

## 🔹 6. Your 12 Problems → Lessons

| Problem                               | Technique     | Key Learning                  |
| ------------------------------------- | ------------- | ----------------------------- |
| 35. Search Insert Position            | Binary Search | Insert position handling      |
| 704. Binary Search                    | Binary Search | Basic template                |
| 278. First Bad Version                | Binary Search | Condition-based search        |
| 69. Sqrt(x)                           | Binary Search | Answer approximation          |
| 34. Find First/Last Position          | Binary Search | Boundary search               |
| 33. Rotated Sorted Array              | Binary Search | Check which half is sorted    |
| 81. Search in Rotated Sorted Array II | Binary Search | Handle duplicates             |
| 167. Two Sum II                       | Two Pointers  | Sorted array sum check        |
| 977. Squares of Sorted Array          | Two Pointers  | Compare absolute values       |
| 344. Reverse String                   | Two Pointers  | Swapping characters           |
| 125. Valid Palindrome                 | Two Pointers  | Ignore non-alphanumeric chars |
| 283. Move Zeroes                      | Two Pointers  | In-place shifting of zeros    |
| 11. Container With Most Water         | Two Pointers  | Max area logic                |
| 15. 3Sum                              | Two Pointers  | Sorting + pair sum logic      |


---

## 🔹 7. Quick Practice Tasks

* Re-implement Binary Search **without looking**.
* Dry run `nums = [5,6,7,1,2,3,4]` (rotated array) for target = 3.
* Code palindrome check from scratch.
* Move Zeroes: test `[0,1,0,3,12]`.

---