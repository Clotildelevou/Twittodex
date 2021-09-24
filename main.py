import tweepy


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


def generate_reply(sentence):
    reply = "I just love Gengar"
    return reply


def retweet_gengar(api):
    for tweet in api.search(q="Gengar", lang="en", rpp=10):
        api.create_favorite(tweet)
        tweet_to_quote_url = "https://twitter.com/twitter/statuses/" + str(tweet.id)
        print(tweet_to_quote_url)
        api.update_status(generate_reply("text"), attachment_url=tweet_to_quote_url)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    consumer_key = "A9gcRMmWBVYTX3UdlahRNjPv8"
    consumer_secret = "HFr1gOlg3NQorYW44njr1EpmVBE3yVPwMImjKZ2pfAZyDUqQiu"
    access_token = "1441322507491942400-82hSZGU7XOjMRxq9HMJizxyBeqwp03"
    access_secret = "2nB3CKPY1Uwm5byr3GxzdyvyqeEXytn5eQtBn5il9u4pF"

    api = get_api(consumer_key, consumer_secret, access_token, access_secret)
    retweet_gengar(api)
