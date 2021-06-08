
# Project Title

Here I want to create a Streamlit App where I'll be able to generate a Wordcloud with most common words used in every musical genre.

The main reason I want to do this is **nerd enthusiasm**, but, beyond that, I think that it's interesting to know which are the main themes every genre has. I'd like to answer questions like:

* Could be that death metal talks more about love than death? (I really, REALLY doubt this)
* Is jazz more brainy than blues in the use of words?
* What will be the most used word in reggaeton?

To cover all of this (and many others) questions, this project came to my mind.

## Installation

    1. install virtualenv:
         `python -m venv env`

    2. install requirements in virtual env:
        `env/bin/pip install -r requirements.txt`

    3. you can launch an interpreter in the env context like this:
        `env/bin/python`

## Usage/Examples

In order to get the lyrics that we will need to create wordclouds, I use the Genius API with a database of artists that I'd collect for [another project](https://github.com/74minutos/music_clustering)

Be careful with this call to the API because it can be a long one if you use the same database. You can launch it like this:
```
env/bin/python -m get_data_build_streamlit.get_lyrics_from_genius
```

The script **will emit a csv file** in our directory and we will use that data for our App.

You can check if your data is correct to the App **running the dashboard on a local server**:
```
env/bin/streamlit run get_data_build_streamlit/lyrics_genre_to_streamlit.py
```
To share publicly this dashboard, you have to [ask for a invitation](https://streamlit.io/sharing)

## Running Tests

#### flake8 linting

Run flake8 on the packages:
```
env/bin/python -m flake8 --select F get_data_build_streamlit
```
#### mypy type checks

This runs [mypy](http://mypy-lang.org/) static typechecks on the code:
```
env/bin/python -m mypy --check-untyped-defs --ignore-missing-imports get_data_build_streamlit
```
## Authors

- [@74minutos](https://www.github.com/74minutos)
