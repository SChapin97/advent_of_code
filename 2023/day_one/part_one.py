import re


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
            puzzle_lines.append(line)
    return puzzle_lines


def get_numbers_from_string(input_string: str) -> list:
    numbers: list = re.findall("[0-9]", input_string)
    return numbers


def concatenate_numbers(first_digit: int, second_digit: int) -> int:
    return int(f"{first_digit}{second_digit}")


if __name__ == '__main__':
    main()
