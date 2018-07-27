import tweepy
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

#retweet setup
for tweet in tweepy.Cursor(api.search, q="#naijamoments").items():
    try:
# Add \n escape character to print() to organize tweets
        print('\nTweet by: @' + tweet.user.screen_name)

# Retweet tweets as they are found
        tweet.retweet()
        print('Retweeted the tweet')

        sleep(5)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
    
# Follow the user who tweeted
        tweet.user.follow()
        print('Followed the user')

        sleep(5)

    except tweepy.TweepError as e:
        print(e.reason)

    if not tweet.user.following:
            tweet.user.follow()
            print('Followed the user')

    


    
