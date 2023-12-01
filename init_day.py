import os
from datetime import date

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

# 
