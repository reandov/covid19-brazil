import matplotlib.pyplot as plt

# Regional accumulated
def plot_regional_acc(dataset, region_list, last_available_date):
    # Creating the figure
    fig, axs = plt.subplots(2, 1, figsize=(12, 14), dpi=100)
    
    # Customizing the figure
    fig.subplots_adjust(top=0.92)
    fig.autofmt_xdate(rotation=0, ha='center')
    fig.suptitle("Número de Casos e Óbitos acumulados de COVID-19 nas Regiões do Brasil até %s/%s/%s" % (last_available_date[-2:], last_available_date[5:7], last_available_date[0:4]))
    fig.text(.5, .09, "Autor: Evandro Rodrigues | Fonte: Brasil.IO em: %s/%s/%s" % (last_available_date[-2:], last_available_date[5:7], last_available_date[0:4]), ha='center', fontsize="14", fontweight=600)

    # Adding data to the axis (accumulated cases/deaths)
    for index in range(0, len(region_list)):
        regional_dataset = dataset[dataset["region"] == region_list[index]]
        axs[0].plot(regional_dataset["date"], regional_dataset["accumulated_num_cases"], label = ("Região " + region_list[index]))
        axs[1].plot(regional_dataset["date"], regional_dataset["accumulated_num_deaths"], label = ("Região " + region_list[index]))

    # Customizing axis
    axs[0].set_title("Número de casos confirmados (acumulados)")
    axs[0].set_xlabel("Data")
    axs[0].set_ylabel("Nº de Casos")
    axs[1].set_title("Número de óbitos confirmados (acumulados)")
    axs[1].set_xlabel("Data")
    axs[1].set_ylabel("Nº de Óbitos")
    
    # For each axis apply ->
    for ax in axs:
        ax.yaxis.get_major_formatter().set_scientific(False)
        ax.legend(prop=dict(weight='bold'))
    
    # Saving the chart
    plt.savefig("images/regions/01_regional_acc.png")
    
    return plt.close()

# Regional daily
def plot_regional_daily(dataset, region_list, last_available_date):
    
    # Specifying the regional data to today's date
    dataset = dataset[dataset["date"] == last_available_date]
    
    # Gathering number of new cases and new deaths
    n_cases = list(dataset.new_num_cases)
    n_deaths = list(dataset.new_num_deaths)
    
    # Creating the figure
    fig, axs = plt.subplots(2, 1, figsize=(12, 14), dpi=100)

    # Customizing the figure
    fig.subplots_adjust(top=0.92)
    fig.autofmt_xdate(rotation=0, ha='center')
    fig.suptitle("Número de Casos e Óbitos de HOJE de COVID-19 nas Regiões do Brasil até %s/%s/%s" % (last_available_date[-2:], last_available_date[5:7], last_available_date[0:4]))
    fig.text(.5, .09, "Autor: Evandro Rodrigues | Fonte: Brasil.IO em: %s/%s/%s" % (last_available_date[-2:], last_available_date[5:7], last_available_date[0:4]), ha='center', fontsize="14", fontweight=600)

    # Adding data to the axis
    axs[0].pie(list(map(lambda x: (x / sum(n_cases)) * 100, n_cases)), labels=region_list, autopct='%1.2f%%', shadow=False, startangle=90, textprops=dict(fontweight="bold", fontsize=12))
    axs[0].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    axs[1].pie(list(map(lambda x: (x / sum(n_deaths)) * 100, n_deaths)), labels=region_list, autopct='%1.2f%%', shadow=False, startangle=90, textprops=dict(fontweight="bold", fontsize=12))
    axs[1].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Customizing axis
    axs[0].set_title("Número de casos confirmados (diário)")  
    axs[1].set_title("Número de óbitos confirmados (diário)")
     
    # For each axis apply ->
    for ax in axs:
        ax.legend(prop=dict(weight='bold'))
    
    # Saving the chart
    plt.savefig("images/regions/02_regional_new.png")
    
    return plt.close()