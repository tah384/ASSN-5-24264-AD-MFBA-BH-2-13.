# =============================================================================
# Chapter 5 - Practice Set: Sets and Dictionaries
# Topic  : Python Sets and Dictionaries
# =============================================================================


# -----------------------------------------------------------------------------
# Question 1
# Write a program to create a dictionary of Hindi words with values as their
# English translation. Provide user with an option to look it up.
# -----------------------------------------------------------------------------

def q1_hindi_dictionary():
    """
    Builds a static Hindi-to-English dictionary and allows the user to
    look up the English translation of any Hindi word.
    """

    # Predefined dictionary: Hindi word (key) -> English translation (value)
    hindi_dict = {
        "नमस्ते"   : "Hello",
        "धन्यवाद"  : "Thank you",
        "पानी"     : "Water",
        "खाना"     : "Food",
        "घर"       : "Home",
        "किताब"    : "Book",
        "दोस्त"    : "Friend",
        "स्कूल"    : "School",
        "समय"      : "Time",
        "रात"      : "Night"
    }

    print("\n--- Question 1: Hindi Dictionary Lookup ---")
    print("Available Hindi words:", list(hindi_dict.keys()))

    word = input("\nEnter a Hindi word to look up: ").strip()

    # Check if the entered word exists as a key in the dictionary
    if word in hindi_dict:
        print(f"English translation of '{word}': {hindi_dict[word]}")
    else:
        print("Word not found in the dictionary.")


# -----------------------------------------------------------------------------
# Question 2
# Write a program to input eight numbers from the user and display all the
# unique numbers (once each).
# -----------------------------------------------------------------------------

def q2_unique_numbers():
    """
    Accepts 8 numbers from the user and displays only the unique values.
    A set is used because it automatically discards duplicate entries.
    """

    print("\n--- Question 2: Display Unique Numbers ---")

    unique_numbers = set()   # Set stores only unique values automatically

    for i in range(1, 9):
        num = int(input(f"Enter number {i}: "))
        unique_numbers.add(num)

    print("Unique numbers entered:", unique_numbers)


# -----------------------------------------------------------------------------
# Question 3
# Can we have a set with 18 (int) and "18" (str) as values in it?
# -----------------------------------------------------------------------------

def q3_int_and_str_in_set():
    """
    Demonstrates that a set can hold 18 (int) and "18" (str) simultaneously.
    They are considered distinct because they have different types and
    different hash values even though they look similar.
    """

    print("\n--- Question 3: int and str as Set Members ---")

    sample_set = {18, "18"}

    print("Set contents :", sample_set)
    print("Length of set:", len(sample_set))

    # Explanation
    print("\nExplanation:")
    print("  18 (int) and '18' (str) are different objects with different hash values.")
    print("  Therefore Python treats them as two separate elements in a set.")
    print("  Answer: YES, a set can hold both 18 (int) and '18' (str) at the same time.")


# -----------------------------------------------------------------------------
# Question 4
# What will be the length of the following set S after these operations?
#   S = set()
#   S.add(20)
#   S.add(20.0)
#   S.add("20")
# -----------------------------------------------------------------------------

def q4_set_length_after_operations():
    """
    Demonstrates the length of a set after adding 20, 20.0, and "20".

    Key concept:
    - 20 (int) and 20.0 (float) are considered EQUAL in Python (20 == 20.0 is True)
      and they share the same hash value, so the set treats them as the same element.
    - "20" (str) is a completely different type, so it is stored separately.
    - Final length = 2  (one slot for 20/20.0, one slot for "20")
    """

    print("\n--- Question 4: Set Length After add() Operations ---")

    S = set()
    S.add(20)      # S = {20}
    S.add(20.0)    # 20.0 == 20, same hash -> duplicate, not added again
    S.add("20")    # "20" is a string, different hash -> added as new element

    print("Set S after all operations:", S)
    print("Length of S:", len(S))

    print("\nExplanation:")
    print("  20 (int) and 20.0 (float) are equal in Python (20 == 20.0 is True).")
    print("  They also have the same hash, so the set does not store 20.0 separately.")
    print("  '20' (str) is a different type with a different hash -> stored separately.")
    print("  Final length = 2")


# -----------------------------------------------------------------------------
# Question 5
# S = {3}  -- What is the type of S?
# -----------------------------------------------------------------------------

def q5_type_of_set():
    """
    Shows the type of the variable S when it is assigned {3}.
    {3} is a set literal containing one element, not an integer or a dict.
    Note: {} alone (empty braces) creates a dict, but {3} creates a set.
    """

    print("\n--- Question 5: Type of S = {3} ---")

    S = {3}

    print("S =", S)
    print("type(S) =", type(S))

    print("\nExplanation:")
    print("  {3} is a set literal containing the integer 3.")
    print("  {} (empty braces) creates a dict, but {value} creates a set.")
    print("  Therefore type(S) is <class 'set'>.")


# -----------------------------------------------------------------------------
# Question 6
# Create an empty dictionary. Allow 4 friends to enter their favourite
# language as values and use keys as their names.
# Assume that the names are unique.
# -----------------------------------------------------------------------------

