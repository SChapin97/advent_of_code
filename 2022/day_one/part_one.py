import os

def main():
    filename = "input_one.txt"
    current_elf_calorie_count: int = 0
    elf_calorie_dict: dict = {}
    current_elf_position = 1

    with open(filename, 'r+') as file:
        for line in file.readlines():
            line = line.replace('\n', '')
            if line:
                current_elf_calorie_count += int(line)
            else:
                elf_calorie_dict[current_elf_position] = current_elf_calorie_count
                current_elf_calorie_count = 0
                current_elf_position += 1

    top_calorie_count = list(elf_calorie_dict.values())
    top_calorie_count.sort()
    top_calorie_count: int = top_calorie_count[-1]
    
    top_elf_position = list(elf_calorie_dict.values()).index(top_calorie_count)
    print(f"Elf with largest calorie count is number {top_elf_position}")
    print(f"This elf has {top_calorie_count} calories")

main()