import streamlit as st
import pickle
import pandas as pd

def recommendations(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(similarity[movie_index])),reverse=True,key = lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]][0])
    return recommended_movies

movies_list = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movies_list)
similarity = pickle.load(open('similarity.pkl','rb'))
st.title('Movies Recommendations')
selected_movie_name = st.selectbox(
'How would you like to be contacted?',
movies['title'].values
)
if st.button('Recommend'):
    recommendations = recommendations(selected_movie_name)
    for i in recommendations:
        st.write(i)
