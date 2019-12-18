import os
from twython import Twython

consumer_key        = os.environ['TWITTER_CONSUMER_KEY']
consumer_secret     = os.environ['TWITTER_CONSUMER_SECRET']
access_token        = os.environ['TWITTER_ACCESS_TOKEN']
access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

TwitterClient = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

def sendTweet(msg: str):
    global TwitterClient
    TwitterClient.update_status(status=msg)