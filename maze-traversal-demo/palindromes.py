"""Palindrome checker.

Checks if word in a list of words is a palindrome.
"""

for word in ['radar', 'racecar', 'grumble']:
    palindrome = True
    start = 0
    end = len(word) - 1   # pos of last letter

    while start < end:
        if word[start] != word[end]:
            print(f"Not a palindrome: {word}")
            palindrome = False
            break
        start = start + 1
        end = end - 1

    if palindrome:
        print(f"Palindrome: {word}")
