window_1 = [0,0,0]
window_2 = [0,0,0]
window_3 = [0,0,0]
window_4 = [0,0,0]
window_5 = [0,0,0]
window_6 = [0,0,0]

number_of_sum_increaes = 0
window_cycle_position = 0
current_completed_window = 1

def main():
    global window_1
    global window_2
    global window_3
    global window_4
    global window_5
    global window_6

    global number_of_sum_increaes
    global window_cycle_position
    global current_completed_window

    initiate_window_compairision = 0

    input_file = open('input202101.txt', 'r')

    for line in input_file:
        window_cycle_position += 1
        if window_cycle_position > 12:
            window_cycle_position = 1

        current_line_value = int(line.strip())
        print (f"The current depth reading is: {current_line_value}")

        add_value_to_windows(current_line_value)

        initiate_window_compairision += 1
        if initiate_window_compairision > 5:
            current_completed_window += 1

            if current_completed_window > 6:
                current_completed_window = 1

            window_compairison()
        else:
            pass

    input_file.close()

    current_completed_window = current_completed_window + 1
    if current_completed_window > 6:
        current_completed_window = 1
    window_compairison()

    current_completed_window = current_completed_window + 1
    if current_completed_window > 6:
        current_completed_window = 1
    window_compairison()
    
    print(f"The total number of sums which were larger than the previous sum was: {number_of_sum_increaes}")

    print(f"window 1 is now: {window_1}")
    print(f"window 2 is now: {window_2}")
    print(f"window 3 is now: {window_3}")
    print(f"window 4 is now: {window_4}")
    print(f"window 5 is now: {window_5}")
    print(f"window 6 is now: {window_6}")

    print(f"window_cycle_position is now {window_cycle_position}")
    print(f"current_completed_window is now {current_completed_window}")

def add_value_to_windows(current_line_value):
    global window_1
    global window_2
    global window_3
    global window_4
    global window_5
    global window_6

    global window_cycle_position

    if window_cycle_position == 1:
        window_1[0] = current_line_value
        window_5[2] = current_line_value
        window_6[1] = current_line_value

    elif window_cycle_position == 2:
        window_1[1] = current_line_value
        window_2[0] = current_line_value
        window_6[2] = current_line_value

    elif window_cycle_position == 3:
        window_1[2] = current_line_value
        window_2[1] = current_line_value
        window_3[0] = current_line_value

    elif window_cycle_position == 4:
        window_2[2] = current_line_value
        window_3[1] = current_line_value
        window_4[0] = current_line_value

    elif window_cycle_position == 5:
        window_3[2] = current_line_value
        window_4[1] = current_line_value
        window_5[0] = current_line_value

    elif window_cycle_position == 6:
        window_4[2] = current_line_value
        window_5[1] = current_line_value
        window_6[0] = current_line_value

    elif window_cycle_position == 7:
        window_5[2] = current_line_value
        window_6[1] = current_line_value
        window_1[0] = current_line_value

    elif window_cycle_position == 8:
        window_6[2] = current_line_value
        window_1[1] = current_line_value
        window_2[0] = current_line_value

    elif window_cycle_position == 9:
        window_1[2] = current_line_value
        window_2[1] = current_line_value
        window_3[0] = current_line_value

    elif window_cycle_position == 10:
        window_2[2] = current_line_value
        window_3[1] = current_line_value
        window_4[0] = current_line_value

    elif window_cycle_position == 11:
        window_3[2] = current_line_value
        window_4[1] = current_line_value
        window_5[0] = current_line_value

    elif window_cycle_position == 12:
        window_4[2] = current_line_value
        window_5[1] = current_line_value
        window_6[0] = current_line_value

def window_compairison():
    global window_1
    global window_2
    global window_3
    global window_4
    global window_5
    global window_6

    global number_of_sum_increaes
    global current_completed_window

    if current_completed_window == 1:
        print(f"The three numbers in the previous window were: {window_6} and the three in the current window are: {window_1}")
        print(f"The previous window total was: {sum(window_6)} and the current window total is: {sum(window_1)}")
        if sum(window_1) > sum (window_6):
            number_of_sum_increaes += 1
            print(f"Since the current window total is higher, the total number of sum increases has gone up to {number_of_sum_increaes}")
        else:
            pass

    elif current_completed_window == 2:
        print(f"The three numbers in the previous window were: {window_1} and the three in the current window are: {window_2}")
        print(f"The previous window total was: {sum(window_1)} and the current window total is: {sum(window_2)}")
        if sum(window_2) > sum (window_1):
            number_of_sum_increaes += 1
            print(f"Since the current window total is higher, the total number of sum increases has gone up to {number_of_sum_increaes}")
        else:
            pass

    elif current_completed_window == 3:
        print(f"The three numbers in the previous window were: {window_2} and the three in the current window are: {window_3}")
        print(f"The previous window total was: {sum(window_2)} and the current window total is: {sum(window_3)}")
        if sum(window_3) > sum (window_2):
            number_of_sum_increaes += 1
            print(f"Since the current window total is higher, the total number of sum increases has gone up to {number_of_sum_increaes}")
        else:
            pass

    elif current_completed_window == 4:
        print(f"The three numbers in the previous window were: {window_3} and the three in the current window are: {window_4}")
        print(f"The previous window total was: {sum(window_3)} and the current window total is: {sum(window_4)}")
        if sum(window_4) > sum (window_3):
            number_of_sum_increaes += 1
            print(f"Since the current window total is higher, the total number of sum increases has gone up to {number_of_sum_increaes}")
        else:
            pass

    elif current_completed_window == 5:
        print(f"The three numbers in the previous window were: {window_4} and the three in the current window are: {window_5}")
        print(f"The previous window total was: {sum(window_4)} and the current window total is: {sum(window_5)}")
        if sum(window_5) > sum (window_4):
            number_of_sum_increaes += 1
            print(f"Since the current window total is higher, the total number of sum increases has gone up to {number_of_sum_increaes}")
        else:
            pass

    elif current_completed_window == 6:
        print(f"The three numbers in the previous window were: {window_5} and the three in the current window are: {window_6}")
        print(f"The previous window total was: {sum(window_5)} and the current window total is: {sum(window_6)}")
        if sum(window_6) > sum (window_5):
            number_of_sum_increaes += 1
            print(f"Since the current window total is higher, the total number of sum increases has gone up to {number_of_sum_increaes}")
        else:
            pass

main()
