import re

def main():
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
                        elif unravel_dir_name != '/':
                            unravel_dir_name = re.sub(r'/[^\/]+$', '', unravel_dir_name)
                        else:
                            unravel_dir_name = ""
    
    total_size_to_delete: int = 0
    for dir in directory_size_dict.keys():
        if directory_size_dict[dir] <= 100000:
            total_size_to_delete += directory_size_dict[dir]

    print(f"A total of {total_size_to_delete} bytes can be freed from the system.")

main()