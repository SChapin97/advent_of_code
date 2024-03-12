#! /usr/bin/python3

import re

#test input is 5 digits long, real input is 12
INPUT_LENGTH = 12

def main():
    with open ('input.txt', 'r') as file:
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
    gamma_rate = [0] * INPUT_LENGTH   # Bit with more occurrences in given position
    epsilon_rate = [0] * INPUT_LENGTH # Bit with least occurrences in given position

    # print("Zero array:", *zero_array)
    # print("One array: ", *one_array)

    position=0
    while position < INPUT_LENGTH:
        if zero_array[position] > one_array[position]:
            gamma_rate[position] = 0
            epsilon_rate[position] = 1
        elif one_array[position] > zero_array[position]:
            gamma_rate[position] = 1
            epsilon_rate[position] = 0
        else:
            print("Number of zeroes and ones for position", position, "is the same, cannot figure out gamma rate.")

        position += 1

    # print("Gamma rate is:", *gamma_rate)
    # print("Epsilon rate is:", *epsilon_rate)

    find_total_power_consumption(gamma_rate, epsilon_rate)

def find_total_power_consumption(gamma_rate, epsilon_rate):
    grb_string = [str(i) for i in gamma_rate]
    gamma_rate_binary = "".join(grb_string)
    erb_string = [str(i) for i in epsilon_rate]
    epsilon_rate_binary = "".join(erb_string)

    gamma_rate_decimal=int(gamma_rate_binary,2)
    epsilon_rate_decimal=int(epsilon_rate_binary,2)
    total_power_consumption=0

    print("Binary gamma rate number", gamma_rate_binary, "is decimal number", gamma_rate_decimal)
    print("Binary epsilon rate number", epsilon_rate_binary, "is decimal number", epsilon_rate_decimal)

    total_power_consumption = int(gamma_rate_decimal * epsilon_rate_decimal)
    print("Total power consumption:", total_power_consumption)


main()