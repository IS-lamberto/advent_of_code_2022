current_elf_1 = 0
current_elf_2 = 0
current_elf_3 = 0
new_elf = 0
number_of_elves = 0

with open('input.txt') as file:
    for line in file:
        if line in ['\n', '\r\n']:
            if new_elf > current_elf_1:
                current_elf_3 = current_elf_2
                current_elf_2 = current_elf_1
                current_elf_1 = new_elf
            elif new_elf > current_elf_2:
                current_elf_3 = current_elf_2
                current_elf_2 = new_elf
            elif new_elf > current_elf_3:
                current_elf_3 = new_elf
            new_elf = 0
            number_of_elves += 1
        else:
            # print(line.rstrip())
            new_elf += int(line)

print("Number of elves - " +str(number_of_elves))
print("1st elf - " + str(current_elf_1))
print("2nd elf - " + str(current_elf_2))
print("3rd elf - " + str(current_elf_3))
print("\n==============\nTotal 3 elfs")
print(current_elf_1 + current_elf_2 + current_elf_3)