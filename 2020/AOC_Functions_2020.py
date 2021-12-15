def read_lines(file_name):

    return_list = []

    with open(file_name, "r") as input:

        for line in input:
            return_list.append(line.strip())

    return return_list
