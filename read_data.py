# read_data.py

import csv

# read_data returns a 2D array of floats
def read_data(filename):
    with open(filename) as file:

        # Use ' ' as delimiter
        csv_reader = csv.reader(file, delimiter=' ')
        data_arr = []
        for row in csv_reader:
            data_row = []
            for elem in row:

                # We need to filter out those pesky whitespaces
                if elem != '':

                    # Convert from scientific notation to floating-point
                    data_row.append(float(elem))
            data_arr.append(data_row)
        #print(data_arr)
        return data_arr

# For testing purposes
if __name__ == '__main__':
    print(read_data('small-test-dataset.txt'))