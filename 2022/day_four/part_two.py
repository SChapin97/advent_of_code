def main():
    total_pairs_with_overlapping_spans: int = 0
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

            if elf_one_start <= elf_two_end and elf_one_end >= elf_two_start:
                total_pairs_with_overlapping_spans += 1

            elif elf_two_start <= elf_one_end and elf_two_end >= elf_one_start:
                total_pairs_with_overlapping_spans += 1

    print(
        f"There are {total_pairs_with_overlapping_spans} pairs of elves with overlapping ranges.")


main()
