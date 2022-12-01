current_elf = 0
new_elf = 0

with open('input.txt') as file:
    for line in file:
        if line in ['\n', '\r\n']:
            if new_elf > current_elf:
                current_elf = new_elf
            new_elf = 0
        else:
            # print(line.rstrip())
            new_elf += int(line)

print(current_elf)