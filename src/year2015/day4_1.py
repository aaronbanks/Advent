from ..functions import run_solution
import hashlib

# input_filename = "./inputs/201504.txt"
# expected_output = None


def main():

    secret_key = "ckczppom"
    hash_input = ""
    answer = ""

    iteration_count = 0

    while True:
        iteration_count += 1
        hash_input = f"{secret_key}{str(iteration_count)}"

        result = hashlib.md5(hash_input.encode())
        hexidecimal_equivalent = result.hexdigest()

        if hexidecimal_equivalent[0:5] == "00000":
            answer = iteration_count
            break

    print(answer)


if __name__ == "__main__":
    main()
