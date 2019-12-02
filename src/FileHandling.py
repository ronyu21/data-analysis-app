from typing import List
import csv


def load_csv_to_2d_list(filename: str) -> List[List]:
    result_list: List[List] = []
    # open the csv file
    with open(filename, 'rt') as csv_file:
        # use CSV lib to read the csv file
        data = csv.reader(csv_file)
        # append the row data to the result list
        for row in data:
            result_list.append(row)

    return result_list


def load_csv_to_2d_list_plain(filename: str) -> List[List]:
    result_list: List[List] = []
    # open the csv file
    with open(filename, 'rt') as csv_file:
        # read the lines in the csv file one by one
        for line in csv_file:
            # remove the newline symbol, then split the string by comma
            data = line.rstrip('\n').split(',')
            # append the row data to result list
            result_list.append(data)

    return result_list


def save_data_to_csv(filename: str, data_list: List[str]) -> None:
    with open(filename, 'wt') as csv_file:
        csv_file.writelines(data_list)

