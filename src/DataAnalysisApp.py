from typing import List

from src.FileHandling import load_csv_to_2d_list

if __name__ == "__main__":

    # load from csv file and save as a list
    data_list = load_csv_to_2d_list('./resource/Emissions.csv')

    # transform the list to become dictionary
    # with the first item as key, the remaining list as value
    data_dict = dict()
    for item in data_list:
        key = item[0]
        value = item[1:]
        data_dict.setdefault(key, value)

    # output the dictionary as shown in the email
    # key - value
    for key, val in data_dict.items():
        print(key, ' - ', val)

