# 🧠 LeetCode + DSA Practice in Python

Hi, I’m **Waseem Mushtaq** 👋
This repo contains my daily practice of **Data Structures & Algorithms (DSA)** using Python, with problems mainly from **LeetCode**, organized by topic and readiness level.

My goal is to build a strong foundation and prepare for top tech interviews (MAANG, remote jobs, internships).

---

## 📍 Pre DSA — Why `01_Pre_DSA` Exists

Before jumping into core DSA topics, I created `01_Pre_DSA` to **solidify Python fundamentals, problem decomposition, and basic patterns**. This prevents syntax and small logic mistakes from slowing down learning when I start real DSA problems (arrays, linked lists, trees, graphs).

**Goals of Pre DSA**

* Strengthen loops, conditions, functions, and basic data structure usage.
* Build confidence solving beginner algorithmic problems.
* Practice writing clean, testable Python code.
* Start thinking about complexity (Big O) in small examples.

---

## ✅ Progress

| Topic / Folder  | Problems Solved | Last Updated |
| --------------- | --------------: | -----------: |
| 01\_Pre\_DSA    |               0 |            - |
| 02\_Big\_O      |               0 |            - |
| 03\_Arrays      |               0 |            - |
| 04\_Strings     |               0 |            - |
| 05\_LinkedLists |               0 |            - |
| 06\_Trees       |               0 |            - |
| 07\_Graphs      |               0 |            - |

---

## 🗂️ Folder Structure (Corrected)

```
My_DSA_Journey/
├── 01_Pre_DSA/
│   ├── 01_Simple_Logic_Problems/
│   │   ├── fizzbuzz.py
│   │   ├── palindrome.py
│   │   ├── fibonacci.py
│   │   ├── factorial.py
│   │   └── prime_check.py
│   │
│   ├── 02_List_String_Problems/
│   │   ├── reverse_string_list.py
│   │   ├── find_max_min.py
│   │   ├── count_vowels.py
│   │   ├── remove_duplicates.py
│   │   └── merge_sorted_lists.py
│   │
│   ├── 03_Dict_Set_Practice/
│   │   ├── word_frequency.py
│   │   ├── first_non_repeating_char.py
│   │   ├── set_operations.py
│   │   └── lists_to_dict.py
│   │
│   └── 04_Loop_Condition_Challenges/
│       ├── sum_of_digits.py
│       ├── multiplication_table.py
│       ├── number_patterns.py
│       └── armstrong_number.py
│
├── 02_Big_O/
├── 03_Arrays/
├── 04_Strings/
├── 05_LinkedLists/
├── 06_Trees/
├── 07_Graphs/
└── README.md
```

---

## 📌 How Each File Should Be Structured

Each problem file should include the following sections at the top (as comments or docstring):

1. **Problem Summary** — 1–2 line description (source, expected input/output).
2. **Approach** — brief explanation / steps in plain language.
3. **Time & Space Complexity** — Big O analysis.
4. **Implementation** — final Python code, with a `main` test block or simple asserts.
5. **Example Tests** — a few representative test cases as comments or `assert` statements.

Example skeleton for `fizzbuzz.py`:

```python
"""
Problem: FizzBuzz
Input: integer n
Output: print numbers 1..n with Fizz/Buzz rules

Approach:
- Loop from 1..n, check divisibility by 3 and 5, print accordingly.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == "__main__":
    fizzbuzz(15)
```

---

## 🚀 Repo Goals & Workflow

* [ ] Complete `01_Pre_DSA` and ensure fluency in Python basics.
* [ ] Move to `02_Big_O`, then `03_Arrays`, `04_Strings`, and so on.
* [ ] For each topic, aim to: Understand → Implement → Analyze → Refactor.
* [ ] Push solutions with clear READMEs and problem notes for revision.

---

## 🛠 Tech Stack

* Python 3.x
* Git & GitHub
* LeetCode (primary problem source)

---

## ✍️ Contact

**Waseem Mushtaq**
[GitHub](https://github.com/waseem1302-x) | [LinkedIn](https://www.linkedin.com/in/waseem-mushtaq-1302-x/)
