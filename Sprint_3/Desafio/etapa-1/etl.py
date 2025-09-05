import pandas as pd
import re

# Lendo o arquivo csv
df = pd.read_csv("concert_tours_by_women.csv")

# Selecionando só as colunas que quero manter, seguindo o modelo fornecido no desafio
df = df[[
    "Rank",
    "Actual gross",
    "Adjustedgross (in 2022 dollars)",
    "Artist",
    "Tour title",
    "Year(s)",
    "Shows",
    "Average gross"
]]

# Padronizando os traços da coluna "Year(s)"
df["Year(s)"] = df["Year(s)"].astype(str).str.replace("–", "-", regex=False)

# Separando a coluna "Year(s)" em Start year e End year
years = df["Year(s)"].str.split("-", expand=True)

df["Start year"] = years[0]
df["End year"] = years[1]    

# Se não tiver End year, usa o Star year mesmo
df["End year"] = df["End year"].fillna(df["Start year"])

# Removendo a coluna original
df = df.drop(columns=["Year(s)"])  

# Limpando tudo que não seja número ou ponto nas colunas de dinheiro
def limpa_dinheiro(valor):
    if isinstance(valor, str):
        valor = re.sub(r"[^0-9.]", "", valor)
        if valor == "":
            return 0.0
        return float(valor)
    return float(valor)

# Aplicando nas colunas de dinheiro
df["Actual gross"] = df["Actual gross"].apply(limpa_dinheiro)
df["Adjustedgross (in 2022 dollars)"] = df["Adjustedgross (in 2022 dollars)"].apply(limpa_dinheiro)
df["Average gross"] = df["Average gross"].apply(limpa_dinheiro)

# Alterando o tipo das colunas
df["Rank"] = df["Rank"].astype(int)
df["Actual gross"] = df["Actual gross"].astype(float)
df["Adjustedgross (in 2022 dollars)"] = df["Adjustedgross (in 2022 dollars)"].astype(float)
df["Shows"] = df["Shows"].astype(int)
df["Average gross"] = df["Average gross"].astype(float)
df["Start year"] = df["Start year"].astype(int)
df["End year"] = df["End year"].astype(int)

# Limpando as colunas de texto, transformando tudo em string e retirando possíveis espaços extras
df["Artist"] = df["Artist"].astype(str).str.strip()
df["Tour title"] = df["Tour title"].astype(str).str.strip()

# Renomeando a coluna "Adjustedgross (in 2022 dollars)" para seguir o modelo fornecido
df = df.rename(columns={
    "Adjustedgross (in 2022 dollars)": "Adjusted gross (in 2022 dollars)"
})

# Removendo símbolos da coluna "Tour Title"
def limpa_texto(txt):
    if pd.isna(txt):
        return txt
    txt = str(txt)
    txt = re.sub(r"\[.*?\]", "", txt)
    txt = re.sub(r"[†‡]", "", txt)
    txt = re.sub(r"\s*\d+[a-zA-Z]$", "", txt)
    return txt.strip()

df["Tour title"] = df["Tour title"].apply(limpa_texto)

df.to_csv("csv_limpo.csv", index=False)