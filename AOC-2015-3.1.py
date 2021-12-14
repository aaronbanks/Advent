def main():

    with open('input201503.txt', 'r') as input:

        set_of_houses = {(0,0)}

        total_number_of_houses = 1

        horizontal_position = 0
        vertical_position = 0

        for line in input:
                current_line_contents = line.strip()

                for character in current_line_contents:
                    if character == "^":
                        vertical_position += 1

                    if character == "v":
                        vertical_position -= 1

                    if character == ">":
                        horizontal_position += 1

                    if character == "<":
                        horizontal_position -= 1

                    current_position = (horizontal_position, vertical_position)

                    if current_position in set_of_houses:
                        pass
                    else:
                        set_of_houses.add(current_position)
                        total_number_of_houses += 1

        print(f"The total number of houses visited is: {total_number_of_houses}")

main()
