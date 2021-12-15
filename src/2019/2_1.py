from ..functions import read_lines

def main():



    input = read_lines("./inputs/201902.txt")

    intcode = input.split(",")

    location_counter = 0

    while True:

        opcode = intcode[location_counter]

        if opcode = "1":

        elif opcode = "2":

        elif opcode = "99":

        else:
            print("opcode alingment error")

        location_counter += 4
