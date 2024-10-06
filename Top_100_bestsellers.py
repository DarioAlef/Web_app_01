import streamlit as st   #faz a fortação HTML da página
import pandas as pd    #faz a formatação de tabelas e banco de dados
import plotly_express as px   #faz a formatação de gráficos

#metodo da streamlit que configura formatação da página
st.set_page_config(layout='wide')

#'.read_' metodo da biblioteca pandas para "ler" arquivos
reviews = pd.read_csv('customer reviews.csv')
top100_books = pd.read_csv('Top-100 Trending Books.csv')

#metodos da st para recortar o máximo e mínimo de uma coluna
preco_max = top100_books['book price'].max()
preco_min = top100_books['book price'].min()

#cria um widget de controle deslizante: barra móvel para manipulação de valores
#em: mínimo, máximo e onde começará
#metodo 'sidebar' indica que aquela função ficará na side bar
slider_preco = st.sidebar.slider('Faixa de preço', preco_min, preco_max, preco_max)

#colchete [] , se assemelha a dizer 'quando'

#indica: top_100 apenas ocorrerá conforme a preco_max. Associando as variáveis
#sintaxe: lista_de_precos será a coluna book price, que pertence a top100, quando for menor ou igual a preco_max e preco_max está atrela ao slider
lista_de_precos = top100_books[top100_books['book price'] <= slider_preco]

lista_de_precos

#metodo value_counts da pandas conta a freqência de um item
#medoto da px '.bar' exibirá o gráfica em barra
grafico_ano = px.bar(lista_de_precos['year of publication'].value_counts())

#metodo da px '.histogram' faz o value_counts, mas com cálculos
grafico_preco = px.histogram(lista_de_precos['book price'])

#forma de escrita que atribui o mesmo valor gerando duas variáveis, com parâmetro '(2)' para dividir a tela em duas
col1, col2 = st.columns(2)
col1.plotly_chart(grafico_ano)
col2.plotly_chart(grafico_preco)
