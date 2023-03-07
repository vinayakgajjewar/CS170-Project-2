# validator.py

import random
import math
from read_data import read_data

class Validator():

    # Return a random accuracy value
    # For testing purposes
    def random_accuracy(self):
        return random.random()

    # Calculate the distance between two data points
    # We use this function in leave-one-out cross validation
    # Only use the features in the feature set
    def calc_distance(self, point1, point2, feature_set):
        sum = 0

        # Start at 1 so we can skip the label
        for i in range(len(point1)):

            # We have to do i+1 here because feature_set is 1-indexed not 0-indexed
            if (i + 1) in feature_set:
                sum += (point2[i] - point1[i]) ** 2
        return math.sqrt(sum)

    # Leave-one-out cross validation
    # feature_set is a list of indices (the first index is 1)
    def leave_one_out_cross_validation(self, data, feature_set):

        # Keep track of the number of correctly-classified instances
        num_correct = 0

        # Loop through data points
        for i in range(len(data)):

            # To keep track of the current nearest neighbor
            nearest_neighbor_dist = math.inf
            nearest_neighbor = -1
            nearest_neighbor_label = -1.0

            #print(f'We are on data point {i}.')
            #print(f'Label = {int(data[i][0])}.')

            # Loop through every other data point
            for j in range(len(data)):

                # Don't compare a point to itself
                if i != j:
                    #print(f'\tComparing point {i} to point {j}.')

                    # Calculate distance
                    distance = self.calc_distance(data[i][1:], data[j][1:], feature_set)

                    # Check if it's the shortest distance we've observed so far
                    if distance < nearest_neighbor_dist:
                        nearest_neighbor_dist = distance
                        nearest_neighbor = j
                        nearest_neighbor_label = int(data[j][0])

            # Now that we've found the nearest neighbor
            # Check if they share the same label
            #print(f'It\'s nearest neighbor is {nearest_neighbor} which has label {nearest_neighbor_label}.')
            if nearest_neighbor_label == data[i][0]:

                # Why doesn't Python let me just do num_correct++ ?
                num_correct += 1

        # Calculate accuracy
        accuracy = num_correct / len(data)
        #print(f'The accuracy is {accuracy}.')
        return accuracy

# For testing lol
if __name__ == '__main__':
    data = read_data('small-test-dataset.txt')
    v = Validator()
    # [1, 15, 27] for Large-test-dataset.txt
    # [3, 5, 7] for small-test-dataset.txt
    print(v.leave_one_out_cross_validation(data, [3, 5, 7]))