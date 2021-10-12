import tweepy
import csv
import os
from os.path import join, dirname
from dotenv import load_dotenv


# returns the connected api
def get_api(consumer_key, consumer_secret, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
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


def generate_reply(sentence):
    reply = "I just love Gengar"
    return reply


# retweets
def retweet_gengar(api):
    for tweet in api.search(q="Gengar", lang="en", rpp=2):
        tweet_to_quote_url = "https://twitter.com/twitter/statuses/" + str(tweet.id)
        api.update_status(generate_reply("text"), attachment_url=tweet_to_quote_url)


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
    api = get_api(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
