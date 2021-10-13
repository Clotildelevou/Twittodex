import tweepy
import os
import traceback
from os.path import join, dirname
from dotenv import load_dotenv

import pokemon
import logger


def get_api():
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
    CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
    ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
    ACCESS_SECRET = os.environ.get("ACCESS_SECRET")

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print("Authentication OK")
        return api
    except:
        print("Error during authentication")


def set_profile_picture(national_number):
    api = get_api()
    pp_path = pokemon.get_pokemon_pic(national_number)
    api.update_profile_image(pp_path)


# generate the daily tweet
def gen_daily_tweet(national_number):
    api = get_api()
    description = pokemon.build_desc(national_number)
    img_path = pokemon.get_pokemon_pic(national_number)
    stats_path = pokemon.get_pokemon_stats(national_number)

    status = api.update_with_media(img_path, description)
    api.update_with_media(stats_path, "Stats of today's Pokemon", in_reply_to_status_id=status.id,
                          auto_populate_reply_metadata=True)

