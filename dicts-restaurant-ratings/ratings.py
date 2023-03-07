"""Restaurant rating lister."""

# put your code here
def restaurant_ratings(filename):
    with open(filename, 'r') as reader:
        ratings = {}
        # looping through file
        for line in reader:
            line = line.strip()
            line = line.split(':')

            # assigning key and value to dictionary

            ratings[line[0]] = line[1]
        # sorting dictonary in alphabetical order
        sorted_rating = sorted(ratings)

    for show in sorted_rating:
        print(f"{show} is rated a {ratings[show]}.")

print(restaurant_ratings('scores.txt'))