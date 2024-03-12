def main():
    filename = "input.txt"
    character_list: list = []
    found_marker: bool = False
    with open(filename, 'r+') as file:
        for character in file.readline():
            character_list.append(character)
            if not found_marker:
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
                        found_marker = True
            else:
                if len(character_list) >= 14:
                    last_fourteen_characters = character_list[-14:]

                    # If this stays True after the while loop, we have our marker.
                    is_message: bool = True
                    while len(last_fourteen_characters) > 0:
                        search_char = last_fourteen_characters.pop()
                        if search_char in last_fourteen_characters:
                            is_message = False

                    if is_message:
                        print(
                            f"The first message can be found at character {len(character_list)}")
                        exit()


main()
