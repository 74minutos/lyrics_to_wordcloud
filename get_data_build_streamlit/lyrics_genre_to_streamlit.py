import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from stop_words import get_stop_words

STOP_WORDS = set(get_stop_words("en")).union(set(get_stop_words("es")))
STOP_WORDS = STOP_WORDS.union(["don", "pa", "Rose", "S", "m", "si", "D", "re", "oh", "ooh", "get", "know", "na", "t", "like"])

st.cache(suppress_st_warning=True)
data = pd.read_csv("lyrics_dataset.csv", delimiter=";")
data['lyrics_data'] = data['lyrics_data'].str.replace("[", "").str.replace("]", "")
data['genre'] = data['genre'].str.replace("[", "").str.replace("]", "").str.replace("'", "")
data['genre'] = data['genre'].str.strip(' ').str.split(',')

data = data.explode('genre', ignore_index=True)
st.set_page_config(page_icon="assets/favicon.ico",
                   layout='wide')
st.title('Lyrics Analysis')

st.markdown("A study about lyrics in different music genres")

genre = st.sidebar.multiselect(
    'Which genre do you want to track?',
     (data.genre).unique())

for i in genre:
    'You selected: ', i
    mask = data.genre == i
    filtered_data = data.loc[mask, :]
    fig, ax = plt.subplots()
    wc = WordCloud(stopwords=STOP_WORDS)
    wc.generate(str(filtered_data['lyrics_data'].values).replace("'", ""))

    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    st.pyplot(fig)
