import matplotlib.pyplot as plt

# Epidemiological
def plot_epidemiological_weeks(dataset, last_available_date):
    
    # Shortcuts for nice plotting
    weeks = dataset["epidemiological_week"].unique()
    n_cases = [dataset[dataset["epidemiological_week"] == week].new_num_cases.sum() for week in weeks]
    n_deaths = [dataset[dataset["epidemiological_week"] == week].new_num_deaths.sum() for week in weeks]
      
    # Creating the figure
    fig, axs = plt.subplots(2, 1, figsize=(12, 14), dpi=100)

    # Customizing the figure
    fig.subplots_adjust(top=0.92)
    fig.suptitle("Número de Casos e Óbitos de COVID-19 p/ Semana Epidemiológica no Brasil")
    fig.text(0.43, 0.060, ("Semana atual: " + str(dataset["epidemiological_week"].iat[-1])[-2:] + " de " + last_available_date[0:4]), fontsize=14, fontweight="bold")
    fig.text(0.5, 0.035, "Autor: Evandro Rodrigues | Fonte: Brasil.IO em: %s/%s/%s" % (last_available_date[-2:], last_available_date[5:7], last_available_date[0:4]), ha='center', fontsize="14", fontweight=600)

    # Adding data to the axis (accumulated cases/deaths)  
    axs[0].bar(range(len(weeks)), n_cases, align='center')
    axs[1].bar(range(len(weeks)), n_deaths, align='center', color="red")
    
    # Customizing axis
    axs[0].set_title("Número de casos p/ semana")
    axs[0].set_xlabel("Data")
    axs[0].set_ylabel("Nº de Casos")
    axs[1].set_title("Número de óbitos p/ semana")
    axs[1].set_xlabel("Data")
    axs[1].set_ylabel("Nº de Óbitos")
    axs[0].set_xticks(range(len(weeks)))
    axs[0].set_xticklabels([(str(week)[-2:] + "-" + str(week)[:4]) for week in list(weeks)])
    axs[1].set_xticks(range(len(weeks)))
    axs[1].set_xticklabels([(str(week)[-2:] + "-" + str(week)[:4]) for week in list(weeks)])
    axs[0].xaxis.set_major_locator(plt.MaxNLocator(8))
    axs[1].xaxis.set_major_locator(plt.MaxNLocator(8))
    axs[0].tick_params(axis='x', which='both', length=5, width=1.5, color='lightgray')
    axs[1].tick_params(axis='x', which='both', length=5, width=1.5, color='lightgray')

    # Saving the chart
    plt.savefig("images/03_epidemiological_weeks.png")
    
    return plt.close()