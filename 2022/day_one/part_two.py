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

    calorie_count_list = list(elf_calorie_dict.values())
    calorie_count_list.sort()
    top_calorie_count: int = calorie_count_list[-1]
    second_calorie_count: int = calorie_count_list[-2]
    third_calorie_count: int = calorie_count_list[-3]
    
    top_elf_position = list(elf_calorie_dict.values()).index(top_calorie_count)
    second_elf_position = list(elf_calorie_dict.values()).index(second_calorie_count)
    third_elf_position = list(elf_calorie_dict.values()).index(third_calorie_count)
    
    print(f"Elf with the largest calorie count is number {top_elf_position}")
    print(f"This elf has {top_calorie_count} calories")

    print(f"Elf with the seocnd largest calorie count is number {second_elf_position}")
    print(f"This elf has {second_calorie_count} calories")

    print(f"Elf with the third largest calorie count is number {third_elf_position}")
    print(f"This elf has {third_calorie_count} calories")

    top_three_total_calorie_count: int = top_calorie_count + second_calorie_count + third_calorie_count
    print(f"These elves are carrying {top_three_total_calorie_count} calories in total.")

main()