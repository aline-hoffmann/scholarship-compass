# Importando as bibliotecas pandas e matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Lendo o arquivo csv já limpo
csv_file = r"C:\Users\josim\OneDrive\Área de Trabalho\ALINE\CC\COMPASS\scholarship-compass\Sprint_3\Desafio\etapa-1\csv_limpo.csv"

df = pd.read_csv(csv_file)

# QUESTÃO 1
# Contando quantas vezes cada artista aparece na lista
artistas_contagem = df['Artist'].value_counts()

# Verificando qual o número máximo de aparições
max_aparicoes = artistas_contagem.max()

# Verificando quais artistas aparecem 4 vezes
artistas_mais_frequentes = artistas_contagem[artistas_contagem == max_aparicoes]

# Filtrando apenas as artistas empatadas
artistas_empate = artistas_mais_frequentes.index.tolist()

# Calculando a média do faturamento bruto (Actual gross) dessas duas artistas
medias_empate = df.groupby("Artist")["Actual gross"].mean().loc[artistas_empate]

# Verificando qual a artista que mais aparece e tem maior média de faturamento bruto
artista_mais_frequente = medias_empate.idxmax()
media_faturamento_artista = medias_empate.max()

# Imprimindo a resposta da Questão 1
resposta_q1 = (
    f"Q1:\nA artista que mais aparece na lista e possui maior média de seu faturamento bruto é {artista_mais_frequente}, com média de ${media_faturamento_artista:,.2f} USD."
)

# QUESTÃO 2
# Verificando se existe pelo menos uma turnê que começou e terminou no mesmo ano
turnes_mesmo_ano = df[df["Start year"] == df["End year"]]

# Selecionando qual dessas turnês que começaram e terminaram no mesmo ano teve a maior média de faturmento bruto ("Actual gross")
maior_gross = turnes_mesmo_ano.loc[turnes_mesmo_ano["Average gross"].idxmax()]

resposta_q2 = f"Q2:\nA turnê que aconteceu dentro de um único ano e teve a maior média de faturamento bruto (Average gross) foi '{maior_gross['Tour title']}' da artista {maior_gross['Artist']}, com média de faturamento de ${maior_gross['Average gross']:,.2f} USD."

# QUESTÃO 3
# Criando uma coluna para o faturamento bruto por show
df["Bruto por show"] = df["Adjusted gross (in 2022 dollars)"] / df["Shows"]

# Selecionando as 3 turnês que possuem o show (unitário) mais lucrativo
top3 = df.sort_values("Bruto por show", ascending=False).head(3)

resposta_q3 = (
    "Q3:\nAs 3 turnês mais lucrativas por show (em dólares ajustados de 2022):\n"
    f"1. {top3.iloc[0]['Tour title']} — {top3.iloc[0]['Artist']} — "
    f"Bruto por show: ${top3.iloc[0]['Bruto por show']:,.2f}\n"
    f"2. {top3.iloc[1]['Tour title']} — {top3.iloc[1]['Artist']} — "
    f"Bruto por show: ${top3.iloc[1]['Bruto por show']:,.2f}\n"
    f"3. {top3.iloc[2]['Tour title']} — {top3.iloc[2]['Artist']} — "
    f"Bruto por show: ${top3.iloc[2]['Bruto por show']:,.2f}"
)

# JUNTANDO A RESPOTAS DAS TRÊS PRIMEIRAS QUESTÕES E CRIANDO UM ARQUIVO TXT
respostas = (
    f"{resposta_q1} \n\n"
    f"{resposta_q2} \n\n"
    f"{resposta_q3}"
)

with open("respostas.txt", "w", encoding="utf-8") as f:
    f.write(respostas)

# QUESTÃO 4
# Aproveitando a resposta da Questão 1, que me informava as duas artistas que mais apareciam na lista, porém, dessa vez desempatando pelo somatório do faturamento bruto

somatorio_empate = df.groupby("Artist")["Actual gross"].sum().loc[artistas_empate]

# Verificando qual artista tem o maior somatório do faturamento bruto
artista_q4 = somatorio_empate.idxmax()
soma_faturamento_artista = somatorio_empate.max()

# Filtrando só os dados da Taylor Swift
df_artista = df[df["Artist"] == artista_q4]

# Agrupando por ano de início e somando o faturamento bruto
faturamento_por_ano = df_artista.groupby("Start year")["Actual gross"].sum()

# Criando o gráfico de linhas para visualizar o resultado
with plt.style.context('dark_background'):
    plt.figure(figsize=(9,5))
    plt.plot(faturamento_por_ano.index, faturamento_por_ano.values, marker="o", linestyle="-", color="deeppink")

    plt.title(f"FATURAMENTO POR ANO DA TURNÊ - {artista_mais_frequente}", fontweight="bold")
    plt.xlabel("ANO DE INÍCIO DA TURNÊ", labelpad=20, fontweight="bold")
    plt.ylabel("FATURAMENTO BRUTO (US$)", labelpad=20, fontweight="bold")
    plt.xticks(faturamento_por_ano.index)

    # Organizando o eixo y de 100 em 100 milhões
    max_val = faturamento_por_ano.max()
    yticks = range(0, int(max_val) + 100_000_000, 100_000_000)
    plt.yticks(yticks, [f"{y//1_000_000}M" for y in yticks])

    # Grid
    plt.grid(True, linestyle="--", alpha=0.8)
    plt.tight_layout()
    plt.savefig("questao-4.png", dpi=300)
    plt.close()

# QUESTÃO 5
# Descobrindo a quantidade de shows por artista
shows_por_artista = df.groupby("Artist")["Shows"].sum()

# Selecionando apenas as cinco artistas com mais shows
top5_artistas_shows = shows_por_artista.sort_values(ascending=False).head(5)

# Criando o gráfico de barras para visualizar o resultado
plt.figure(figsize=(9,6))
bars=plt.bar(top5_artistas_shows.index, top5_artistas_shows.values, color="deeppink", zorder=3)

plt.title("TOP CINCO ARTISTAS POR NÚMERO DE SHOWS",fontweight="bold")
plt.xlabel("ARTISTAS", labelpad=20, fontweight="bold")
plt.ylabel("NÚMERO DE SHOWS", labelpad=20, fontweight="bold")
plt.bar_label(bars, labels=[f"{int(v)}" for v in top5_artistas_shows.values], fontsize=10, fontweight="bold")

plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("questao-5.png", dpi=300, bbox_inches="tight")
plt.close()