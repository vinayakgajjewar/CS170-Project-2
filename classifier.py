# classifier.py

import math

class Classifier():

    # Data set to use when predicting new instances
    train_data = []

    # Feature set to use when predicting new instances
    feature_set = []

    def train(self, training_data, feature_set):
        self.train_data = training_data
        self.feature_set = feature_set

    # Calculate the distance between two data points
    # Only use the features in the feature set
    # point1 and point2 are lists of the same length
    def calc_distance(self, point1, point2):
        sum = 0
        for i in range(len(point1)):
            if i in self.feature_set:
                sum += (point2[i] - point1[i]) ** 2
        return math.sqrt(sum)

    # Returns the predicted label of the test instance
    # test_instance
    def test(self, test_instance):

        # To keep track of the current nearest neighbor
        nearest_neighbor_dist = math.inf
        nearest_neighbor_label = -1
        
        # Loop through every data point in our training set
        for i in range(len(self.train_data)):

            # Calculate distance
            # First we need to remove the labels from our training data
            distance = self.calc_distance(test_instance, self.train_data[i][1:])

            # Check if it's the shortest distance we've observed so far
            if distance < nearest_neighbor_dist:
                nearest_neighbor_dist = distance
                nearest_neighbor_label = int(self.train_data[i][0])
        
        # When we finish looping through the training data, return the nearest label
        return nearest_neighbor_label