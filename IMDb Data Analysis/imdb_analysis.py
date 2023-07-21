import pandas as pd
import matplotlib.pyplot as plt
import gzip

# Função para ler o arquivo gzip e carregar dados em um DataFrame
def read_imdb_data(file_path):
    with gzip.open(file_path, 'rt', encoding='utf-8') as file:
        df = pd.read_csv(file, sep='\t')
    return df

# Função para realizar análise e visualização de dados
def analyze_imdb_data(df):
    # Limpeza e pré-processamento de dados
    # Retirando as linhas com informações de região ou idioma ausentes
    df = df.dropna(subset=['region', 'language'])

    # Agrupando dados por região e calculando a contagem de títulos em cada região
    region_counts = df['region'].value_counts()

    # Agrupando dados por idioma e calculando a contagem de títulos em cada idioma
    language_counts = df['language'].value_counts()

    # Agrupando dados por tipos de títulos e calculando a contagem de títulos para cada tipo
    types_counts = df['types'].explode().value_counts()

    # Plotando as 10 principais regiões com mais títulos
    plt.figure(figsize=(10, 6))
    plt.bar(region_counts[:10].index, region_counts[:10].values)
    plt.xlabel('Region')
    plt.ylabel('Number of Titles')
    plt.title('Top 10 Regions with Most Titles')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Plotando os 10 principais idiomas com mais títulos
    plt.figure(figsize=(10, 6))
    plt.bar(language_counts[:10].index, language_counts[:10].values)
    plt.xlabel('Language')
    plt.ylabel('Number of Titles')
    plt.title('Top 10 Languages with Most Titles')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Plotando as contagens de diferentes tipos de títulos
    plt.figure(figsize=(10, 6))
    plt.bar(types_counts.index, types_counts.values)
    plt.xlabel('Title Type')
    plt.ylabel('Number of Titles')
    plt.title('Distribution of Title Types')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Executando a análise
def main():
    file_path = 'title.akas.tsv.gz'
    df = read_imdb_data(file_path)
    analyze_imdb_data(df)

if __name__ == "__main__":
    main()