import re
def main():
    #[V]     [B]                     [C]
    #[C]     [N] [G]         [W]     [P]
    #[W]     [C] [Q] [S]     [C]     [M]
    #[L]     [W] [B] [Z]     [F] [S] [V]
    #[R]     [G] [H] [F] [P] [V] [M] [T]
    #[M] [L] [R] [D] [L] [N] [P] [D] [W]
    #[F] [Q] [S] [C] [G] [G] [Z] [P] [N]
    #[Q] [D] [P] [L] [V] [D] [D] [C] [Z]
    # 1   2   3   4   5   6   7   8   9 
    crate_configuration = [['Q', 'F', 'M', 'R', 'L', 'W', 'C', 'V'], 
                           ['D', 'Q', 'L'], 
                           ['P', 'S', 'R', 'G', 'W', 'C', 'N', 'B'], 
                           ['L', 'C', 'D', 'H', 'B', 'Q', 'G'], 
                           ['V', 'G', 'L', 'F', 'Z', 'S'], 
                           ['D', 'G', 'N', 'P'], 
                           ['D', 'Z', 'P', 'V', 'F', 'C', 'W'], 
                           ['C', 'P', 'D', 'M', 'S'], 
                           ['Z', 'N', 'W', 'T', 'V', 'M', 'P', 'C']]
    filename = "input.txt"
    print(f"Initial crate configuration: {crate_configuration}")
    with open(filename, 'r+') as file:
        for line in file.readlines():
            line = line.replace('\n', '')
            num_to_move = int(re.sub(r'(move )([0-9]+)(.*)', r'\2', line))
            start_stack = int(re.sub(r'(.*from )([0-9]+)(.*)', r'\2', line)) - 1
            end_stack= int(re.sub(r'(.*to )([0-9]+)(.*)', r'\2', line)) - 1

            while num_to_move > 0:
                crate_configuration[end_stack] += crate_configuration[start_stack][-1]
                crate_configuration[start_stack] = crate_configuration[start_stack][:-1]

                num_to_move -= 1
                
        print(f"Final crate configuration: {crate_configuration}")
        top_crates = []
        for stack in crate_configuration:
            top_crates.append(stack[-1])
        print(f"Contents at the top of the crate configuration: {top_crates}")

main()
