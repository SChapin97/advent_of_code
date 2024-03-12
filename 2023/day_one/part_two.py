import re

SINGLE_DIGIT_PHONETIC_NUMBERS: dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def main():
    filename = "puzzle_input.txt"
    input_text = read_puzzle_input_from_file(filename)
    all_calibration_numbers = []
    for line in input_text:
        numbers = get_numbers_from_string(line)
        first_number = numbers[0]
        last_number = numbers[-1]
        all_calibration_numbers.append(concatenate_numbers(first_number, last_number))

    print(f"Sum of all calibration numbers: {sum(all_calibration_numbers)}")


def read_puzzle_input_from_file(filename: str) -> list:
    puzzle_lines = []
    with open(filename, 'r+') as file:
        for line in file.readlines():
            puzzle_lines.append(line.strip())
    return puzzle_lines


def get_numbers_from_string(input_string: str) -> list:
    # Some numbers are phonetic (e.g. "one") and must be formatted as an integer (e.g. 1)
    # Need to read from right to left
    non_phonetic_input = input_string.lower()
    current_string = ""
    for character in non_phonetic_input:  # TODO: Debug
        current_string = f"{current_string}{character}"
        for word in SINGLE_DIGIT_PHONETIC_NUMBERS.keys():
            if word in current_string:
                current_string = current_string.replace(str(SINGLE_DIGIT_PHONETIC_NUMBERS.get(word)), "")
    non_phonetic_input = current_string

    print(f"Not formatted: {input_string}, formatted: {non_phonetic_input}")
    numbers: list = re.findall("[0-9]", non_phonetic_input)
    return numbers


def concatenate_numbers(first_digit: int, second_digit: int) -> int:
    return int(f"{first_digit}{second_digit}")


if __name__ == '__main__':
    main()
