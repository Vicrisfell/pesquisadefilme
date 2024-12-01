import streamlit as st
import pandas as pd

# Carregar os dados CSV
movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")

# Pré-processar os dados de forma eficiente
movies["genres"] = movies["genres"].fillna("")  # Garantir que não haja valores nulos
movies = movies[movies["genres"] != "(no genres listed)"]  # Remover filmes sem gênero

# Criar uma tabela expandida de filmes e gêneros
movie_genres = movies[["movieId", "title", "genres"]].copy()
movie_genres = movie_genres.assign(genres=movie_genres["genres"].str.split("|"))
expanded_movies = pd.concat(
    [movie_genres.drop(columns="genres"), movie_genres["genres"].apply(pd.Series).stack().reset_index(drop=True)], 
    axis=1
)
expanded_movies.columns = ["movieId", "title", "genre"]

# Combinar filmes e avaliações
data = ratings.merge(expanded_movies, on="movieId", how="inner")

# Streamlit interface
st.title("API de Pesquisa de Filmes")

# Gêneros disponíveis para seleção
genres = data["genre"].unique()
selected_genre = st.selectbox("Escolha o gênero do filme", genres)

# Exibir os filmes mais bem avaliados para o gênero selecionado
if selected_genre:
    filtered_data = data[data["genre"] == selected_genre]

    if filtered_data.empty:
        st.error(f"Nenhum filme encontrado para o gênero '{selected_genre}'.")
    else:
        top_movies = (
            filtered_data.groupby("title")["rating"]
            .mean()
            .sort_values(ascending=False)
            .head(10)  # Top 10 filmes mais bem avaliados
        )

        st.subheader(f"Top 10 Filmes no Gênero '{selected_genre}'")
        st.write(top_movies.reset_index())
