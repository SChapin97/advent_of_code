import re

def main():
    total_value_of_nonunique_chars: int = 0

    filename = "input.txt"
    with open(filename, 'r+') as file:
        group_flag = 0
        group_values: list = []
        for line in file.readlines():
            line = line.replace('\n', '')
            group_flag += 1
            group_values.append(line)

            if group_flag == 3:
                group_flag = 0
                badge_value: str = ""
                possible_badge_values: list = []
                for value in group_values:
                    if not possible_badge_values:
                        for char in value:
                            possible_badge_values.append(char)
                    else:
                        common_item_values: list = []
                        for char in possible_badge_values:
                            if char in value and char not in common_item_values:
                                common_item_values.append(char)
                        possible_badge_values = common_item_values
                
                group_values = []
                badge_value = possible_badge_values[0]
                total_value_of_nonunique_chars += get_value_of_chars(badge_value)


    print(f"The sum of priorities from each rucksack is {total_value_of_nonunique_chars}")

def get_value_of_chars(input_string: str) -> int:
    total_value: int = 0
    for char in input_string:
        if char.islower():
            total_value += ord(char) - 96
        else:
            total_value += ord(char) - 38

    return total_value


main()