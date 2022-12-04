from string import ascii_letters

score_table = {}

for index, letter in enumerate(ascii_letters):
    score_table[letter] = index + 1

print(score_table)