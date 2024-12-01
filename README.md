# Movie Genre Search

Este projeto permite pesquisar por filmes de um determinado gênero e obter uma lista dos filmes mais bem avaliados nesse gênero. Ele utiliza **Streamlit** para a interface de usuário e **Pandas** para manipulação de dados. O conjunto de dados de filmes e avaliações foi extraído de arquivos CSV.

## Funcionalidades

- Pesquisa de filmes por gênero.
- Exibição dos 10 filmes mais bem avaliados dentro do gênero selecionado.
- Interface interativa e fácil de usar criada com Streamlit.

## Pré-requisitos

Certifique-se de ter o Python instalado na versão 3.7 ou superior.

### Bibliotecas necessárias

- **Streamlit**: Para criar a interface interativa.
- **Pandas**: Para manipulação e análise de dados.
- **Matplotlib/Seaborn**: Para visualizações (se necessário).

## Instalação

1. Clone este repositório para sua máquina local:

   ```bash
   git clone https://github.com/seu-usuario/movie-genre-search.git

2. Navegue até o diretório do projeto:

    ```bash
    cd movie-genre-search
3. Instale as dependências:

   Usando o pip:

   ```bash
   pip install -r requirements.txt
    Ou, se preferir, crie um ambiente virtual:
   ```bash
     python -m venv venv
     source venv/bin/activate  # No Linux/Mac
     venv\Scripts\activate     # No Windows
     pip install -r requirements.txt

4. Execute o aplicativo Streamlit:
     ```bash
       streamlit run app.py

5. Abra o navegador e acesse http://localhost:8501 para interagir com a aplicação.

### Como Usar
   .Na interface do Streamlit, insira o gênero de filme desejado (por exemplo, "Comedy", "Action", etc.).
   .A aplicação exibirá os 10 filmes mais bem avaliados para o gênero selecionado.



