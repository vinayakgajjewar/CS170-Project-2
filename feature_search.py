# feature_search.py

import sys
from validator import Validator


def feature_search(data):

    # Initialize validator
    v = Validator()

    # Start with an empty feature set
    current_feature_set = []

    # Best accuracy overall
    # We use this variable to find out when our accuracy starts decreasing
    best_acc_overall = 0
    best_feature_set_overall = []

    # For-loop to "walk" down the search tree
    for i in range(1, len(data[0])):

        print(f'We are on level {i} of the search tree.')

        feature_to_add_at_this_level = None
        best_accuracy_so_far = 0

        # Consider each feature separately
        for j in range(1, len(data[0])):

            # Check if the feature is already in our feature set
            if j not in current_feature_set:


                #print(f'\tConsidering adding feature {j}.')

                # Compute accuracy
                # TODO: IDK IF THIS IS HOW YOU DO IT
                new_feature_set = current_feature_set + [j]
                accuracy = v.leave_one_out_cross_validation(data, new_feature_set)
                if accuracy > best_accuracy_so_far:
                    best_accuracy_so_far = accuracy
                    feature_to_add_at_this_level = j
            else:
                pass
                #print(f'\tFeature {j} is already in our feature set.')

        print(f'On level {i}, we will add feature {feature_to_add_at_this_level} to the current set.')
        current_feature_set.append(feature_to_add_at_this_level)

        # Print out current feature set
        print('Current feature set:')
        print(current_feature_set)

        # TODO: how can I check when our accuracy starts decreasing
        print(f'Accuracy at level {i} = {best_accuracy_so_far}.')

        # Update best accuracy overall
        if best_accuracy_so_far > best_acc_overall:
            best_acc_overall = best_accuracy_so_far
            best_feature_set_overall = current_feature_set
        else:
            print('Warning: accuracy has decreased or leveled off')

        print()
    
    # Now let's print out our all-time best accuracy and the feature set that got it
    print(f'Our final accuracy is {best_acc_overall} with feature set {best_feature_set_overall}.')


def backward_elimination(data):
    
    # Initialize validator
    v = Validator()

    # Start with a full feature set
    current_feature_set = list(range(len(data[0])))

    # For-loop to walk down the search tree
    # i starts at 1 because we don't want the label
    for i in range(1, len(data[0])):
        print(f'We are on level {i} of the search tree.')

        feature_to_omit_at_this_level = None
        best_accuracy_so_far = 0

        # Consider omitting each feature separately
        # j starts at 1 because we don't want the label
        for j in range(1, len(data[0])):

            # Only conside omitting a feature if it's in our feature set
            if j in current_feature_set:

                # Compute accuracy
                new_feature_set = current_feature_set[:]
                new_feature_set.remove(j)
                accuracy = v.leave_one_out_cross_validation(data, new_feature_set)
                if accuracy > best_accuracy_so_far:
                    best_accuracy_so_far = accuracy
                    feature_to_omit_at_this_level = j
        
        print(f'On level {i}, we will omit feature {feature_to_omit_at_this_level} from the current set.')
        current_feature_set.remove(feature_to_omit_at_this_level)

        # Print out current feature set
        print('Current feature set:')
        print(current_feature_set)

        print(f'Accuracy at level {i} = {best_accuracy_so_far}.')

if __name__ == "__main__":
    sys.exit('Don\'t run this module directly.')