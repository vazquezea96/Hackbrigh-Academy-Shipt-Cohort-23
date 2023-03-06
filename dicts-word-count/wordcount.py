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

    # return letter_counts

    for letter, count in letter_counts.items():
        print(letter, count)


print(word_count('twain.txt'))
