# Recommendation-Engine-MsE2k22

This is my Microsoft Engage 2022 project on the problem statement of Algorithms for Recommendation Engine/system.

![Python](https://img.shields.io/badge/Python-3.9-blueviolet)
![Framework](https://img.shields.io/badge/Framework-Streamlit-red)
![API](https://img.shields.io/badge/API-TMDB-fcba03)


## Overview

Content Based Recommender System recommends movies similar to the movie searched by the user by calculating similarity scores with different movies based on storyline, genres, top cast and director and recommends top five choices for you. 
      For calculating the similarity scores I'm using `cosine similarity`, to learn more about it follow the Reference section.
      The details of the movies(title, genre, storyline, rating, poster, etc) are fetched using an API by TMDB, https://www.themoviedb.org/documentation/api, learn how to get your own API key on How to get the API key section.
      
Check out the live demo: http://192.168.43.213:8501/
#### Heroku URL:


## How to get the API key?

Create an account in https://www.themoviedb.org/, click on the `API` link from the left hand sidebar in your account settings and fill all the details to apply for API key. If you are asked for the website URL, just give "NA" if you don't have one. You will see the API key in your `API` sidebar once your request is approved.


## How to run the project?

1. Clone or download this repository to your local machine.
2. Install all the libraries mentioned in the [requirements.txt] file with the command `pip install -r requirements.txt`
3. Get your API key from https://www.themoviedb.org/. (Refer the above section on how to get the API key)
3. Replace YOUR_API_KEY in **both** the places (line no. 8) of `main.py` file and hit save.
4. Open your terminal/command prompt from your project directory and run the file `main.py` by executing the command `streamlit run main.py`.
5. Go to your browser and type `http://localhost:8501` in the address bar.
6. Hurray! That's it.


## Functionality Used:

### Similarity Score : 

How does it decide which item is most similar to the item user searches? Here come the similarity scores.
   
It is a numerical value ranges between zero to one which helps to determine how much two items are similar to each other on a scale of zero to one. This similarity score is obtained measuring the similarity between the text details of both of the items. So, similarity score is the measure of similarity between given text details of two items. This can be done by cosine-similarity.
 
 
### How Cosine Similarity works?

Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.
  
![image](https://user-images.githubusercontent.com/36665975/70401457-a7530680-1a55-11ea-9158-97d4e8515ca4.png)

  
More about Cosine Similarity : [Understanding the Math behind Cosine Similarity](https://www.machinelearningplus.com/nlp/cosine-similarity/)

### Sources of the datasets
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_credits.csv
