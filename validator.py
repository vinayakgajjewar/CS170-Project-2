# validator.py

import random
import math
from read_data import read_data

class Validator():

    def __init__(self):
        print('Initializing validator.')

    # Return a random accuracy value
    # For testing purposes
    def random_accuracy(self):
        return random.random()

    # Calculate the distance between two data points
    # We use this function in leave-one-out cross validation
    def calc_distance(self, point1, point2):
        sum = 0
        for i in range(len(point1)):
            sum += (point2[i] - point1[i]) ** 2
        return math.sqrt(sum)

    # Leave-one-out cross validation
    def leave_one_out_cross_validation(self, data):

        # Loop through data points
        for i in range(len(data)):

            # To keep track of the current nearest neighbor
            nearest_neighbor_dist = math.inf
            nearest_neighbor = -1
            nearest_neighbor_label = -1.0

            print(f'We are on data point {i}.')
            print(f'Label = {int(data[i][0])}.')

            # Loop through every other data point
            for j in range(len(data)):

                # Don't compare a point to itself
                if i != j:
                    #print(f'\tComparing point {i} to point {j}.')

                    # Calculate distance
                    # First we get rid of the labels cuz we don't need them here
                    distance = self.calc_distance(data[i][1:], data[j][1:])

                    # Check if it's the shortest distance we've observed so far
                    if distance < nearest_neighbor_dist:
                        nearest_neighbor_dist = distance
                        nearest_neighbor = j
                        nearest_neighbor_label = int(data[j][0])

            # Now that we've found the nearest neighbor
            # Print it out
            print(f'It\'s nearest neighbor is {nearest_neighbor} which has label {nearest_neighbor_label}.')


# For testing lol
if __name__ == '__main__':
    data = read_data('small-test-dataset.txt')
    v = Validator()
    v.leave_one_out_cross_validation(data)