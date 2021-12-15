from AOC_Functions import read_lines
import math

def main():

    input = read_lines("input201901.txt")

    total_fuel_req = 0

    for module in input:
        mass = float(module)

        fuel_req = int(math.floor(mass / 3) - 2)

        total_fuel_req += fuel_req

    print(total_fuel_req)

main()
