def input_file(filename):
    with open(filename, 'w') as infile:
        line = input("Enter text (send empty line to finish): \n")
        while True:
            if line != "":
                infile.write(line + "\n")
                line = input()
            else:
                return


def output_file(filename):
    with open(filename, 'r') as file:
        lines = file.read().split("\n")
        for i in lines:
            print(i)


def create_second_file(first_file_name, second_file_name):
