import pickle
import streamlit as st
import pandas as pd
import numpy as np
#import requests

def fetch_poster(isbn):
    url = "http://covers.openlibrary.org/b/isbn/{}-M.jpg".format(isbn)
    return url

def recommend(book):
    index = new_book[new_book['title'] == book].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_book_names = []
    recommended_book_posters = []
    for i in distances[1:6]:
        isbn = new_book.iloc[i[0]].isbn13
        recommended_book_posters.append(fetch_poster(isbn))
        recommended_book_names.append(new_book.iloc[i[0]].title)
    return recommended_book_names,recommended_book_posters


st.header('Book Recommender system')
new_book = pd.read_pickle(open('model/updatedbook_list.pkl','rb'))
similarity = pickle.load(open('model/similaritybook.pkl','rb'))

book_list = np.sort(new_book['title'].values)
selected_book = st.selectbox("Enter the name of the book: ",book_list)

if st.button('Recommend'):
    recommended_book_names,recommended_book_posters = recommend(selected_book)
    col1, col2, col3, col4, col5 = st.beta_columns(5)
    with col1:
        st.text(recommended_book_names[0])
        st.image(recommended_book_posters[0])
    with col2:
        st.text(recommended_book_names[1])
        st.image(recommended_book_posters[1])
    with col3:
        st.text(recommended_book_names[2])
        st.image(recommended_book_posters[2])
    with col4:
        st.text(recommended_book_names[3])
        st.image(recommended_book_posters[3])
    with col5:
        st.text(recommended_book_names[4])
        st.image(recommended_book_posters[4])