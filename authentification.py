import tweepy
import os
from os.path import join, dirname
from dotenv import load_dotenv

import pokemon


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


# cleans 200 tweets of the bot
def delete_all_tweets(api):
    tweets = api.user_timeline(screen_name="the_gengar_bot",
                               # 200 is the maximum allowed count
                               count=200,
                               include_rts=True,
                               )
    for tweet in tweets:
        api.destroy_status(tweet.id)


# generate the daily tweet
def gen_daily_tweet(national_number):
    api = get_api()
    description = pokemon.build_desc(national_number)
    img_path = pokemon.get_pokemon_pic(national_number)
    stats_path = pokemon.get_pokemon_stats(national_number)

    status = api.update_with_media(img_path, description)
    api.update_with_media(stats_path, "Stats of today's Pokemon", in_reply_to_status_id=status.id,
                          auto_populate_reply_metadata=True)

