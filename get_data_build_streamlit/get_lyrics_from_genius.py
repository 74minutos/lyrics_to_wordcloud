import pandas as pd
from typing import List, Dict, Any
from get_data_build_streamlit import utilities

def make_dict(artist: str, genre: str, lyrics_data: List[Any]) -> Dict:
    return {
    'artist': artist,
    'genre': genre,
    'lyrics_data': lyrics_data}

def get_lyrics(api_key_path: str, max_songs: int, seconds: int, retries: int) -> None:
    music_data_url = "https://raw.githubusercontent.com/74minutos/music_clustering/master/songs_with_audio_features.csv"
    music_data = pd.read_csv(music_data_url, delimiter=";")
    artist_genre = pd.concat([music_data['artist_name'], music_data['genre']], axis=1, keys=['artist_name', 'genre'])
    artist_genre = artist_genre.drop_duplicates().to_dict('records')
    lyrics_data = []

    for artist in artist_genre:
        songs = utilities.genius_api_calls(api_key_path, artist['artist_name'], max_songs, seconds, retries)
        music_dict = make_dict(artist = artist['artist_name'],
            genre = artist['genre'],
            lyrics_data  = [song.lyrics for song in songs])
        lyrics_data.append(music_dict)
    lyrics_dataset = pd.DataFrame(lyrics_data)
    lyrics_dataset.to_csv('lyrics_dataset.csv', sep=';')

if __name__ == '__main__':
    get_lyrics('credentials/genius_credentials', 3, 2, 3)
