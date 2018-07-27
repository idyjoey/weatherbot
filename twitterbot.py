import tweepy
from weather import Weather, Unit
from time import sleep
# Create variables for each key, secret, token
consumer_key = 'BeYqF0eIVOZtPNLWVLtFy8PiF'
consumer_secret = 'x88fwGQtYB0FVDC4ZZW2c6k1PXAiivq8s1NemVDDrcuAqGrEgu'
access_token = 	'999255188459401216-Tf2Yrouz88ttyBsfFhYLiEq85zJLCi9'
access_token_secret = 'dkKpzTTC83hqWmkROKweZ2Y3HOUeMRQ2IP39Z06It0zKA'
# Set up OAuth and integrate with API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
# weather setup
weather = Weather(unit=Unit.CELSIUS)
location = weather.lookup_by_location('lagos')
condition = location.condition
# Write a tweet to push to our Twitter account
tweet = "the weather in lagos is" + ","  + condition.text
count = 6
for twitter in tweet:
    api.update_status(status=tweet)
    count -= 1
    sleep (3600)
