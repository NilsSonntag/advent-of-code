import os
from datetime import date
from aocd.models import Puzzle
import shutil
from pathlib import Path

# get date
today = date.today()
current_day = today.strftime('%d')
current_year = today.strftime('%Y')

# create new directory if it doesn't exist yet
new_directory = Path(current_year, current_day)
new_directory.mkdir(parents=True, exist_ok=True)

# generate python solution file
template_file = Path("src", "template.py")
destination_and_name = new_directory / f"sol{current_day}.py"
if not destination_and_name.exists():
    shutil.copy(template_file, destination_and_name)

# get input.txt
puzzle = Puzzle(day=int(current_day), year=int(current_year))
new_input_file = new_directory / "input.txt"

def write_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            file.write(data)
    except FileExistsError:
        print(f"The file '{file_path}' already exists.")
    except FileNotFoundError:
        print(f"The directory '{new_directory}' does not exist.")

write_file(new_input_file, puzzle.input_data)

# get example.txt
example_parts = puzzle.examples
for part_number, example_part in enumerate(example_parts, start=1):
    new_example_file = new_directory / f"example{part_number}.txt"
    write_file(new_example_file, example_part.input_data)

empty_example_file = new_directory / "example2.txt"
write_file(empty_example_file, "")

# generate pytest
template_file = Path("src", "test_template.py")
destination_and_name = new_directory / f"test_{current_day}.py"
if not destination_and_name.exists():
    shutil.copy(template_file, destination_and_name)
    # adjust import by replacing template with sol+current_day
    with open(destination_and_name, 'r') as file:
        filedata = file.read()
        filedata = filedata.replace("template", f"sol{current_day}")
        with open(destination_and_name, 'w') as file:
            file.write(filedata)