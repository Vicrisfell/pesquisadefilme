from flask import Flask, request, jsonify
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

# Criar a aplicação Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Bem-vindo à API de Pesquisa de Filmes! Use o endpoint /search para buscar por gênero."

@app.route('/search', methods=['GET'])
def search():
    # Pegar o parâmetro 'genre' da URL
    genre = request.args.get('genre')
    if not genre:
        return jsonify({"error": "Por favor, forneça um gênero no parâmetro 'genre'."}), 400

    # Filtrar os filmes pelo gênero fornecido
    filtered_data = data[data["genre"] == genre]

    if filtered_data.empty:
        return jsonify({"error": f"Nenhum filme encontrado para o gênero '{genre}'."}), 404

    # Calcular as médias das avaliações e ordenar os filmes
    top_movies = (
        filtered_data.groupby("title")["rating"]
        .mean()
        .sort_values(ascending=False)
        .head(10)  # Top 10 filmes mais bem avaliados
    )

    # Retornar o resultado como JSON
    result = top_movies.reset_index().to_dict(orient="records")
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
