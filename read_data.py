# read_data.py

import csv

def read_data(filename):
    with open(filename) as file:
        csv_reader = csv.reader(file, delimiter=' ')
        data_arr = []
        for row in csv_reader:
            data_row = []
            for elem in row:
                if elem != '':
                    data_row.append(float(elem))
            data_arr.append(data_row)
        #print(data_arr)
        return data_arr

if __name__ == '__main__':
    print(read_data('small-test-dataset.txt'))