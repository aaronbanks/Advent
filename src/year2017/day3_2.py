def main():
    input = 805
    #input = 347991

    grid_positions_values = {"0X0": 1}

    previous_perimeter_end = 1
    current_perimeter_level = 0

    current_perimeter_size = 0

    position_counter = 1

    current_x_coordinate = 1
    current_y_coordinate = 0

    first_value_larger_than_input = 0

    first_iteration = True

    while True:
        current_position_value = 0

        position_counter += 1

        print(f"position: {position_counter}")

#1# CALCULATE_CURRENT_POSITION_VALUE BASED ON SURROUNDING COORDINATES
        # for dx in [-1, 0, +1]:
        #   for dy in [-1, 0, +1]:
        #     if dx == 0 and dy == 0:
        #       continue
        #    // do something with x + dx and y + dy

        #don't need to convert to string, just use a tuple as key
        #.get(key, default)
        print(f"current_x_coordinate: {current_x_coordinate}\ncurrent_y_coordinate: {current_y_coordinate}")
        print("Values added to current position value:")

        try:
            temp_str_grid_position = str(current_x_coordinate - 1) + "X" + str(current_y_coordinate)
            current_position_value += grid_positions_values[temp_str_grid_position]
            print(f"grid_position: {temp_str_grid_position}, {grid_positions_values[temp_str_grid_position]}")
        except KeyError:
            pass

        try:
            temp_str_grid_position = str(current_x_coordinate - 1) + "X" + str(current_y_coordinate + 1)
            current_position_value += grid_positions_values[temp_str_grid_position]
            print(f"grid_position: {temp_str_grid_position}, {grid_positions_values[temp_str_grid_position]}")
        except KeyError:
            pass

        try:
            temp_str_grid_position = str(current_x_coordinate - 1) + "X" + str(current_y_coordinate - 1)
            current_position_value += grid_positions_values[temp_str_grid_position]
            print(f"grid_position: {temp_str_grid_position}, {grid_positions_values[temp_str_grid_position]}")
        except KeyError:
            pass

        try:
            temp_str_grid_position = str(current_x_coordinate + 1) + "X" + str(current_y_coordinate)
            current_position_value += grid_positions_values[temp_str_grid_position]
            print(f"grid_position: {temp_str_grid_position}, {grid_positions_values[temp_str_grid_position]}")
        except KeyError:
            pass

        try:
            temp_str_grid_position = str(current_x_coordinate + 1) + "X" + str(current_y_coordinate + 1)
            current_position_value += grid_positions_values[temp_str_grid_position]
            print(f"grid_position: {temp_str_grid_position}, {grid_positions_values[temp_str_grid_position]}")
        except KeyError:
            pass

        try:
            temp_str_grid_position = str(current_x_coordinate + 1) + "X" + str(current_y_coordinate - 1)
            current_position_value += grid_positions_values[temp_str_grid_position]
            print(f"grid_position: {temp_str_grid_position}, {grid_positions_values[temp_str_grid_position]}")
        except KeyError:
            pass

        try:
            temp_str_grid_position = str(current_x_coordinate) + "X" + str(current_y_coordinate + 1)
            current_position_value += grid_positions_values[temp_str_grid_position]
            print(f"grid_position: {temp_str_grid_position}, {grid_positions_values[temp_str_grid_position]}")
        except KeyError:
            pass

        try:
            temp_str_grid_position = str(current_x_coordinate) + "X" + str(current_y_coordinate - 1)
            current_position_value += grid_positions_values[temp_str_grid_position]
            print(f"grid_position: {temp_str_grid_position}, {grid_positions_values[temp_str_grid_position]}")
        except KeyError:
            pass

#2# CREATE NEW LOCATION IN GRID POSITION AND ASSIGN VALUE TO GRID POSITION
        str_grid_position = str(current_x_coordinate) + "X" + str(current_y_coordinate)
        grid_positions_values[str_grid_position] = current_position_value

        print(f"grid_positions_values: {grid_positions_values}")
        print(f"current_position_value: {current_position_value}")

#3# THIS IS THE CONDITION FOR ANSWERING THIS QUESTION
        if current_position_value > input:
            first_value_larger_than_input = current_position_value
            break

#4# MOVE TO THE NEXT POSITION IN THE SPIRAL
        if position_counter >= current_perimeter_size + previous_perimeter_end:
            if first_iteration == True:
                previous_perimeter_end = 1
            else:
                previous_perimeter_end = position_counter
            current_perimeter_level += 1
            current_perimeter_size += 8
            perimeter_move_counter = 0

        distance_to_top = current_perimeter_level * 2 - 1
        distance_across_sides = current_perimeter_level * 2

        if perimeter_move_counter < distance_to_top:
            current_y_coordinate += 1

        elif perimeter_move_counter < distance_to_top + distance_across_sides:
            current_x_coordinate -= 1

        elif perimeter_move_counter < distance_to_top + distance_across_sides * 2:
            current_y_coordinate -= 1

        else:
            current_x_coordinate += 1

        perimeter_move_counter += 1

        first_iteration = False

#5# PRINT SOLUTION
    print(f"first_value_larger_than_input: {first_value_larger_than_input}")

if __name__ == "__main__":
    main()
