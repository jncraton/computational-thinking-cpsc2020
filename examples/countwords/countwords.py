def count_words(text):
    count = 0
    in_whitespace = True

    for char in text:
        if char == " " or char == "\n":
            in_whitespace = True
        elif in_whitespace:
            count += 1
            in_whitespace = False

    return count

assert count_words("Hello world") == 2
assert count_words("   extra   spaces   ") == 2
assert count_words("") == 0