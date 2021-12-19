def main():
    #input = 347991
    input = 805

    grid_positions_values = {"0X0": 1}

    previous_perimeter_end = 1
    current_perimeter_level = 0

    current_perimeter_size = 0

    position_counter = 0

    current_grid_position = [1, 0]

    first_value_larger_than_input = 0

    while True:
        current_position_value = 0

        current_x_coordinate = current_grid_position[0]
        current_y_coordinate = current_grid_position[1]

        position_counter += 1

        if position_counter == 1:
            position_counter += 1
        print(f"position: {position_counter}")


#1# CALCULATE_CURRENT_POSITION_VALUE BASED ON SURROUNDING COORDINATES
        #if current_grid_position has_key():

        try:
            temp_str_grid_position = str(current_x_coordinate - 1) + "X" + str(current_y_coordinate)
            current_position_value += grid_positions_values[temp_str_grid_position]
        except KeyError:
            pass

        try:
            temp_str_grid_position = str(current_x_coordinate - 1) + "X" + str(current_y_coordinate + 1)
            current_position_value += grid_positions_values[temp_str_grid_position]
        except KeyError:
            pass

        try:
            temp_str_grid_position = str(current_x_coordinate - 1) + "X" + str(current_y_coordinate - 1)
            current_position_value += grid_positions_values[temp_str_grid_position]
        except KeyError:
            pass

        try:
            temp_str_grid_position = str(current_x_coordinate + 1) + "X" + str(current_y_coordinate)
            current_position_value += grid_positions_values[temp_str_grid_position]
        except KeyError:
            pass

        try:
            temp_str_grid_position = str(current_x_coordinate + 1) + "X" + str(current_y_coordinate + 1)
            current_position_value += grid_positions_values[temp_str_grid_position]
        except KeyError:
            pass

        try:
            temp_str_grid_position = str(current_x_coordinate + 1) + "X" + str(current_y_coordinate - 1)
            current_position_value += grid_positions_values[temp_str_grid_position]
        except KeyError:
            pass

        try:
            temp_str_grid_position = str(current_x_coordinate) + "X" + str(current_y_coordinate + 1)
            current_position_value += grid_positions_values[temp_str_grid_position]
        except KeyError:
            pass

        try:
            temp_str_grid_position = str(current_x_coordinate) + "X" + str(current_y_coordinate + 1)
            current_position_value += grid_positions_values[temp_str_grid_position]
        except KeyError:
            pass

        print(f"current_position_value: {current_position_value}")

#2# CREATE NEW LOCATION IN GRID POSITION AND ASSIGN VALUE TO GRID POSITION
        str_grid_position = str(current_x_coordinate) + "X" + str(current_y_coordinate)
        grid_positions_values[str_grid_position] = current_position_value

#4# THIS IS THE CONDITION FOR ANSWERING THIS QUESTION
        if current_position_value > input:
            first_value_larger_than_input = current_position_value
            break

#3# MOVE TO THE NEXT POSITION IN THE SPIRAL
        if position_counter >= current_perimeter_size + previous_perimeter_end:
            previous_perimeter_end = position_counter
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

#5# PRINT SOLUTION
    print(f"first_value_larger_than_input: {first_value_larger_than_input}")

if __name__ == "__main__":
    main()
