from ..functions import run_solution

input_filename = "./inputs/202101.txt"
expected_output = 1446


def solution(input_lines):
    previous_measurement = 0
    current_measurement = 0
    depth_increases = 0
    line_count = 0

    for current_line in input_lines:
        if len(current_line) == 0:
            print(
                f"The total number of times a depth measurement increased was: {depth_increases}"
            )
            break

        else:
            line_count += 1
            current_measurement = int(current_line.strip())
            print(f"Depth reading # {line_count} is {current_measurement}")

            if line_count == 1 or current_measurement <= previous_measurement:
                pass
            elif current_measurement > previous_measurement and line_count > 1:
                depth_increases += 1

            print(f"The current # of Depth increases is: {depth_increases}")
            previous_measurement = current_measurement

    return depth_increases


if __name__ == "__main__":
    run_solution(solution, input_filename, expected_solution)
