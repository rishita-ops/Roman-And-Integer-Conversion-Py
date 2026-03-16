# 🏛️ Roman to Integer

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![C++](https://img.shields.io/badge/C++-17-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-String%20%7C%20HashMap-blueviolet?style=for-the-badge)
![LeetCode](https://img.shields.io/badge/LeetCode-%23000000.svg?style=for-the-badge&logo=LeetCode&logoColor=#d16c06)

> Convert a Roman numeral string into its integer equivalent using a single elegant rule — no special casing needed.

---

## 📌 Problem Statement

Roman numerals are represented by 7 symbols:

| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

Numerals are written **largest to smallest, left to right** — except in 6 subtraction cases:

| Numeral | Value |
|---------|-------|
| IV      | 4     |
| IX      | 9     |
| XL      | 40    |
| XC      | 90    |
| CD      | 400   |
| CM      | 900   |

**Given** a roman numeral string `s`, return its integer value.

---

## 🧠 The Core Insight

> You don't need to hardcode any of the 6 subtraction cases.

One rule handles everything:

```
If current symbol < next symbol  →  SUBTRACT it
If current symbol >= next symbol →  ADD it
```

That's it. The entire problem reduces to **one comparison per character**.

---

## 📖 Walkthrough Example

**`MCMXCIV` = 1994**

```
M  → next is C  (1000 > 100)  → ADD    1000   | running total: 1000
C  → next is M  ( 100 < 1000) → SUB     100   | running total:  900
M  → next is X  (1000 > 10)   → ADD    1000   | running total: 1900
X  → next is C  (  10 < 100)  → SUB      10   | running total: 1890
C  → next is I  ( 100 > 1)    → ADD     100   | running total: 1990
I  → next is V  (   1 < 5)    → SUB       1   | running total: 1989
V  → no next                  → ADD       5   | running total: 1994 ✅
```

---

## 💻 Implementations

This repo provides solutions in **two languages** — same logic, different syntax flavors.

### 🐍 Python — `solution.py`

Uses a dictionary for the symbol map and clean loop logic.

```python
def roman_to_int(s: str) -> int:
    roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    total = 0
    for i in range(len(s)):
        current  = roman[s[i]]
        next_val = roman[s[i+1]] if i+1 < len(s) else 0
        total += -current if current < next_val else current
    return total
```

### ⚙️ C++ — `solution.cpp`

Uses `unordered_map<char, int>` for O(1) lookups and structured test output.

```cpp
int romanToInt(const std::string& s) {
    unordered_map<char,int> roman = {
        {'I',1},{'V',5},{'X',10},{'L',50},{'C',100},{'D',500},{'M',1000}
    };
    int total = 0;
    for (int i = 0; i < s.size(); i++) {
        int cur  = roman[s[i]];
        int next = (i+1 < s.size()) ? roman[s[i+1]] : 0;
        total += (cur < next) ? -cur : cur;
    }
    return total;
}
```

---

## 📊 Complexity Analysis

| Metric           | Value  | Note                              |
|------------------|--------|-----------------------------------|
| Time Complexity  | O(n)   | Single pass through the string    |
| Space Complexity | O(1)   | HashMap has fixed 7 entries only  |

---

## 🧪 Test Cases

| Input        | Expected | Note                    |
|--------------|----------|-------------------------|
| `"I"`        | 1        | Single symbol           |
| `"IV"`       | 4        | I before V → subtract   |
| `"IX"`       | 9        | I before X → subtract   |
| `"LVIII"`    | 58       | L + V + III             |
| `"MCMXCIV"`  | 1994     | Classic complex case    |
| `"MMMCMXCIX"`| 3999     | Maximum roman numeral   |

---

## 🚀 How to Run

### Python
```bash
python solution.py
```

### C++
```bash
# Compile
g++ -std=c++17 -o solution solution.cpp

# Run
./solution
```

**Expected output (both languages):**
```
=================================================================
Input           Expected     Got          Pass?
=================================================================
I               1            1            ✅  Single symbol
II              2            2            ✅  Repeated symbol
IV              4            4            ✅  Subtraction: I before V
...
=================================================================
Results: 14/14 passed
```

---

## 🔍 Why No Special Casing?

Most people's first instinct is to explicitly handle `IV`, `IX`, `XL`, etc. But the **look-ahead rule** makes this unnecessary:

```
IV → I(1) < V(5) → subtract 1 → 5 - 1 = 4 ✅
CM → C(100) < M(1000) → subtract 100 → 1000 - 100 = 900 ✅
```

The pattern self-emerges from the structure of Roman numerals — no hardcoding needed.

---

## 📁 File Structure

```
📦 roman-to-integer
 ┣ 📜 solution.py       # Python solution + test runner
 ┣ 📜 solution.cpp      # C++ solution + test runner
 ┗ 📜 README.md         # You are here
```

---

## 🔗 Related Problems

| Problem | Difficulty | Link |
|---------|------------|------|
| Integer to Roman | Medium | LeetCode #12 |
| Regular Expression Matching | Hard | LeetCode #10 |

---

## 🙋 Author

Made with 🏛️ and an appreciation for ancient number systems.

If this helped you, drop a ⭐ — it means a lot!
