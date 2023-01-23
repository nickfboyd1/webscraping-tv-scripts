
# Load libraries
import tweepy

# set up the API keys and access tokens
consumer_key = 'M7TGz2os40Qx9z7SGynyvhRKu'
consumer_secret = 'jTkZMs8ZVg8EqE1rFmPGyoPesnyz4JxsU46oeOWo9uJ6Z86CX8'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAENelQEAAAAA1FKhTMc1%2Fr1h5Z8v1%2B%2BtF6epUic%3DysWXrPEgdQV13Nopasscsggf0LUR611rdnbWcNrDgVybiRaA9d'
client_id = "SVliUlNDLUhDOXJOc3FkVVRMWGE6MTpjaQ"
client_secret "nny1AdkNdn-yKsZPdcC9hOSUmiRzAaUo5cuDRDaoJj0fSlfg1U"

auth = tweepy.OAuth2BearerHandler(bearer_token)
api = tweepy.API(auth)

# authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# set the text to be tweeted
text = "This is a very long string of text that I want to iteratively print out in chunks."
index = 0

# tweet the text in chunks of 10 characters
while True:
    tweet = text[index:index+10]
    api.update_status(tweet)
    index = (index + 10) % len(text)
