import os
from datetime import date
from aocd.models import Puzzle
import shutil
import sys

# arguments
gen_input_and_example = True
if len(sys.argv) > 1:
    if(sys.argv[1] == "-n"):
        gen_input_and_example = False

import sys

# arguments
gen_input_and_example = True
if len(sys.argv) > 1:
    if(sys.argv[1] == "-n"):
        gen_input_and_example = False


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

# generate python solution file
template_file = os.path.join(current_working_directory, "src", "template.py")
destination_and_name = os.path.join(assembled_path, "sol"+current_day+".py")
if not os.path.exists(destination_and_name):
    shutil.copy(template_file, destination_and_name)

# generate pytest
template_file = os.path.join(current_working_directory, "src", "test_template.py")
destination_and_name = os.path.join(assembled_path, "test_"+current_day+".py")
if not os.path.exists(destination_and_name):
    shutil.copy(template_file, destination_and_name)
    # adjust import by replacing template with sol+current_day
    with open(destination_and_name, 'r') as file:
        filedata = file.read()
        filedata = filedata.replace("template", "sol"+current_day)
        with open(destination_and_name, 'w') as file:
            file.write(filedata)

# exit if no input and example should be generated
if not gen_input_and_example:
    sys.exit()

# generate pytest
template_file = os.path.join(current_working_directory, "src", "test_template.py")
destination_and_name = os.path.join(assembled_path, "test_"+current_day+".py")
if not os.path.exists(destination_and_name):
    shutil.copy(template_file, destination_and_name)
    # adjust import by replacing template with sol+current_day
    with open(destination_and_name, 'r') as file:
        filedata = file.read()
        filedata = filedata.replace("template", "sol"+current_day)
        with open(destination_and_name, 'w') as file:
            file.write(filedata)

# exit if no input and example should be generated
if not gen_input_and_example:
    sys.exit()

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
    print("The '%s' Directory does not exists" % new_directory)
try:
    empty_example_file = os.path.join(new_directory, "example2.txt")
    with open(empty_example_file, 'w') as example:
        example.write("")
        print("Created empty file '%s'. Fill it with the second example when you submitted the first solution" % empty_example_file)
except FileExistsError:
    print("The file '%s' is not empty!" % empty_example_file)


# generate pytest
template_file = os.path.join(current_working_directory, "src", "test_template.py")
destination_and_name = os.path.join(assembled_path, "test_"+current_day+".py")
if not os.path.exists(destination_and_name):
    shutil.copy(template_file, destination_and_name)
    # adjust import by replacing template with sol+current_day
    with open(destination_and_name, 'r') as file:
        filedata = file.read()
        filedata = filedata.replace("template", "sol"+current_day)
        with open(destination_and_name, 'w') as file:
            file.write(filedata)
            