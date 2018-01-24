from TwitterSearch import *
import sys, os
import csv

# file = open('C:/MyProjects/twitter.csv')




try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    # tso.set_keywords(['Guttenberg', 'Doktorarbeit']) # let's define all words we would like to have a look for
    tso.add_keyword("#walmart") # let's define all words we would like to have a look for
    tso.set_language('en') # we want to see German tweets only
    tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = 'YuItBDeXuC9WS5WFfeniRNKnx',
        consumer_secret = 'J9q11yQfuVfPFylLPKAdUn8JMlkHa7TcB8hBUUwRZQO8588b2G',
        access_token = '526160372-j12PDUY4NwS22HzIJ5gMn5iaXY8luzVbPIyWvRbP',
        access_token_secret = 'mkQNff1FSKkF2q2J4N88oLZljMZZfnRZX4aUAFSea22pP'
    )

    # this is where the fun actually starts :)

    for tweet in ts.search_tweets_iterable(tso):
        # print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
        print( '@%s  ' % ( tweet['user']['screen_name'] ))
        # file.write('')



except TwitterSearchException as e: # take care of all those ugly errors if there are some

    print(e)