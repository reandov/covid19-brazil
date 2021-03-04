import matplotlib.pyplot as plt

# National accumulated
def plot_national_acc(dataset, last_available_date):
    
    # Creating the figure
    fig, axs = plt.subplots(2, 1, figsize=(12, 14), dpi=100)
    
    # Customizing the figure
    fig.autofmt_xdate(rotation=0, ha='center')
    fig.subplots_adjust(top=0.92)
    fig.suptitle("Números de casos e óbitos acumulados de COVID-19 no Brasil até %s/%s/%s" % (last_available_date[-2:], last_available_date[5:7], last_available_date[0:4]))
    fig.text(.5, .12, "Autor: Evandro Rodrigues | Fonte: Brasil.IO em: %s/%s/%s" % (last_available_date[-2:], last_available_date[5:7], last_available_date[0:4]), ha='center', fontsize="14", fontweight=600)
    
    # Adding data to the axis
    axs[0].plot(dataset["date"], dataset["accumulated_num_cases"], label = "Casos Acumulados")
    axs[1].plot(dataset["date"], dataset["accumulated_num_deaths"], label = "Óbitos Acumulados", color='red')
    
    # Customizing the axis
    axs[0].set_title("Número de casos confirmados (acumulados)", fontsize=14)
    axs[1].set_title("Número de óbitos confirmados (acumulados)", fontsize=14)
    axs[0].set_xlabel("Data")
    axs[1].set_xlabel("Data")
    axs[0].set_ylabel("Nº de Casos")
    axs[1].set_ylabel("Nº de Óbitos")
    axs[1].tick_params(axis='x', which='both', length=5, width=1.5, color='lightgray')
    
    # For each axis apply ->
    for ax in axs:
        ax.xaxis.set_major_locator(plt.MaxNLocator(10))
        ax.yaxis.set_major_locator(plt.MaxNLocator(10))
        ax.legend(prop=dict(weight='bold'))
        ax.yaxis.get_major_formatter().set_scientific(False)
        
    # Annotations
    axs[0].annotate('{0:,}'.format(dataset["accumulated_num_cases"].iat[-1]).replace(',','.'), 
                    (dataset["date"].iat[-1], dataset["accumulated_num_cases"].iat[-1]), 
                    textcoords = "offset points", xytext=(20, -3), 
                    fontweight = 600, color='black', 
                    arrowprops=dict(color='black', arrowstyle='wedge'), fontsize=12)
    
    axs[1].annotate('{0:,}'.format(dataset["accumulated_num_deaths"].iat[-1]).replace(',','.'), 
                    (dataset["date"].iat[-1], dataset["accumulated_num_deaths"].iat[-1]), 
                    textcoords = "offset points", xytext=(20, -3), 
                    fontweight = 600, color='black', 
                    arrowprops=dict(color='black', arrowstyle='wedge'), fontsize=12)
        
    # Saving the chart
    plt.savefig("images/01_national_acc.png")
    
    return plt.close()

# National daily
def plot_national_daily(dataset, last_available_date):
    
    # Creating the figure
    fig, axs = plt.subplots(2, 1, figsize=(12, 14), dpi=100)
    
    # Customizing the figure
    fig.autofmt_xdate(rotation=0, ha='center')
    fig.subplots_adjust(top=0.92)
    fig.suptitle("Números de casos e óbitos diários de COVID-19 no Brasil até %s/%s/%s" % (last_available_date[-2:], last_available_date[5:7], last_available_date[0:4]))
    fig.text(.5, .12, "Autor: Evandro Rodrigues | Fonte: Brasil.IO em: %s/%s/%s" % (last_available_date[-2:], last_available_date[5:7], last_available_date[0:4]), ha='center', fontsize="14", fontweight=600)
    
    # Adding data to the axis
    axs[0].plot(dataset["date"], dataset["new_num_cases"], label = "Casos Diários")
    axs[1].plot(dataset["date"], dataset["new_num_deaths"], label = "Óbitos Diários", color='red')
    
    # Customizing the axis
    axs[0].set_title("Número de casos confirmados (diários)", fontsize=14)
    axs[1].set_title("Número de óbitos confirmados (diários)", fontsize=14)
    axs[0].set_xlabel("Data")
    axs[1].set_xlabel("Data")
    axs[0].set_ylabel("Nº de Casos")
    axs[1].set_ylabel("Nº de Óbitos")
    axs[1].tick_params(axis='x', which='both', length=5, width=1.5, color='lightgray')
    
    # For each axis apply ->
    for ax in axs:
        ax.xaxis.set_major_locator(plt.MaxNLocator(10))
        ax.yaxis.set_major_locator(plt.MaxNLocator(10))
        ax.legend(prop=dict(weight='bold'))
        ax.yaxis.get_major_formatter().set_scientific(False)
        
    # Annotations
    axs[0].annotate('{0:,}'.format(dataset["new_num_cases"].iat[-1]).replace(',','.'), 
                    (dataset["date"].iat[-1], dataset["new_num_cases"].iat[-1]), 
                    textcoords = "offset points", xytext=(20, -3), 
                    fontweight = 600, color='black', 
                    arrowprops=dict(color='black', arrowstyle='wedge'), fontsize=12)
    
    axs[1].annotate('{0:,}'.format(dataset["new_num_deaths"].iat[-1]).replace(',','.'), 
                    (dataset["date"].iat[-1], dataset["new_num_deaths"].iat[-1]), 
                    textcoords = "offset points", xytext=(20, -3), 
                    fontweight = 600, color='black', 
                    arrowprops=dict(color='black', arrowstyle='wedge'), fontsize=12)
    
    # Saving the chart
    plt.savefig("images/02_national_new.png")
    
    return plt.close()