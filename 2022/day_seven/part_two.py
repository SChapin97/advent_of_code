import re

def main():
    total_disk_space: int = 70000000
    required_empty_space: int = 30000000
    current_directory: str = ""
    input_filename = "input.txt"
    with open(input_filename, 'r+') as input_file:
        directory_size_dict: dict = {}
        directory_size_dict["/"] = 0

        for line in input_file.readlines():
            line = line.replace('\n', '')
            if line.startswith('$'):
                #Read command
                if line.startswith('$ cd'):
                    new_dir = re.sub('^.*cd ', '', line)
                    if new_dir == '..':
                        current_directory = re.sub(r'/[^\/]+$', '', current_directory)
                        current_directory = current_directory.replace("//", "/")
                        if not current_directory:
                            current_directory = "/"
                    else:
                        if new_dir == '/':
                            current_directory = new_dir
                        else:
                            current_directory += '/' + new_dir
                        current_directory = current_directory.replace('//', '/')
            else:
                if line.startswith('dir'):
                    dir_name: str = line.split(" ")[1]
                    file_path = current_directory + "/" + dir_name
                    file_path = file_path.replace("//", "/")
                    directory_size_dict[file_path] = 0

                elif re.match('^[0-9]', line):
                    #Found a file
                    file_size: int = int(line.split(" ")[0])

                    unravel_dir_name = current_directory
                    while unravel_dir_name:
                        directory_size_dict[unravel_dir_name] += file_size
                        if re.match(r'^/[^/]+$', unravel_dir_name):
                            unravel_dir_name = "/"
                        elif unravel_dir_name == "/":
                            unravel_dir_name = ""
                        else:
                            unravel_dir_name = re.sub(r'/[^\/]+$', '', unravel_dir_name)
    
    min_size_to_delete = required_empty_space - (total_disk_space - directory_size_dict["/"])

    possible_dirs_to_delete: dict = {}
    for dir in directory_size_dict.keys():
        if directory_size_dict[dir] >= min_size_to_delete:
            possible_dirs_to_delete[dir] = directory_size_dict[dir]

    lowest_file_size: int = 0
    for dir in possible_dirs_to_delete.keys():
        if lowest_file_size == 0 or possible_dirs_to_delete[dir] < lowest_file_size:
            lowest_file_size = possible_dirs_to_delete[dir]

    print(f"A directory with {lowest_file_size} bytes can be deleted to free enough space for an update.")



main()