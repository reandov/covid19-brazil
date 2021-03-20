import pandas as pd

#import extra_functions
from util.extra_functions.aux_functions import save_dataset

def process_state_split_data(state_list, dataset, date_list, last_available_date):
    
    # Iterating over each state
    for state in state_list:
        
        # Creating auxiliary lists
        acc_cases = []
        acc_deaths = []
        n_cases = []
        n_deaths = []
        
        # Querying dataset accordinly with the state
        sample = dataset[dataset['state'] == state]
        
        # Iterating over each date
        for date in date_list[:-1]:

            # Summing over all data for specific date
            summatory = sample[sample['date'] == date.strftime("%Y-%m-%d")].sum()

            # Getting summed data of each column
            acc_cases.append(summatory[6])
            acc_deaths.append(summatory[7])
            n_cases.append(summatory[8])
            n_deaths.append(summatory[9])
            
        # For today's data
        # Summing over all data for specific date
        summatory = sample[sample["is_last"] == True].sum()

        # Getting summed data of each column
        acc_cases.append(summatory[6])
        acc_deaths.append(summatory[7])
        n_cases.append(summatory[8])
        n_deaths.append(summatory[9])
        
        # Creating a new DataFrame of the processed data
        state_dataframe = pd.DataFrame({"date": pd.date_range(start = "2020-02-25", end = last_available_date), 
                                           "country": "Brazil",
                                           "state": state,
                                           "accumulated_num_cases": map(int, acc_cases), 
                                           "accumulated_num_deaths": map(int, acc_deaths),
                                           "new_num_cases": map(int, n_cases),
                                           "new_num_deaths": map(int, n_deaths)
                                          })

        # Saving the dataset

        save_dataset(state_dataframe, f"data/states/{state}/covid19-dataset-{state}.csv")