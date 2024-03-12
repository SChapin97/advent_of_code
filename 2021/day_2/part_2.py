#! /usr/bin/python3

def main():
    horizontal_total=0
    aim=0
    depth_total=0

    with open ('input.txt', 'r') as file:
        for line in file.read().splitlines():
            amount=int(line.split(" ")[1])
            print("Current totals: Horizontal:", horizontal_total, "Depth:", depth_total, "Aim:", aim)

            if line.__contains__("forward"):
                print("Going", line)
                horizontal_total += amount
                depth_total += int(aim * amount)
            elif line.__contains__("up"):
                print("Aiming", line)
                aim -= amount
            elif line.__contains__("down"):
                print("Aiming", line)
                aim += amount
            else:
                print("Not sure what to do with", line)
        
        print("Horizontal total:", horizontal_total)
        print("Depth total:", depth_total)
        print("Total movement multiplied:", int(horizontal_total * depth_total))


main()