def main():

    current_compass_direction = "N"
    list_of_compass_directions = ("N", "E", "S", "W")

    compass_direction_value = 0

    horizontal_position = 0
    vertical_position = 0

    set_of_locations_visited = {(0, 0)}

    location_found = False
    first_location_visited_twice = ()

    with open("./inputs/201601.txt", "r") as input:

        for line in input:
            current_line_contents = (line.strip()).split(", ")

            for instruction in current_line_contents:

                if instruction[:1] == "R":
                    compass_direction_value += 1
                    if compass_direction_value > 3:
                        compass_direction_value = 0

                elif instruction[:1] == "L":
                    compass_direction_value -= 1
                    if compass_direction_value < 0:
                        compass_direction_value = 3

                current_compass_direction = list_of_compass_directions[
                    compass_direction_value
                ]

                counter = 1
                while counter <= int(instruction[1:]):
                    counter += 1

                    if current_compass_direction == "N":
                        vertical_position += 1

                    elif current_compass_direction == "E":
                        horizontal_position += 1

                    elif current_compass_direction == "S":
                        vertical_position -= 1

                    elif current_compass_direction == "W":
                        horizontal_position -= 1

                    current_location = (horizontal_position, vertical_position)

                    if current_location in set_of_locations_visited:
                        location_found = True
                        first_location_visited_twice = current_location

                        print(
                            f"The locations visited so far: {set_of_locations_visited}"
                        )
                        print(f"The Current location is {current_location}")
                        break

                    else:
                        set_of_locations_visited.add(current_location)

                if location_found == True:
                    break

            if location_found == True:
                break

    distance_to_destination = abs(first_location_visited_twice[0]) + abs(
        first_location_visited_twice[1]
    )

    print(f"The shortest path to the destination is {distance_to_destination} blocks")


main()
