f = open("./a.input", "r")
raw = f.read()

m = 0
elves_inventories = raw.split("\n\n")
for elf_inventory in elves_inventories:
    m = max(m, sum(map(lambda x: int(x), elf_inventory.strip().split("\n"))))

print(m)
