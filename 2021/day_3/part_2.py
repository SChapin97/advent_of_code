#! /usr/bin/python3

import re

#test input is 5 digits long, real input is 12
INPUT_LENGTH = 5

def main():
    with open ('test_input.txt', 'r') as file:
        
        total_zeroes_array = [0] * INPUT_LENGTH
        total_ones_array = [0] * INPUT_LENGTH

        for line in file.read().splitlines():
            r_bits = re.compile("[0-1]")

            position = 0
            for value in re.findall(r_bits, line):
                if value == "0":
                    total_zeroes_array[position] += 1
                elif value == "1":
                    total_ones_array[position] += 1
                else:
                    print("Invalid character:", value)
                
                position += 1

        find_power_rates(total_zeroes_array, total_ones_array)
        

def find_power_rates(zero_array, one_array):
    oxygen_rate = [0] * INPUT_LENGTH   # Bit with more occurrences in given position
    carbon_dioxide_rate = [0] * INPUT_LENGTH # Bit with least occurrences in given position

    # print("Zero array:", *zero_array)
    # print("One array: ", *one_array)

    position=0
    while position < INPUT_LENGTH:
        if zero_array[position] > one_array[position]:
            oxygen_rate[position] = 0
            carbon_dioxide_rate[position] = 1
        elif one_array[position] >= zero_array[position]:
            oxygen_rate[position] = 1
            carbon_dioxide_rate[position] = 0

        position += 1

    # print("oxygen rate is:", *oxygen_rate)
    # print("carbon_dioxide rate is:", *carbon_dioxide_rate)



def find_correct_value_in_array(array_to_search, search_key):


    for binary_key in search_key:
        pass




# def find_total_power_consumption(oxygen_rate, carbon_dioxide_rate):
#     grb_string = [str(i) for i in oxygen_rate]
#     oxygen_rate_binary = "".join(grb_string)
#     erb_string = [str(i) for i in carbon_dioxide_rate]
#     carbon_dioxide_rate_binary = "".join(erb_string)

#     oxygen_rate_decimal=int(oxygen_rate_binary,2)
#     carbon_dioxide_rate_decimal=int(carbon_dioxide_rate_binary,2)
#     total_power_consumption=0

#     print("Binary oxygen rate number", oxygen_rate_binary, "is decimal number", oxygen_rate_decimal)
#     print("Binary carbon_dioxide rate number", carbon_dioxide_rate_binary, "is decimal number", carbon_dioxide_rate_decimal)

#     total_power_consumption = int(oxygen_rate_decimal * carbon_dioxide_rate_decimal)
#     print("Total power consumption:", total_power_consumption)


main()