## Function used to save DataFrames into CSV datasets
def save_dataset(dataset, path):
    return dataset.to_csv(path, index=False)

## Function to create a report of the daily updated data
def generate_report(dataset, last_available_date):
    file = open(f"reports/{last_available_date[5:7]}-{last_available_date[0:4]}/report_{last_available_date[-2:]}{last_available_date[5:7]}{last_available_date[0:4]}.txt", "w", encoding='utf8')
    
    file.write(f"Atualização COVID-19 no Brasil [{last_available_date[-2:]}/{last_available_date[5:7]}/{last_available_date[0:4]}]\n\n")
    
    file.write(("| Casos Acumulados: {0:,}\n").format(dataset["accumulated_num_cases"].iat[-1]).replace(',','.'))
    file.write(("| Óbitos Acumulados: {0:,}\n\n").format(dataset["accumulated_num_deaths"].iat[-1]).replace(',','.'))
   
    file.write(("| Qntd. de NOVOS Casos: {0:,}\n").format(dataset["new_num_cases"].iat[-1]).replace(',','.'))
    file.write(("| Qntd. de NOVOS Óbitos: {0:,}\n\n").format(dataset["new_num_deaths"].iat[-1]).replace(',','.'))
    
    file.write("Fonte dos dados: http://brasil.io / Secretarias de Saúde\n")
    file.write("#ficaemcasa #DataScience #COVID19")
    
    file.write("\n\n=================================\n\n")
    
    file.write("Visualização por Semanas Epidemiológicas e visualizações Regionais:")
    
    file.write("\n\n=================================\n\n")
    
    file.write("Repositório do GitHub:\n")
    file.write("https://github.com/evnrodr/covid19-brazil")
    
    file.close()
    
## Function to get a region name based on input (state)
def get_region(state, regions):
    for region, states in regions.items():  
        if state in states:
            return region