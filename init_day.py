import os
from datetime import date

today = date.today()
current_day = today.strftime('%d')
current_year = today.strftime('%Y')

new_directory = os.path.join(current_year, current_day)

current_working_directory = os.getcwd()

assembled_path = os.path.join(current_working_directory, new_directory)

os.mkdir(assembled_path)



