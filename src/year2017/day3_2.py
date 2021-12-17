def main():
    input = 347991

    grid_positions = [[1]]

    previous_perimeter_end = 0
    current_perimeter_level = 0

    current_perimeter_size = 0

    counter = 0

    current_grid_position = [1, 0]

    first_value_larger_than_input = 0

    while True:
        current_x_coordinate = current_grid_position[0]
        current_y_coordinate = current_grid_position[1]

        current_position_value = 1

        try:
                current_position_value += grid_positions[current_x_coordinate - 1][current_y_coordinate]
        except IndexError:
            pass

        try:
            current_position_value += grid_positions[current_x_coordinate - 1][current_y_coordinate + 1]
        except IndexError:
            pass

        try:
            current_position_value += grid_positions[current_x_coordinate - 1][current_y_coordinate - 1]
        except IndexError:
                pass

        try:
            current_position_value += grid_positions[current_x_coordinate + 1][current_y_coordinate]
        except IndexError:
                pass

        try:
            current_position_value += grid_positions[current_x_coordinate + 1][current_y_coordinate + 1]
        except IndexError:
                pass

        try:
            current_position_value += grid_positions[current_x_coordinate + 1][current_y_coordinate - 1]
        except IndexError:
                pass

        try:
            current_position_value += grid_positions[current_x_coordinate][current_y_coordinate + 1]
        except IndexError:
                pass

        try:
            current_position_value += grid_positions[current_x_coordinate][current_y_coordinate - 1]
        except IndexError:
                pass

        if current_position_value > input:
            first_value_larger_than_input = current_position_value
            break

        if counter >= current_perimeter_size + previous_perimeter_end:
            previous_perimeter_end = counter
            current_perimeter_level += 1
            current_perimeter_size += 8
            perimeter_move_counter = 0

        distance_to_top = current_perimeter_level * 2 - 1
        distance_across_sides = current_perimeter_level * 2

        if perimeter_move_counter < distance_to_top:
            current_grid_position[1] += 1

        elif perimeter_move_counter < distance_to_top + distance_across_sides:
            current_grid_position[0] -= 1

        elif perimeter_move_counter < distance_to_top + distance_across_sides * 2:
            current_grid_position[1] -= 1

        else:
            current_grid_position[0] += 1

        perimeter_move_counter += 1
        counter += 1
        print(current_position_value)

        if counter > 50:
            break

    print(first_value_larger_than_input)

if __name__ == "__main__":
    main()
