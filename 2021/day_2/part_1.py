#! /usr/bin/python3

def main():
    horizontal_total=0
    depth_total=0

    with open ('input.txt', 'r') as file:
        for line in file.read().splitlines():
            if line.__contains__("forward"):
                print("Going", line)
                horizontal_total += int(line.split(" ")[1])
            elif line.__contains__("up"):
                print("Going", line)
                depth_total -= int(line.split(" ")[1])
            elif line.__contains__("down"):
                print("Going", line)
                depth_total += int(line.split(" ")[1])
            else:
                print("Not sure what to do with", line)
        
        print("Horizontal total:", horizontal_total)
        print("Depth total:", depth_total)
        print("Total movement multiplied:", int(horizontal_total * depth_total))


main()