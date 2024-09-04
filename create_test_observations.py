import random
from colorama import Fore

file_name = 'test_observations.txt'

number_of_rows = 10000
min_value = 1
max_value = 125
number_of_observations_per_row = 5

with open(file_name, 'w') as file:
    file.truncate(0)

with open(file_name, 'w') as file:
    for _ in range(number_of_rows):
        random_numbers = [str(random.randint(min_value, max_value)) for _ in range(number_of_observations_per_row)]
        file.write(','.join(random_numbers) + '\n')

print(Fore.LIGHTBLUE_EX + str(number_of_rows) + Fore.WHITE + ' rows of random numbers have been written to ' + Fore.LIGHTYELLOW_EX + str(file_name) + Fore.RESET)
