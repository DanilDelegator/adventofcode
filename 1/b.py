f = open("./b.input", "r")
raw = f.read()

first = 0 
second = 0
third = 0

elves_inventories = raw.split("\n\n")
for elf_inventory in elves_inventories:
    elf_calories = sum(map(lambda x: int(x), elf_inventory.strip().split("\n")))
    if elf_calories >= first:
        third, second, first = second, first, elf_calories
    elif elf_calories >= second:
        third, second = second, elf_calories
    elif elf_calories > third:
        third = elf_calories

print(first + second + third)

