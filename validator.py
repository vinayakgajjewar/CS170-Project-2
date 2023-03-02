# validator.py

import random
from read_data import read_data

class Validator():

    def __init__(self):
        print('Initializing validator.')

    # Return a random accuracy value
    # For testing purposes
    def random_accuracy(self):
        return random.random()

    # Leave-one-out cross validation
    def leave_one_out_cross_validation(self, data):
        
        # Loop through data points
        i = 0
        for row in data:
            print(f'We are on data point {i}.')
            print(f'Label = {int(row[0])}.')

            # Loop through every other data point
            j = 0
            for other_row in data:

                # Don't compare a point to itself
                if i != j:
                    print(f'\tComparing point {i} to point {j}.')
                j += 1

            i += 1


# For testing lol
if __name__ == '__main__':
    data = read_data('small-test-dataset.txt')
    v = Validator()
    v.leave_one_out_cross_validation(data)