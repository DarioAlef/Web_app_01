import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit import metric



#metodo da streamlit que configura formatação da página
st.set_page_config(layout='wide')

#'.read_' metodo da biblioteca pandas para "ler" arquivos
reviews = pd.read_csv('customer reviews.csv')
top100_books = pd.read_csv('Top-100 Trending Books.csv')

#metodo 'unique' da pd, retorna um string excluindo os nomes repetidos
#metodo entre chaves sempre irá se referir a uma coluna do arquivo .cvs
nomes_livros = top100_books['book title'].unique()

#mover 'nomes_livros' pra side bar
sidebar_nomes = st.sidebar.selectbox('Books', nomes_livros)

#agora 'top100_books' fica atrelado ao operador de comparação, FILTRADO
#'==' está perguntando se é igual a book
livro_escolhido = top100_books[top100_books['book title'] == sidebar_nomes]
livro_review = reviews[reviews['book name'] == sidebar_nomes]

#metodo .iloc da pd transforma um item da coluna em array, podendo partí-lo por índice, igual o metodo .len(), assim as informações adicionais não vem junto
titulo_livro = livro_escolhido['book title'].iloc[0]
genero_livro = livro_escolhido['genre'].iloc[0]
#fomat string para adicionar o '$'
preco_livro = f'${livro_escolhido["book price"].iloc[0]}'
rating_livro = livro_escolhido['rating'].iloc[0]
ano_livro = livro_escolhido['year of publication'].iloc[0]

#metodo da st que coloca um texto grande (título)
st.title(titulo_livro)
#subtitulo
st.subheader(genero_livro)

col1,col2,col3 = st.columns(3)
#metodo '.metric' da st que cria paineis de dados metricos
col1.metric('Price', preco_livro)
col2.metric('Rating', rating_livro)
col3.metric('Year of Publication', ano_livro)

#metodo para adicionar uma linha divisória
st.divider()

#o for irá percorrer a lista de reviewa
livro_review
for row in livro_review.values:
    st.write(row[2])
    st.write(row[5])

