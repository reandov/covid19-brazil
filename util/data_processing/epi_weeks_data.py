import pandas as pd

from util.extra_functions.aux_functions import save_dataset

def process_epi_weeks_data(dataset):
    
    # Shortcuts for nice plotting
    weeks = dataset["epidemiological_week"].unique()
    weeks_formatted = list(map(lambda week: week[-2:] + "-" + week[:4], map(str, weeks)))
    n_cases = [dataset[dataset["epidemiological_week"] == week].new_num_cases.sum() for week in weeks]
    n_deaths = [dataset[dataset["epidemiological_week"] == week].new_num_deaths.sum() for week in weeks]
    
    epi_weeks_dataset = pd.DataFrame({"epidemiological_week": weeks_formatted, 
                                      "new_cases": n_cases, 
                                      "new_deaths": n_deaths
                                     })
    
    save_dataset(epi_weeks_dataset, "./data/extras/covid19-dataset-epi-weeks.csv")
    
    return epi_weeks_dataset