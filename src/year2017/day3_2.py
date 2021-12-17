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
        current_position_value = 0

        current_x_coordinate = current_grid_position[0]
        current_y_coordinate = current_grid_position[1]

#1# ITERATE THROUGH A POSITION IN THE SPIRAL AND UPDATE YOU GRID POSITION COORDINATES ACCORDINGLY
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
#2# CALCULATE_CURRENT_POSITION_VALUE BASED ON SURROUNDING COORDINATES
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
#3# NEED TO CREATE NEW LOCATION IN GRID POSITION AND ASSIGN VALUE TO GRID POSITION
        grid_positions[current_grid_position[0]].append()


#4# THIS IS THE CONDITION FOR ANSWERING THIS QUESTION
        if current_position_value > input:
            first_value_larger_than_input = current_position_value
            break

#5# PRINT SOLUTION
    print(first_value_larger_than_input)

if __name__ == "__main__":
    main()
