def main():
    total_fully_contained_pairs: int = 0
    filename = "input.txt"
    with open(filename, 'r+') as file:
        for line in file.readlines():
            line = line.replace('\n', '')
            elf_one_section = line.split(',')[0]
            elf_one_start: int = int(elf_one_section.split('-')[0])
            elf_one_end: int = int(elf_one_section.split('-')[1])

            elf_two_section = line.split(',')[1]
            elf_two_start: int = int(elf_two_section.split('-')[0])
            elf_two_end: int = int(elf_two_section.split('-')[1])

            elf_one_span: int = elf_one_end - elf_one_start
            elf_two_span: int = elf_two_end - elf_two_start

            if elf_one_span <= elf_two_span and elf_one_start >= elf_two_start and elf_one_end <= elf_two_end:
                total_fully_contained_pairs += 1

            elif elf_two_span <= elf_one_span and elf_two_start >= elf_one_start and elf_two_end <= elf_one_end:
                total_fully_contained_pairs += 1

    print(
        f"There are {total_fully_contained_pairs} elves made redundant by their partner's span.")


main()
