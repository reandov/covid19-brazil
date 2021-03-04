import pandas as pd
import csv
import gzip
import io
from urllib.request import Request, urlopen

from util.extra_functions import save_dataset, get_region

## Function to download and save the dataset
def download_dataset():
    
    # Downloads the dataset from request/response
    request = Request("https://data.brasil.io/dataset/covid19/caso_full.csv.gz", headers={"User-Agent": "python-urllib"})
    response = urlopen(request)
    
    # Create a DataFrame from dictionary
    dataset = pd.DataFrame.from_dict(csv.DictReader(io.StringIO(gzip.decompress(response.read()).decode("utf-8"))))
    
    # Saves the dataset
    save_dataset(dataset, "data/covid19-dataset-brasil-io.csv")
    
    # Returns the reading of the saved dataset (This process it's necessary in order to avoid type errors and possible errors during data reading)
    return pd.read_csv("data/covid19-dataset-brasil-io.csv")

## Dataset cleaning
def data_cleaning(dataset):
    
    # List of columns that will be droped
    columns_to_drop = ["city", "city_ibge_code", "estimated_population_2019", "is_repeated", "last_available_confirmed_per_100k_inhabitants", "last_available_death_rate", "order_for_place", "place_type"]
    
    # Droping the columns and resetting the indexes;
    dataset = (dataset[~dataset["place_type"].isin(["city"])]
                .drop(columns_to_drop, axis=1)
                .reset_index(drop=True))
    
    # Adding the "Region" column (refer to the getRegion utility function)
    dataset['region'] = list(map(get_region, dataset.state.tolist()))
    
    # Reordering and renaming columns
    dataset = (dataset[['date', 'last_available_date', "is_last", 'region', 'state', 'epidemiological_week', 'last_available_confirmed', 'last_available_deaths', 'new_confirmed', 'new_deaths']]
               .rename(columns={"last_available_confirmed": "accumulated_cases",
                                 "new_confirmed": "new_cases",
                                 "last_available_deaths": "accumulated_deaths",
                                 "new_deaths": "new_deaths",
                                }))
    
    # Saving the updated dataset
    save_dataset(dataset, "data/covid19-dataset-brasil-io_cleaned.csv")
    
    return dataset, dataset.last_available_date.max()