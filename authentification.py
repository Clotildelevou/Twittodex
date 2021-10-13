import tweepy
import os
import traceback
from os.path import join, dirname
from dotenv import load_dotenv

import pokemon
import logger

from os import environ
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']


def get_api():
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print("Authentication OK")
        return api
    except:
        print("Error during authentication")


def destroy_all_tweets():
    api = get_api()
    tweets = api.user_timeline(screen_name="TwittodexBot",
                               include_rts=True,
                               )
    for tweet in tweets:
        api.destroy_status(tweet.id)


def set_profile_picture(national_number):
    api = get_api()
    pp_path = pokemon.get_pokemon_pic(national_number)
    api.update_profile_image(pp_path)


# generate the daily tweet
def gen_daily_tweet(national_number, logfile):
    api = get_api()
    name = pokemon.get_pokemon_info(national_number).english_name
    description = pokemon.build_description(national_number)
    img_path = pokemon.get_pokemon_pic(national_number)
    stats_path = pokemon.get_pokemon_stats(national_number)
    weak_path = pokemon.get_pokemon_weakness(national_number)
    status = 0

    # First post
    try:
        status = api.update_with_media(img_path, description)
        logger.pokemon_posted(logfile, name)
    except:
        error = traceback.format_exc()
        logger.err_pokemon_posted(logfile, name, error)

    # stats comment
    if not os.path.exists(stats_path):
        pokemon.build_stats(national_number)

    try:
        status = api.update_with_media(stats_path, "Stats of today's Pokemon", in_reply_to_status_id=status.id,
                                       auto_populate_reply_metadata=True)
        logger.stats_posted(logfile, name)
    except:
        error = traceback.format_exc()
        logger.err_stats_posted(logfile, name, error)

    # weaknesses comment
    if not os.path.exists(weak_path):
        pokemon.build_weaknesses(national_number)

    try:
        api.update_with_media(weak_path, "Weaknesses of today's Pokemon", in_reply_to_status_id=status.id,
                              auto_populate_reply_metadata=True)
        logger.stats_posted(logfile, name)
    except:
        error = traceback.format_exc()
        logger.err_stats_posted(logfile, name, error)
