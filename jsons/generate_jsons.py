import pandas as pd

state_list = ['AC', 'AP', 'AM', 'TO', 'PA', 'RR', 'RO', 'AL', 'BA', 'PB', 'PE', 'SE', 'PI', 'CE', 'MA', 'RN', 'MT', 'GO', 'MS', 'DF', 'SP', 'ES', 'RJ', 'MG',  'SC', 'RS', 'PR']

pd.read_csv("../data/national/covid19-dataset-brasil.csv").to_json("national_data.json")

pd.read_csv("../data/regions/covid19-Norte.csv").to_json("region_norte.json")
pd.read_csv("../data/regions/covid19-Nordeste.csv").to_json("region_nordeste.json")
pd.read_csv("../data/regions/covid19-Centro-Oeste.csv").to_json("region_centrooeste.json")
pd.read_csv("../data/regions/covid19-Sudeste.csv").to_json("region_sudeste.json")
pd.read_csv("../data/regions/covid19-Sul.csv").to_json("region_sul.json")

for state in state_list:
    pd.read_csv(f"../data/states/{state}/covid19-dataset-{state}.csv").to_json(f"state_{state.lower()}_data.json")