import streamlit as st
import pandas as pd
import pickle
import requests


def get_poster(mov_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=de8b4945f7d701714e15884d50035c0d&language=en-US".format(mov_id)
    response = requests.get(url)
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity_score[movie_index])), reverse=True, key=lambda x: x[1])

    recommended_movie_names = []
    recommended_movie_posters = []
    recommended_movie_overviews = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(get_poster(movie_id))
        recommended_movie_overviews.append(movies.iloc[i[0]].overview)

    return recommended_movie_names, recommended_movie_posters, recommended_movie_overviews


movies = pd.DataFrame(pickle.load(open('movies_dict.pkl', 'rb')))
similarity_score = pickle.load(open('similarity.pkl', 'rb'))
movie_list = movies['title'].values

st.title('Movie Recommendation System')

selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    st.markdown('**_BINGE WATCH!_**')
    rec_mov_names, rec_mov_posters, rec_mov_overviews = recommend(selected_movie)
    col1, col2, col3, col4, col5= st.columns(5)
    with col1:
        st.text(rec_mov_names[0])
        st.image(rec_mov_posters[0])
        with st.expander("See Storyline"):
            st.write(rec_mov_overviews[0])
    with col2:
        st.text(rec_mov_names[1])
        st.image(rec_mov_posters[1])
        with st.expander("See Storyline"):
            st.write(rec_mov_overviews[1])
    with col3:
        st.text(rec_mov_names[2])
        st.image(rec_mov_posters[2])
        with st.expander("See Storyline"):
            st.write(rec_mov_overviews[2])
    with col4:
        st.text(rec_mov_names[3])
        st.image(rec_mov_posters[3])
        with st.expander("See Storyline"):
            st.write(rec_mov_overviews[3])
    with col5:
        st.text(rec_mov_names[4])
        st.image(rec_mov_posters[4])
        with st.expander("See Storyline"):
            st.write(rec_mov_overviews[4])
