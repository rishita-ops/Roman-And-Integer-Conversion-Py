"""
Roman ↔ Integer Converter
==========================

Problem 1 — Roman to Integer  (LeetCode #13 | Easy)
Problem 2 — Integer to Roman  (LeetCode #12 | Medium)

Symbols & Values:
    I=1, V=5, X=10, L=50, C=100, D=500, M=1000

Subtraction Rule (Roman → Integer):
    If a symbol is SMALLER than the symbol to its RIGHT → subtract it.
    Otherwise → add it.

Greedy Rule (Integer → Roman):
    At each step, pick the largest symbol that fits into the remaining value.
    Repeat until the value reaches 0.

Time  : O(n) for both
Space : O(1) — fixed-size lookup tables
"""


# ─────────────────────────────────────────────
#  Problem 1 — Roman to Integer
# ─────────────────────────────────────────────

def roman_to_int(s: str) -> int:
    roman = {
        'I': 1, 'V': 5,  'X': 10,
        'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    for i in range(len(s)):
        current  = roman[s[i]]
        next_val = roman[s[i + 1]] if i + 1 < len(s) else 0

        # Core rule: smaller before larger → subtract, else → add
        total += -current if current < next_val else current

    return total


# ─────────────────────────────────────────────
#  Problem 2 — Integer to Roman
# ─────────────────────────────────────────────

def int_to_roman(num: int) -> str:
    # Values paired with symbols in descending order (including subtraction pairs)
    val_sym = [
        (1000, "M"),  (900, "CM"), (500, "D"),  (400, "CD"),
        (100,  "C"),  (90,  "XC"), (50,  "L"),  (40,  "XL"),
        (10,   "X"),  (9,   "IX"), (5,   "V"),  (4,   "IV"),
        (1,    "I"),
    ]

    result = ""
    for value, symbol in val_sym:
        while num >= value:
            result += symbol
            num    -= value

    return result


# ─────────────────────────────────────────────
#  Interactive Menu
# ─────────────────────────────────────────────

def main():
    print("\n╔══════════════════════════════════╗")
    print("║    Roman ↔ Integer Converter     ║")
    print("╚══════════════════════════════════╝")

    while True:
        print("\n  1 → Roman  to Integer")
        print("  2 → Integer to Roman")
        print("  0 → Exit")
        choice = input("\nYour choice: ").strip()

        if choice == "1":
            s = input("Enter Roman numeral: ").strip().upper()
            print(f"\n  {s}  →  {roman_to_int(s)}")

        elif choice == "2":
            try:
                n = int(input("Enter integer (1 – 3999): ").strip())
                if not (1 <= n <= 3999):
                    print("  ⚠️  Please enter a number between 1 and 3999.")
                else:
                    print(f"\n  {n}  →  {int_to_roman(n)}")
            except ValueError:
                print("  ⚠️  Invalid input. Please enter a valid integer.")

        elif choice == "0":
            print("\n  Goodbye! 👋\n")
            break

        else:
            print("  ⚠️  Invalid choice. Please enter 1, 2, or 0.")


if __name__ == "__main__":
    main()