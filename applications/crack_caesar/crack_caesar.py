# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here


common = [
    "E",
    "T",
    "A",
    "O",
    "H",
    "N",
    "R",
    "I",
    "S",
    "D",
    "L",
    "W",
    "U",
    "G",
    "F",
    "B",
    "M",
    "Y",
    "C",
    "P",
    "K",
    "V",
    "Q",
    "J",
    "X",
    "Z",
]
# filter out special characters
special_char = [
    '"',
    ":",
    ";",
    ",",
    ".",
    "-",
    "(",
    ")",
    "—",
    "!",
    "'",
    " ",
    "?",
    "\n",
]


# open the text file
with open("ciphertext.txt") as f:
    content = f.read()

letter_cache = {}

filtered_chars = "".join(filter(lambda char: char not in special_char, content))
count = 0
for c in filtered_chars:
    if c not in letter_cache:
        letter_cache[c] = 0
    letter_cache[c] += 1
    count += 1

for k, v in letter_cache.items():
    letter_cache[k] = v / count * 100
letter_list = list(letter_cache.items())
letter_list.sort(key=lambda e: e[1], reverse=True)
letter_map = {k: v for (k, v) in zip([i[0] for i in letter_list], common)}
output = ""
for char in content:
    output_char = char
    if char in letter_map:
        output_char = letter_map[char]
    output += output_char
print(output)

