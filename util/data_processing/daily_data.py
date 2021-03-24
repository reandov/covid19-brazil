import pandas as pd

from util.extra_functions.aux_functions import save_dataset

def process_daily_data(dataset, last_available_date):
  daily_data = dataset[dataset["date"] == last_available_date]

  save_dataset(daily_data, 'data/daily/covid19-dataset-today.csv')

  return daily_data
  