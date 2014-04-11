# import time
# import BaseHTTPServer
# import urlparse
import flask
import os
import json
from TwitterSearch import *

def twit_search(keywords):
  try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.setKeywords(keywords) # let's define all words we would like to have a look for
    tso.setLanguage('en') # we want to see English tweets only
    tso.setCount(7) # please dear Mr Twitter, only give us 1 result per page
    tso.setIncludeEntities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = 'asX13sgNL5fVbVfSwyaLCw',
        consumer_secret = 'Y0SkBfcxZ5Q4AVmmXEMCcWI5lfUD3JBdgtd1fioJwU',
        access_token = '956472907-NGjoV82C6UwGu4xXLod1R3SKsWG9hfCXntt8Smxr',
        access_token_secret = '98S3jvUx5TZQxHYfBcP971ow02mTzeyQUdILamHp3Oee1'
    )

    # for tweet in ts.searchTweetsIterable(tso): # this is where the fun actually starts :)
    #    return '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] )
    tweets = []
    for tweet in ts.searchTweetsIterable(tso):
      tweets.append({"screen_name": tweet['user']['screen_name'],
        "text": tweet['text'],
        "full_name": tweet['user']['name']
        })
      if len(tweets) >= 5:
        break

    return tweets

  except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)
    return []

def to_html(tweets):
  result = []
  for tweet in tweets:
    result.append("<p class='tweet'>"+tweet["text"]+"</p>"+"<h3 class='screen_name'>"+tweet["screen_name"]+"</h3>")
  return result

def to_json(tweets):
  return json.dumps(tweets)

PORT_NUMBER = 8000

app = flask.Flask(__name__, static_url_path = '/static')

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/<path:dirname>/<path:filename>')
def send_foo(dirname, filename):
    print os.path.join('static',dirname)
    return flask.send_from_directory(os.path.join('static',dirname), filename)

@app.route("/testing")
def hello():
    keywords = flask.request.args.getlist('keywords')
    if keywords:
      return "\n".join(to_html(twit_search(keywords)))
    else:
      return "Give me keywords!"

if __name__ == "__main__":
    app.run(port=PORT_NUMBER)