from TwitterSearch import *

def twit_search(keywords):
    try:
        tso = TwitterSearchOrder() # create a TwitterSearchOrder object
        tso.setKeywords(keywords) # let's define all words we would like to have a look for
        tso.setLanguage('en') # we want to see English tweets only
        tso.setCount(7) # please dear Mr Twitter, only give us 7 results per page
        tso.setIncludeEntities(False) # and don't give us all those entity information

        # it's about time to create a TwitterSearch object with our secret tokens
        ts = TwitterSearch(
            consumer_key = 'asX13sgNL5fVbVfSwyaLCw',
            consumer_secret = 'Y0SkBfcxZ5Q4AVmmXEMCcWI5lfUD3JBdgtd1fioJwU',
            access_token = '956472907-NGjoV82C6UwGu4xXLod1R3SKsWG9hfCXntt8Smxr',
            access_token_secret = '98S3jvUx5TZQxHYfBcP971ow02mTzeyQUdILamHp3Oee1'
         )

        for tweet in ts.searchTweetsIterable(tso): # this is where the fun actually starts :)
            return '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] )


    except TwitterSearchException as e: # take care of all those ugly errors if there are some
        print(e)