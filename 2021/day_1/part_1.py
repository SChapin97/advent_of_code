#! /usr/bin/python3


with open ('input.txt', 'r') as file:
    prev=0
    total_increases=0

    for line in file.read().splitlines():
        
        if prev == 0:
            print("No previous depth recorded.")
        elif int(prev) == int(line):
            print("No change in depth.")
        elif int(prev) < int(line):
            print("Depth Increase:", line, "is larger than", prev)
            total_increases+=1
        else:
            print("Depth Decrease:",line, "is smaller than", prev)

        prev=line
    
    print("Total number of depth increases:", total_increases)