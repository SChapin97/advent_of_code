#! /usr/bin/python3

def main():
    with open ('input.txt', 'r') as file:
        list=[]
        prev_sum=0
        total_increases=0

        for line in file.read().splitlines():
            add_to_list(list, line)
            curr_sum = sum_list(list)
            
            if len(list) == 3:
                if prev_sum == 0:
                    print("No previous depth recorded.", curr_sum)
                elif curr_sum == prev_sum:
                    print("No change.", curr_sum)
                elif curr_sum >= prev_sum:
                    print("Depth increase:", curr_sum, "is larger than", prev_sum)
                    total_increases+=1
                else:
                    print("Depth decrease:", curr_sum, "is smaller than", prev_sum)
                
                prev_sum=curr_sum
        
        print("Total number of depth increases:", total_increases)

def add_to_list(list, item):
    #Using a list as a queue with 3 maximum members.

    if len(list) == 3:
        for pos in range(len(list)):
            if pos > 0:
                list[pos - 1] = list[pos]
        list.pop()
    
    list.append(item)
    return list

def sum_list(list):
    total=0
    for item in list:
        total+=int(item)

    return total

main()