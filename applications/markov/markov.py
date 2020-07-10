import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# put all the words in a list
word_list = words.split(" ")
# put the words in a dict with the value of how many times it occurs
word_cache = {}
# start list
starting_list = []
# check str if its a starting word
def starting(str):
    if str[0].isupper():
        return True
    if str[0] == '"' and str[1].isupper():
        return True
    return False


# check str if its an ending word
def stopped(str):
    if str.endswith(("!", "?", ".")):
        return True
    if str.endswith('"'):
        if str[:-1].endswith(("!", "?", ".")):
            return True
    return False


# create the dataset
for index, str in enumerate(word_list):
    if index < len(word_list) - 1:
        if starting(str):
            starting_list.append(str)
        if str not in word_cache:
            word_cache[str] = []
        word_cache[str].append(word_list[index + 1])

# create teh sentence
for i in range(5):
    str = random.choice(starting_list)
    print(str, end=" ")
while not stopped(str):
    str = random.choice(word_cache[str])
    print(str, end=" ")
