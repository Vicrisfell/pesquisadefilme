import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Caminhos para os arquivos CSV
caminho_movies = "movies.csv"  # Substitua pelo caminho correto
caminho_ratings = "ratings.csv"  # Substitua pelo caminho correto

# Carregar dados dos arquivos CSV
try:
    movies = pd.read_csv(caminho_movies)
    ratings = pd.read_csv(caminho_ratings)
    print("Arquivos CSV carregados com sucesso!")
except FileNotFoundError as e:
    print(f"Erro ao carregar os arquivos CSV: {e}")
    exit()

# Análise básica
print("Resumo dos Ratings:")
print(ratings.describe())

# Distribuição dos ratings
sns.histplot(ratings["rating"], bins=10, kde=True)
plt.title("Distribuição de Ratings")
plt.xlabel("Rating")
plt.ylabel("Frequência")
plt.show()

# Popularidade de gêneros
movies["genres"] = movies["genres"].str.split("|")
genres_exploded = movies.explode("genres")
top_genres = genres_exploded["genres"].value_counts()

plt.figure(figsize=(10, 5))
sns.barplot(x=top_genres.index, y=top_genres.values)
plt.title("Gêneros mais Populares")
plt.xlabel("Gêneros")
plt.ylabel("Número de Filmes")
plt.xticks(rotation=45)
plt.show()
