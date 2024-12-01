import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar dados CSV
movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")

# Configurações iniciais do app
st.title("Análise de Dados de Filmes")
st.sidebar.header("Escolha sua Pesquisa")

# Opções para o usuário
option = st.sidebar.selectbox(
    "O que você gostaria de visualizar?",
    ["Resumo dos Ratings", "Distribuição de Ratings", "Popularidade de Gêneros"]
)

if option == "Resumo dos Ratings":
    st.subheader("Resumo dos Ratings")
    st.write(ratings.describe())

elif option == "Distribuição de Ratings":
    st.subheader("Distribuição de Ratings")
    plt.figure(figsize=(8, 6))
    sns.histplot(ratings["rating"], bins=10, kde=True)
    plt.title("Distribuição de Ratings")
    plt.xlabel("Rating")
    plt.ylabel("Frequência")
    st.pyplot(plt)

elif option == "Popularidade de Gêneros":
    st.subheader("Popularidade de Gêneros")
    movies["genres"] = movies["genres"].str.split("|")
    genres_exploded = movies.explode("genres")
    top_genres = genres_exploded["genres"].value_counts()

    plt.figure(figsize=(10, 5))
    sns.barplot(x=top_genres.index, y=top_genres.values)
    plt.title("Gêneros mais Populares")
    plt.xlabel("Gêneros")
    plt.ylabel("Número de Filmes")
    plt.xticks(rotation=45)
    st.pyplot(plt)
