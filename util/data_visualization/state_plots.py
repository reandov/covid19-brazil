import matplotlib.pyplot as plt

# State accumulated
def plot_state_acc(dataset, last_available_date):
    
    # Specifying the dataset for today
    dataset = dataset[dataset["date"] == last_available_date]
    
    # Generating an annotation
    not_updated = dataset[dataset["last_available_date"] != last_available_date].state.tolist()
    str_upd = ""
    
    for state in not_updated:
        str_upd += ("%s " % (state))
        
    # Creating the figure
    fig, axs = plt.subplots(2, 1, figsize=(12, 14), dpi=100)

    # Customizing the figure
    fig.subplots_adjust(top=0.92)
    fig.suptitle("Número de Casos e Óbitos acumulados de COVID-19 nos Estados do Brasil até %s/%s/%s" % (last_available_date[-2:], last_available_date[5:7], last_available_date[0:4]))
    fig.text(0.40, 0.063, ("Estados ainda não atualizados: " + str_upd), fontsize=12)
    fig.text(0.5, 0.038, "Autor: Evandro Rodrigues | Fonte: Brasil.IO em: %s/%s/%s" % (last_available_date[-2:], last_available_date[5:7], last_available_date[0:4]), ha='center', fontsize="14", fontweight=600)
    
    # Adding data to the axis (accumulated cases/deaths)
    axs[0].bar(dataset["state"], dataset["accumulated_cases"], color="#1F77B4", align='center')
    axs[1].bar(dataset["state"], dataset["accumulated_deaths"], color="red", align='center')
    
    # Customizing axis
    axs[0].set_title("Número de casos confirmados (acumulados)")
    axs[0].set_xlabel("Data")
    axs[0].set_ylabel("Nº de Casos")
    axs[1].set_title("Número de óbitos confirmados (acumulados)")
    axs[1].set_xlabel("Data")
    axs[1].set_ylabel("Nº de Óbitos")
    
    # For each axis apply ->
    for ax in axs:
        ax.yaxis.set_major_locator(plt.MaxNLocator(20))
        ax.yaxis.get_major_formatter().set_scientific(False)
    
    # Saving the chart
    plt.savefig("images/states/01_state_acc.png")
    
    return plt.close()

# State accumulated
def plot_state_acc_per_hundthousands(dataset, last_available_date):
    
    # Specifying the dataset for today
    dataset = dataset[dataset["date"] == last_available_date]
    
    # Generating an annotation
    not_updated = dataset[dataset["last_available_date"] != last_available_date].state.tolist()
    str_upd = ""
    
    for state in not_updated:
        str_upd += ("%s " % (state))
        
    # Creating the figure
    fig, axs = plt.subplots(2, 1, figsize=(12, 14), dpi=100)

    # Customizing the figure
    fig.subplots_adjust(top=0.92)
    fig.suptitle("Número de Casos e Óbitos acumulados de COVID-19 nos Estados do Brasil até %s/%s/%s" % (last_available_date[-2:], last_available_date[5:7], last_available_date[0:4]))
    fig.text(0.40, 0.063, ("Estados ainda não atualizados: " + str_upd), fontsize=12)
    fig.text(0.5, 0.038, "Autor: Evandro Rodrigues | Fonte: Brasil.IO em: %s/%s/%s" % (last_available_date[-2:], last_available_date[5:7], last_available_date[0:4]), ha='center', fontsize="14", fontweight=600)
    
    # Adding data to the axis (accumulated cases/deaths)
    axs[0].bar(dataset["state"], dataset["accumulated_cases"], color="#1F77B4", align='center')
    axs[1].bar(dataset["state"], dataset["accumulated_deaths"], color="red", align='center')
    
    # Customizing axis
    axs[0].set_title("Número de casos confirmados (acumulados)")
    axs[0].set_xlabel("Data")
    axs[0].set_ylabel("Nº de Casos")
    axs[1].set_title("Número de óbitos confirmados (acumulados)")
    axs[1].set_xlabel("Data")
    axs[1].set_ylabel("Nº de Óbitos")
    
    # For each axis apply ->
    for ax in axs:
        ax.yaxis.set_major_locator(plt.MaxNLocator(20))
        ax.yaxis.get_major_formatter().set_scientific(False)
    
    # Saving the chart
    plt.savefig("images/states/01_state_acc.png")
    
    return plt.close()

# State daily
def plot_state_daily(dataset, last_available_date):
    
    # Specifying the dataset for today
    dataset = dataset[dataset["date"] == last_available_date]
    
    # Generating an annotation
    not_updated = dataset[dataset["last_available_date"] != last_available_date].state.tolist()
    str_upd = ""
    for state in not_updated:
        str_upd += ("%s " % (state))
        
    # Creating the figure
    fig, axs = plt.subplots(2, 1, figsize=(12, 14), dpi=100)

    # Customizing the figure
    fig.subplots_adjust(top=0.92)
    fig.suptitle("Número de Casos e Óbitos de HOJE de COVID-19 nos Estados do Brasil até %s/%s/%s" % (last_available_date[-2:], last_available_date[5:7], last_available_date[0:4]))
    fig.text(0.40, .063, ("Estados ainda não atualizados: " + str_upd), fontsize=12)
    fig.text(0.5, 0.038, "Autor: Evandro Rodrigues | Fonte: Brasil.IO em: %s/%s/%s" % (last_available_date[-2:], last_available_date[5:7], last_available_date[0:4]), ha='center', fontsize="14", fontweight=600)
    
    # Adding data to the axis (accumulated cases/deaths)
    axs[0].bar(dataset["state"], dataset["new_cases"], color="#1F77B4", align='center')
    axs[1].bar(dataset["state"], dataset["new_deaths"], color="red", align='center')
    
    # Customizing axis
    axs[0].set_title("Número de casos confirmados (diário)")
    axs[0].set_xlabel("Data")
    axs[0].set_ylabel("Nº de Casos")
    axs[1].set_title("Número de óbitos confirmados (diário)")
    axs[1].set_xlabel("Data")
    axs[1].set_ylabel("Nº de Óbitos")
    
    # For each axis apply ->
    for ax in axs:
        ax.yaxis.set_major_locator(plt.MaxNLocator(20))
        ax.yaxis.get_major_formatter().set_scientific(False)
    
    # Saving the chart
    plt.savefig("images/states/02_state_new.png")
    
    return plt.close()