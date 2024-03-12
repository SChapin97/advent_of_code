def main():
    filename = "input.txt"
    character_list: list = []
    with open(filename, 'r+') as file:
        for character in file.readline():
            character_list.append(character)
            if len(character_list) >= 4:
                last_four_characters = character_list[-4:]

                # If this stays True after the while loop, we have our marker.
                is_marker: bool = True
                while len(last_four_characters) > 0:
                    search_char = last_four_characters.pop()
                    if search_char in last_four_characters:
                        is_marker = False

                if is_marker:
                    print(
                        f"The first marker can be found at character {len(character_list)}")
                    exit()


main()
