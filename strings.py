# ─────────────────────────────────────────────
# Problem 1: Greet user with "Good Afternoon"
# ─────────────────────────────────────────────

name = input("Enter your name: ")
print(name + " Good Afternoon")


# ─────────────────────────────────────────────
# Problem 2: Detect double spaces in a string
# ─────────────────────────────────────────────

text = input("Enter a string: ")

if "  " in text:
    print("Double spaces detected in the string.")
else:
    print("No double spaces found.")


# ─────────────────────────────────────────────
# Problem 3: Replace double spaces with single spaces
# ─────────────────────────────────────────────

# Keep replacing until no double spaces remain
while "  " in text:
    text = text.replace("  ", " ")

print("Cleaned string:", text)


# ─────────────────────────────────────────────
# Problem 4: Format letter using escape sequences
# ─────────────────────────────────────────────

letter = "Dear Harry,\n\tThis Python course is nice.\n\tThanks!!"
print(letter)
