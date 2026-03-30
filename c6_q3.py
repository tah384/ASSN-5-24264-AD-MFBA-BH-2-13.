# Q3
comment = input("Enter comment: ").lower()

if "make a lot of money" in comment or "buy now" in comment or "subscribe this" in comment or "click this" in comment:
    print("Spam detected")
else:
    print("Not spam")
