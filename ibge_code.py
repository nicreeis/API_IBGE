import requests
import pandas as pd
import numpy as np

def obter_quantidade_sexo(nome, sexo):
    url = f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}?sexo={sexo}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        df = pd.json_normalize(data[0]["res"])
        total = df["frequencia"].sum()
        return total
    return None

def obter_sexo_correto(nome):
    sexo_M = obter_quantidade_sexo(nome,"M")
    sexo_F = obter_quantidade_sexo(nome,"F")
    if sexo_M > sexo_F:
        return "Masculino"
    else:
        return "Feminino"

df_dados_clientes = pd.read_csv(r'\dataset_clientes.csv')

df_dados_clientes['Sexo Corrigido'] = df_dados_clientes['Nome'].apply(obter_sexo_correto)

df_dados_clientes['Sexo está correto?'] = np.where(df_dados_clientes['Sexo'] == df_dados_clientes['Sexo Corrigido'] , 'True','False')

df_dados_clientes.to_csv(r'\dados_clientes_corrigido.csv', index=False)
