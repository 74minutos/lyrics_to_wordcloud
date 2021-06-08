import requests
import time
import urllib3
import logging
import lyricsgenius as lg

def load_api_key_from_file(filename: str) -> str:
    #loading apikey from file
    with open(filename, "r", encoding="utf8") as f:
        return f.read().strip()

logger = logging.getLogger(__name__)

def genius_api_calls(api_key_path:str, artist: str, max_songs: int, seconds: int, retries: int) -> None:
    client_token = load_api_key_from_file(api_key_path)
    genius = lg.Genius(client_token, skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"],
                                 remove_section_headers=True)
    for i in range(retries):
        try:
            songs = genius.search_artist(artist, max_songs=max_songs, sort='popularity').songs
            return songs
        except requests.exceptions.Timeout:
            time.sleep(2 * (2 ** i))
        except requests.exceptions.HTTPError as e:
            logger.warning("http exception: {0}".format(str(e)))
            logger.warning("text: {0}".format(e.response.text))
            time.sleep(2 * (2 ** i))
        except requests.exceptions.ConnectionError as e:
            logger.warning("connection exception: {0}".format(str(e)))
            time.sleep(seconds * (2 ** i))
        except urllib3.exceptions.ProtocolError as e:
            logger.warning("connection exception: {0}".format(str(e)))
            time.sleep(seconds * (2 ** i))
        except AttributeError:
            pass
    raise Exception("max retries exceeded")
