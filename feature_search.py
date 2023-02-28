# feature_search.py

import sys
from accuracy import random_accuracy

def feature_search(data):
    
    current_feature_set = []

    # For-loop to "walk" down the search tree
    for i in range(1, len(data[0])):

        print(f'We are on level {i}.')

        feature_to_add_at_this_level = 0
        best_accuracy_so_far = 0

        # Consider each feature separately
        for j in range(1, len(data[0])):

            # Check if the feature is already in our feature set
            if j not in current_feature_set:
                
                print(f'\tConsidering adding feature {j}.')

                # Compute accuracy
                accuracy = random_accuracy()
                if accuracy > best_accuracy_so_far:
                    best_accuracy_so_far = accuracy
                    feature_to_add_at_this_level = j
            else:
                print(f'\tFeature {j} is already in our feature set.')

        print(f'On level {i}, we will add feature {feature_to_add_at_this_level} to the current set.')
        current_feature_set.append(feature_to_add_at_this_level)

        # Print out current feature set
        print('Current feature set right now:')
        print(current_feature_set)

if __name__ == "__main__":
    sys.exit('Don\'t run this module directly.')