"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    species = set()

    with open(filename, 'r') as reader:
        for line in reader:
            line = line.split('|')
            species.add(line[1])

    return species

# print(all_species('villagers.csv'))


def get_villagers_by_species(filename, search_string=None):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []

    with open(filename, 'r') as reader:
        for line in reader:
            line = line.split('|')
            if search_string:
                if line[1] == search_string:
                    villagers.append(line[0])
            else:
                villagers.append(line[0])

    return sorted(villagers)


# print(get_villagers_by_species('villagers.csv'))


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    villagers = []
    fitness = []
    nature = []
    education = []
    music = []
    fashion = []
    play = []

    with open(filename, 'r') as reader:
        for line in reader:
            line = line.split('|')
            hobby = line[3]
            name = line[0]
            if hobby == 'Fitness':
                fitness.append(name)
            elif hobby == 'Nature':
                nature.append(name)
            elif hobby == 'Education':
                education.append(name)
            elif hobby == 'Music':
                music.append(name)
            elif hobby == 'Fashion':
                fashion.append(name)
            elif hobby == "Play":
                play.append(name)

    villagers.extend([sorted(fitness), sorted(nature), sorted(
        education), sorted(music), sorted(fashion), sorted(play)])

    return villagers


# print(all_names_by_hobby("villagers.csv"))


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    with open(filename, 'r') as reader:
        for line in reader:
            line = line.rstrip()
            line = line.split('|')

            villager = (line[0], line[1], line[2], line[3], line[4])
            all_data.append(villager)

    return all_data


# print(all_data('villagers.csv'))


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    with open(filename, 'r') as reader:
        for line in reader:
            line = line.split("|")
            if villager_name:
                if villager_name == line[0]:
                    return line[4]
            else:
                return None


# print(find_motto("villagers.csv", "Liying"))


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """
    likeminded_set = set([])

    with open(filename, 'r') as reader:
        personality = ""
        for line in reader:
            line = line.split("|")
            if line[0] == villager_name:
                personality = line[2]

            if personality == line[2]:
                likeminded_set.add(line[0])

    return likeminded_set


# print(find_likeminded_villagers("villagers.csv", "Antonio"))