def q6_friends_language_dict():
    """
    Builds a dictionary where each of 4 friends provides:
      - Key   : their name  (assumed unique)
      - Value : their favourite programming language

    Returns the dictionary for use in Questions 7 and 8.
    """

    print("\n--- Question 6: Friends and Favourite Languages ---")

    friends = {}   # Start with an empty dictionary

    for i in range(1, 5):
        name     = input(f"Enter name of friend {i}: ").strip()
        language = input(f"Enter favourite language of {name}: ").strip()
        friends[name] = language   # name is the key, language is the value

    print("\nFriends dictionary:", friends)
    return friends


# -----------------------------------------------------------------------------
# Question 7
# If names of 2 friends are the same, what will happen to the program
# in Question 6?
# -----------------------------------------------------------------------------

def q7_duplicate_names():
    """
    Explains and demonstrates what happens when two friends share the same name
    while building the dictionary from Question 6.

    Since dictionary keys must be unique, the second entry with the same name
    overwrites (replaces) the first entry. The first friend's language is lost.
    """

    print("\n--- Question 7: Duplicate Names in Dictionary ---")

    friends = {}
    friends["Ali"] = "Python"   # First entry for key "Ali"
    friends["Ali"] = "Java"     # Second entry for the same key -> overwrites the first

    print("Dictionary after adding 'Ali' twice:", friends)

    print("\nExplanation:")
    print("  Dictionary keys must be unique.")
    print("  When the same name (key) is added a second time, the new value")
    print("  replaces (overwrites) the old value.")
    print("  The first friend's favourite language 'Python' is lost.")
    print("  Only the latest entry 'Java' is retained.")


# -----------------------------------------------------------------------------
# Question 8
# If languages of two friends are the same, what will happen to the program
# in Question 6?
# -----------------------------------------------------------------------------

def q8_duplicate_languages():
    """
    Explains and demonstrates what happens when two friends share the same
    favourite language in the dictionary from Question 6.

    Dictionary VALUES do not need to be unique. Only KEYS must be unique.
    Therefore, two different names (keys) can map to the same language (value)
    without any issue.
    """

    print("\n--- Question 8: Duplicate Languages in Dictionary ---")

    friends = {
        "Ali"  : "Python",
        "Sara" : "Python",   # Same language as Ali -> perfectly valid
        "Umar" : "Java",
        "Zara" : "C++"
    }

    print("Dictionary with duplicate language values:", friends)

    print("\nExplanation:")
    print("  Dictionary VALUES are allowed to repeat.")
    print("  Only KEYS (names) must be unique.")
    print("  Having two friends with the same favourite language causes NO error.")
    print("  Both entries are stored and accessible independently.")


# -----------------------------------------------------------------------------
# Question 9
# Can you change the values inside a list which is contained in a Set?
#   S = {8, 7, 12, "Harry", [1, 2]}
# -----------------------------------------------------------------------------

def q9_list_inside_set():
    """
    Explains why a list CANNOT be stored inside a set, and whether its
    contents could be modified if it somehow were stored.

    Sets require all their elements to be HASHABLE (immutable).
    Lists are mutable and therefore NOT hashable.
    Attempting to add a list to a set raises a TypeError.

    If immutability is needed inside a set, a TUPLE should be used instead.
    Tuples are hashable and immutable, so their contents cannot be changed.
    """

    print("\n--- Question 9: List Inside a Set ---")

    # Attempt to create a set containing a list (this will raise TypeError)
    print("Attempting: S = {8, 7, 12, 'Harry', [1, 2]}")
    try:
        S = {8, 7, 12, "Harry", [1, 2]}
    except TypeError as error:
        print(f"  TypeError raised: {error}")

    print("\nExplanation:")
    print("  A set can only contain HASHABLE (immutable) elements.")
    print("  Lists are mutable and therefore unhashable.")
    print("  Python raises TypeError: unhashable type: 'list'")
    print("  The set {8, 7, 12, 'Harry', [1, 2]} cannot be created.")

    # Correct approach: use a tuple instead of a list
    S_correct = {8, 7, 12, "Harry", (1, 2)}
    print("\nCorrect approach using a tuple instead of a list:")
    print("  S =", S_correct)

    print("\nCan you change the values inside the tuple inside the set?")
    print("  NO. Tuples are immutable. Their contents cannot be modified.")
    print("  If you need mutable contents, the element cannot be placed in a set.")


# =============================================================================
# Main entry point -- runs all questions in sequence
# =============================================================================

if __name__ == "__main__":

    print("=" * 62)
    print("  Chapter 5 Practice Set: Sets and Dictionaries")
    print("=" * 62)

    # Run theoretical / demonstration questions automatically
    q3_int_and_str_in_set()
    q4_set_length_after_operations()
    q5_type_of_set()
    q7_duplicate_names()
    q8_duplicate_languages()
    q9_list_inside_set()

    # Run interactive questions that require user input
    print("\n" + "=" * 62)
    print("  Interactive Questions (require input)")
    print("=" * 62)

    q1_hindi_dictionary()
    q2_unique_numbers()
    q6_friends_language_dict()

    print("\n" + "=" * 62)
    print("  All questions completed.")
    print("=" * 62)
