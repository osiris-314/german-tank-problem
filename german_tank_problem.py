#!/usr/local/env python3
from colorama import Fore

def calculate_n(observations):
    observations.sort()

    max_observation = max(observations)
    min_observation = min(observations)

    gap = abs(1 - min_observation)

    def find_avg_gap(observations):
        last_observation = 0
        global gaps_list
        gaps_list = []
        for observation in observations:
            if observation == min_observation:
                gaps_list.append(int(gap))
                last_observation = observation
            else:
                gaps_list.append(int(abs(observation - last_observation) - 1))
                last_observation = observation

    k = len(observations)
    find_avg_gap(observations)
    gaps_sum = sum(gaps_list)
    n = max_observation + (gaps_sum / k)
    return n

file_path = 'observations.txt'

results = []

with open(file_path, 'r') as file:
    for line in file:
        observations = list(map(int, line.strip().split(',')))
        n = calculate_n(observations)
        results.append(n)

for i, result in enumerate(results):
    print(Fore.LIGHTBLUE_EX + str(i+1) + ': ' + Fore.LIGHTGREEN_EX + str(result))

if len(results) > 1:
    average_result = sum(results) / len(results)
    print('\n' + Fore.LIGHTGREEN_EX + 'Average: ' + Fore.LIGHTBLUE_EX + str(round(average_result,2)) + Fore.RESET)
