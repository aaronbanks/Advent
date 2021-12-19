def main():

    current_x_coordinate = 1
    current_y_coordinate = 1

    current_position_value = 1

    grid_positions_values = {"0X0": 1}

    str_grid_position = str(current_x_coordinate) + "X" + str(current_y_coordinate)

    grid_positions_values[str_grid_position] = current_position_value

    print(grid_positions_values)

    str_grid_position = str(current_x_coordinate - 1 + 1) + "X" + str(current_y_coordinate)
    test = grid_positions_values[str_grid_position]

    print(test)


if __name__ == "__main__":
    main()
