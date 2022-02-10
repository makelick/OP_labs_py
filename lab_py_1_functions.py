def input_file(filename):
    with open(filename, 'w') as infile:
        line = input("Enter text (send empty line to finish): \n")
        while line != "":
            infile.write(line + "\n")
            line = input()


def output_file(filename):
    with open(filename, 'r') as file:
        lines = file.read().split("\n")
        for i in lines:
            print(i)


def create_second_file(first_file_name, second_file_name):
    with open(first_file_name, 'r') as infile:
        with open(second_file_name, 'w') as outfile:
            lines = infile.read().split("\n")
            for i in lines:
                if i != "":
                    temp = i.replace(";", " ")
                    temp = i.replace(",", " ")
                    words = temp.split()
                    outfile.write(str(count_same_words(words)) + " " + i + "\n")


def count_same_words(words):
    max_count = 0
    for i in range(len(words)):
        if words.count(words[i]) > max_count:
            max_count = words.count(words[i])
    return max_count
