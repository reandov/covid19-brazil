import pandas as pd

from util.extra_functions.aux_functions import save_dataset

## Function used to get/process information about the whole country (Brazil)
def process_national_data(dataset, date_list, last_available_date):
    
    # Creating auxiliary lists
    acc_cases = []
    acc_deaths = []
    n_cases = []
    n_deaths = []
    epi_week = []
    
    # Iterating over each date
    for date in date_list[:-1]:
        
        # Summing over all data for specific date
        summatory = dataset[dataset['date'] == date.strftime("%Y-%m-%d")].sum()
        
        # Getting the epidemiological week for each date
        epi_week.append(dataset[dataset['date'] == date.strftime("%Y-%m-%d")].epidemiological_week.iat[0])
        
        # Getting summed data of each column
        acc_cases.append(summatory[6])
        acc_deaths.append(summatory[7])
        n_cases.append(summatory[8])
        n_deaths.append(summatory[9])
    
    # For today's data
    # Summing over all data for specific date
    summatory = dataset[dataset["is_last"] == True].sum()

    # Getting the epidemiological week for each date
    epi_week.append(dataset[dataset['date'] == last_available_date].epidemiological_week.iat[0])

    # Getting summed data of each column
    acc_cases.append(summatory[6])
    acc_deaths.append(summatory[7])
    n_cases.append(summatory[8])
    n_deaths.append(summatory[9])
    
    
    # Creating a new DataFrame of the processed data
    national_dataframe = pd.DataFrame({"date": pd.date_range(start = "2020-02-25", end = last_available_date), 
                                       "country": "Brazil", 
                                       "epidemiological_week": epi_week, 
                                       "accumulated_num_cases": acc_cases, 
                                       "accumulated_num_deaths": acc_deaths,
                                       "new_num_cases": n_cases,
                                       "new_num_deaths": n_deaths
                                      })
    
    # Saving the dataset
    save_dataset(national_dataframe, "data/covid19-dataset-brasil-io.csv")
    
    # Returning generated DataFrame
    return national_dataframe