import time
import BaseHTTPServer
import urlparse
import flask
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
      tweets.append({"screen_name": tweet['user']['screen_name'], "tweet": tweet['text']})
      if len(tweets) >= 5:
        break

    return tweets

  except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)
    return []

def to_html(tweets):
  result = []
  for tweet in tweets:
    result.append("<p class='tweet'>"+tweet["tweet"]+"</p>"+"<h3 class='screen_name'>"+tweet["screen_name"]+"</h3>")
  return result

PORT_NUMBER = 8000

app = flask.Flask(__name__)

@app.route("/testing")
def hello():
    keywords = flask.request.args.getlist('keywords')
    if keywords:
      return "\n".join(to_html(twit_search(keywords)))
    else:
      return "Give me keywords!"

if __name__ == "__main__":
    app.run(port=PORT_NUMBER)

# HOST_NAME = '0.0.0.0' # !!!REMEMBER TO CHANGE THIS!!!
# PORT_NUMBER = 8000 # Maybe set this to 9000.

# class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
#   # def do_HEAD(self):
#   #   self.send_response(200)
#   #   self.send_header("Content-type", "text/html")
#   #   self.end_headers()
#   def twitSearch(self):
#     self.send_response(200)
#     self.send_header("Content-type", "text/html")
#     self.end_headers()
#     self.wfile.write("<html><head><title>Title goes here.</title></head>")
#     self.wfile.write("<body>")
#     # If someone went to "http://something.somewhere.net/foo/bar/",
#     # then self.path equals "/foo/bar/".
#     keywords = urlparse.parse_qs(urlparse.urlparse(self.path).query)['keywords']
#     result = "\n".join(to_html(twit_search(keywords)))
#     self.wfile.write(result)
#     self.wfile.write("</body></html>")
#   def favicon(self):
#     self.send_response(404)
#   def do_GET(self):
#     """Respond to a GET request."""
#     if self.path == "/favicon.ico":
#       self.favicon()
#     else:
#       self.twitSearch()

# if __name__ == '__main__':
#   server_class = BaseHTTPServer.HTTPServer
#   httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
#   print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
#   try:
#     httpd.serve_forever()
#   except KeyboardInterrupt:
#     pass
#   httpd.server_close()
#   print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)