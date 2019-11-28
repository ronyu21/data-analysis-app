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

    # output the dictionary as shown in the email day 1
    # key - value
    # for key, val in data_dict.items():
    #     print(key, ' - ', val)

    # day 2
    print("All data from Emissions.csv has been read into a dictionary\n")
    # wait for user input
    target_year = input("Select a year to find statics (1997 to 2010): ")

    # find the index of the user input
    header_row_key = "CO2 per capita"
    index = None
    years = data_dict.get(header_row_key)
    temp_idx = 0
    for year in years:
        if target_year == year:
            index = temp_idx
            break
        temp_idx += 1

    if index is None:
        print("User entered an invalid year: {}".format(target_year))
        exit(-1)

    # extract the emissions for the target year
    target_year_emissions = []
    target_year_emission_countries = []
    for k, v in data_dict.items():
        if k == header_row_key:
            continue
        else:
            target_year_emissions.append(float(v[index]))
            target_year_emission_countries.append(k)

    # calculate the min, max, average
    min_val = min(target_year_emissions)
    min_val_country = target_year_emission_countries[target_year_emissions.index(min_val)]
    max_val = max(target_year_emissions)
    max_val_country = target_year_emission_countries[target_year_emissions.index(max_val)]
    avg_val = sum(target_year_emissions) / len(target_year_emissions)

    # output the result as shown in email
    print('In {}, countries with minimum and maximum CO2 emission levels were [{}] and [{}] respectively.'.format(
        target_year, min_val_country, max_val_country))
    print('Average CO2 emissions in {} were {:0.6f}'.format(target_year, avg_val))
