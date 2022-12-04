elf_pairs = [line.strip().split(",") for line in open("./a.input", "r").readlines()]

res = 0

for first, second in elf_pairs:
    first_s, first_e = [int(item) for item in first.split("-")]
    second_s, second_e = [int(item) for item in second.split("-")]

    if (first_s <= second_s and second_e <= first_e) or \
        (second_s <= first_s and first_e <= second_e):
        res += 1

print(res)