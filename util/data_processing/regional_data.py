import pandas as pd

from util.extra_functions.aux_functions import save_dataset

## Function used to get/process information about the regions in Brazil
def process_regional_data(dataset, region_list, date_list, last_available_date):
    
    # Creating a global list (scope)
    dataframe_list = []
    
    # Iterating over each region
    for region in region_list:
        
        # Creating auxiliary lists
        acc_cases = []
        acc_deaths = []
        n_cases = []
        n_deaths = []
        
        # Specifying the dataset
        temp_dataset = dataset[dataset["region"] == region]
        
        # Iterating over each date
        for date in date_list[:-1]:
            
            # Summing over all data for specific date
            summatory = temp_dataset[temp_dataset['date'] == date.strftime("%Y-%m-%d")].sum()
            
            # Getting summed data of each column
            acc_cases.append(summatory[6])
            acc_deaths.append(summatory[7])
            n_cases.append(summatory[8])
            n_deaths.append(summatory[9])
            
        # Summing over all data for specific date
        summatory = temp_dataset[temp_dataset['is_last'] == True].sum()

        # Getting summed data of each column
        acc_cases.append(summatory[6])
        acc_deaths.append(summatory[7])
        n_cases.append(summatory[8])
        n_deaths.append(summatory[9])
        
        # Generating a new DataFrame for each region and storing at r_data
        dataframe_list.append(pd.DataFrame({"date": pd.date_range(start = "2020-02-25", end = last_available_date),
                                            "region": region,
                                            "accumulated_num_cases": map(int, acc_cases),
                                            "accumulated_num_deaths": map(int, acc_deaths),
                                            "new_num_cases": map(int, n_cases),
                                            "new_num_deaths": map(int, n_deaths)
                                           }))
        
    # Batch dataset saving
    for index, region in enumerate(region_list):
        save_dataset(dataframe_list[index], (f"data/covid19-{region}.csv"))
    
    # Returning a list of 5 DataFrames
    dataframe_list = pd.concat([dataframe_list[0], dataframe_list[1], dataframe_list[2], dataframe_list[3], dataframe_list[4]])
    
    return dataframe_list