# main.py
# This script runs a greedy feature selection algorithm

import csv
from feature_search import feature_search

print('Welcome to Vinayak Gajjewar\'s feature selection algorithm.')

# Get total number of features from user
print('Please enter the total number of features: ', end='')
num_features = int(input())

# Get algorithm from user
print('Which algorithm do you want to run?')
print('\t1) Forward selection')
print('\t2) Backward elimination')
print('\t3) My special algorithm')
print('Your choice: ', end='')
alg_number = int(input())

# Read data file
with open('small-test-dataset.txt') as test_data:
    data_reader = csv.reader(test_data, delimiter='\t')
    data_arr = []
    for row in data_reader:
        print(row)
        data_arr.append(row)
    feature_search(data_arr)