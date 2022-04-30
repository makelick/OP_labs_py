from lab_py_2_functions import *

first_file_path = "../first file.in"
second_file_path = "../second file.out"
input_file(first_file_path)

print("Birthday in this month AND work experience >= 5 years: ")
birthday_in_this_month(first_file_path)
print()

create_second_file(first_file_path, second_file_path)
print("Start career in <= 25 yo AND work experience >= 10 years (second file):")
output_file(second_file_path)
