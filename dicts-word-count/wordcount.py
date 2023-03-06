"""Count words in file."""

# put your code here.

def word_count(filename):
    with open(filename, 'r') as reader:
        letter_counts = {}

        for line in reader:
            line = line.strip()
            line = line.split(' ')

            for letter in line:
                letter_counts[letter] = letter_counts.get(letter, 0) + 1

    return letter_counts


print(word_count('test.txt'))
