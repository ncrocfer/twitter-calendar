#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from datetime import date, timedelta
import json
import re
import sys
import time
import tweepy

# Twitter API
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""


def get_tweets(username):
    '''
    This function retrieves the 3200 last tweets for a user. This limit
    is imposed by Twitter.

    It records the timestamps in a json file, handled by the Cal-HeatMap plugin.
    '''
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    try:
        tweets = api.user_timeline(screen_name=username, count=200)
    except tweepy.error.TweepError:
        print('[!] This account does not seem to exist')
        exit()

    all = []
    all.extend(tweets)

    while len(tweets) > 0:
        tweets = api.user_timeline(screen_name=username, count=200, max_id=int(all[-1].id - 1))
        all.extend(tweets)

        print("[*] {} tweets downloaded".format(len(all)))

    out = {int(time.mktime(tweet.created_at.timetuple())): 1 for tweet in all}
    with open('tweets.json', 'w') as f:
        json.dump(out, f)

def change_calendar_start():
    '''
    This function is used to change the starting date in the index.html file.
    '''
    last_year = date.today() - timedelta(days=364)
    with open('index.html', "r") as f:
        content = re.sub(r'[0-9]{4},[0-9]{1,2},[0-9]{1,2}',
                         '{d.year},{d.month},{d.day}'.format(d=last_year),
                         f.read())

    with open('index.html', 'w') as f:
        f.write((content))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script to create the JSON file used by the Twitter calendar.')
    parser.add_argument('-u', '--user',
                        help='the user\'s twitter account',
                        required='True',
                        default='ncrocfer')

    args = parser.parse_args(sys.argv[1:])

    print('[*] Get {}\'s tweets...'.format(args.user))
    change_calendar_start()
    get_tweets(args.user)
