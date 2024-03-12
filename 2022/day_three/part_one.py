import re

def main():
    total_value_of_nonunique_chars: int = 0

    filename = "input.txt"
    with open(filename, 'r+') as file:
        for line in file.readlines():
            line = line.replace('\n', '')
            half_length = int(len(line) / 2)
            first_half = line[0:half_length]
            second_half = line[half_length:]

            for char in first_half:
                if char in second_half:
                    total_value_of_nonunique_chars += get_value_of_chars(char)
                    break

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