from ..functions import run_solution
import math

input_filename = "./inputs/201901.txt"
expected_output = 4892135


def solution(input_lines):

    total_fuel_req = 0

    for module in input_lines:
        mass = float(module)

        fuel_req_for_module = int(math.floor(mass / 3) - 2)

        fuel_req_for_fuel = 0

        recursive_fuel_calculation = fuel_req_for_module
        decaying_fuel_for_fuel = 0

        while True:

            decaying_fuel_for_fuel = int(math.floor(recursive_fuel_calculation / 3) - 2)
            if decaying_fuel_for_fuel < 1:
                break

            fuel_req_for_fuel += decaying_fuel_for_fuel

            recursive_fuel_calculation = int(math.floor(decaying_fuel_for_fuel / 3) - 2)
            if recursive_fuel_calculation < 1:
                break

            fuel_req_for_fuel += recursive_fuel_calculation

        total_fuel_req += fuel_req_for_module + fuel_req_for_fuel

    print(total_fuel_req)
    return total_fuel_req


if __name__ == "__main__":
    run_solution(solution, input_filename, expected_output)
