# main.py
# This script runs a greedy feature selection algorithm

from feature_search import feature_search
from feature_search import backward_elimination
from read_data import read_data
import sys

print('Welcome to Vinayak Gajjewar (vgajj002)\'s feature selection algorithm.')

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
data_arr = read_data('small-test-dataset.txt')

# Do feature search
if alg_number == 1:
    feature_search(data_arr)
elif alg_number == 2:
    backward_elimination(data_arr)
else:
    sys.exit('Error: invalid input.')