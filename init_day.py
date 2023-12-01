import os
from datetime import date
from aocd.models import Puzzle

# get date
today = date.today()
current_day = today.strftime('%d')
current_year = today.strftime('%Y')

# create new directory if it doesn't exist yet
new_directory = os.path.join(current_year, current_day)
current_working_directory = os.getcwd()
assembled_path = os.path.join(current_working_directory, new_directory)
if not os.path.exists(assembled_path):
    os.mkdir(assembled_path)
    print("Created new directory '% s'" % new_directory)
else:
    print("Directory '%s' already exists" % new_directory)

# TODO: python template file

# get input.txt
puzzle = Puzzle(day = int(current_day), year = int(current_year))
new_input_file = os.path.join(new_directory, "input.txt")
try:
    with open(new_input_file, 'w') as input:
        input.write(puzzle.input_data)
except FileExistsError:
    print("The input file '%s' does already exists" % new_input_file)
except FileNotFoundError:
    print("The '%s' Directory does not exists" % new_directory)

# get example.txt
example_parts = puzzle.examples
try:
    for part_number in range(len(example_parts)):
        new_example_file = os.path.join(new_directory, "example" + str(part_number+1) + ".txt")
        with open(new_example_file, 'w') as example:
            example.write(example_parts[part_number].input_data)
except FileExistsError:
    print("The input file '%s' does already exists" % new_example_file)
except FileNotFoundError:
    print("The '%s' Directory does not exists" % new_example_file)

# TODO: generate pytest
