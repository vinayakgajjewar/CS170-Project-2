# main.py
# This script runs a greedy feature selection algorithm

from feature_search import forward_selection
from feature_search import backward_elimination
from read_data import read_data
from validator import Validator
import sys

print('Welcome to Vinayak Gajjewar (vgajj002)\'s feature selection algorithm.')

# Ask user what file they want to test
print('Type in the name of the data file you want to test: ', end='')
filename = input()

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
data_arr = read_data(filename)

# Print dataset attributes
num_features = len(data_arr[0]) - 1
num_instances = len(data_arr)
print(f'This dataset has {num_features} features and {num_instances} instances.')

# TODO: normalize data?
# Give baseline accuracy (with no features)
v = Validator()
baseline_accuracy = v.leave_one_out_cross_validation(data_arr, [])
print(f'With no feature set, we have a baseline accuracy of {baseline_accuracy}.')

# Do feature search
if alg_number == 1:
    forward_selection(data_arr)
elif alg_number == 2:
    backward_elimination(data_arr)
else:
    sys.exit('Error: invalid input.')