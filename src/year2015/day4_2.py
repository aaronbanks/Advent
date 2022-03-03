from ..functions import run_solution
import hashlib


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

        if hexidecimal_equivalent[0:6] == "000000":
            answer = iteration_count
            break

    print(answer)


if __name__ == "__main__":
    main()
