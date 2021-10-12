import authentification
import pokemon

import os
from os.path import join, dirname
from dotenv import load_dotenv

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # gets the credentials
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
    CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
    ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
    ACCESS_SECRET = os.environ.get("ACCESS_SECRET")

    # connects the api
    api = authentification.get_api(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
    print(pokemon.get_pokemon_info(2))
    print(pokemon.build_text(2))
