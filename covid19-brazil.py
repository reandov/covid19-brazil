## Importations
import pandas as pd
import matplotlib.pyplot as plt
import time

from util.data_preprocessing.get_data import download_dataset, data_cleaning
from util.data_processing.national_data import process_national_data
from util.data_processing.regional_data import process_regional_data
from util.data_visualization.national_plots import plot_national_acc, plot_national_daily
from util.data_visualization.state_plots import plot_state_acc, plot_state_daily
from util.data_visualization.regional_plots import plot_regional_acc, plot_regional_daily
from util.data_visualization.extra_plots import plot_epidemiological_weeks
from util.extra_functions.aux_functions import generate_report

# Creating a dictionary of regions and states
region_list = ["Norte", "Nordeste", "Centro-Oeste", "Sudeste", "Sul"]

regions = {
    "Norte" : ["AC", "AP", "AM", "TO", "PA", "RR", "RO"],
    "Nordeste" : ["AL", "BA", "PB", "PE", "SE", "PI", "CE", "MA", "RN"],
    "Centro-Oeste" : ["MT", "GO", "MS", "DF"],
    "Sudeste" : ["SP", "ES", "RJ", "MG"],
    "Sul" : ["SC", "RS", "PR"],
}

## Defining the style for plottings
plt.style.use(["seaborn-whitegrid", "./styles/custom_style.mplstyle"])

## Main
def main():
        
    print("=== COVID 19 - BRAZIL ===\n")
    print("> Downloading the dataset (caso_full.csv) from | data.brasil.io/dataset/covid19/ |")
    
    covid_dataset = download_dataset()
    
    print("  - Download completed.\n")
    print("> Initiating dataset cleaning.")
    
    covid_dataset, last_available_date = data_cleaning(covid_dataset, regions)
    
    # Creating a list from the first case until today
    date_list = pd.date_range(start = "2020-02-25", end = last_available_date)
    
    print("  - Data cleaning completed.\n")
    print("> Processing national data.")
    
    national_data = process_national_data(covid_dataset, date_list, last_available_date)
    
    print("  - National data acquired.\n")
    print("> Processing regional data.")
    
    regional_data = process_regional_data(covid_dataset, region_list, date_list, last_available_date)
    
    print("  - Regional data acquired.\n")
    print("> Generating plots.")
    
    plot_national_acc(national_data, last_available_date)
    plot_national_daily(national_data, last_available_date)
    plot_epidemiological_weeks(national_data, last_available_date)
    plot_state_acc(covid_dataset, last_available_date)
    plot_state_daily(covid_dataset, last_available_date)
    plot_regional_acc(regional_data, region_list, last_available_date)
    plot_regional_daily(regional_data, region_list, last_available_date)
    
    print("  - Plots generated.\n")
    print("> Returning dataframes.")
    print("  - DataFrames returned.\n")
    
    print("> Generating report")
    
    generate_report(national_data, last_available_date)
    
    print("  - Report generated.\n")
    
    print("Exiting the application.\n")
    
    return covid_dataset, national_data, regional_data

## Extra
# Starting timer
start_time = time.time()

# Running main function
covid_dataset, national_data, regional_data = main()

# Ending and printing the runtime
print("This script runtime was: %s seconds ---" % (time.time() - start_time))