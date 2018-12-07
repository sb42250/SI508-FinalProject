# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 20:26:27 2018

@author: yyjia
"""


import itertools
import collections
import requests
import tweepy
import twitter_info
import json
import psycopg2 # Library for interacting with Postgres. Need to install for your Python.
# Load the psycopg extras module:
import psycopg2.extras
import sys

#Tweepy setup
consumer_key = twitter_info.consumer_key
consumer_secret = twitter_info.consumer_secret
access_token = twitter_info.access_token
access_token_secret = twitter_info.access_token_secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
public_tweets = api.user_timeline('LeoDiCaprio')
#for tweet in public_tweets:
    #print (tweet.text)

CACHE_FNAME = "508_final_project_cache.json"
try:
    cache_file = open(CACHE_FNAME,'r')
    cache_contents = cache_file.read()
    cache_file.close()
    CACHE_DICTION = json.loads(cache_contents)
except:
	 CACHE_DICTION = {}
	 CACHE_DICTION["OMDB"] = {}
	 CACHE_DICTION["Twitter"] = {}


def get_twitter_search_data(search_term):
    if search_term in CACHE_DICTION["Twitter"]:
        response = CACHE_DICTION["Twitter"][search_term]
    else:
        searched_tweets = [status._json for status in tweepy.Cursor(api.search,  q=search_term).items(100)]
        response = json.dumps(searched_tweets)
        
        CACHE_DICTION["Twitter"][search_term] = response
        cache_file = open(CACHE_FNAME, 'w')
        cache_file.write(json.dumps(CACHE_DICTION))
        cache_file.close()
    return response
#titanic = get_twitter_search_data("The Dark Knight")
#for tweet in titanic.items():
   #print (tweet)
def get_OMDB_data(search_term):
    if search_term in CACHE_DICTION["OMDB"]:
        response = CACHE_DICTION["OMDB"][search_term]
    else:
        base_url = "http://www.omdbapi.com/"
        params = {}
        params["t"] = search_term
        params["apikey"] = "8b77328f"
        r = requests.get(base_url, params=params)
        response = json.loads(r.text)
        CACHE_DICTION["OMDB"][search_term] = response
        cache_file = open(CACHE_FNAME, 'w')
        cache_file.write(json.dumps(CACHE_DICTION))
        cache_file.close()
    return response
#print(get_OMDB_data("Titanic"))
class Movie(object):
    def __init__(self, diction):
        self.title = diction["Title"]
        self.movie_id = diction["imdbID"]
        self.director = diction["Director"]
        self.rating = diction["imdbRating"]

class Tweeter():
    def __init__(self, diction):
        self.id = diction['id_str']    
        self.text = diction['text']
        self.user = diction['user']['name']
        self.favorites = diction['user']['favourites_count']
        self.retweets = diction['retweet_count']
        self.userid = diction['user']['id_str']
        self.followers = diction['user']['followers_count']
        

moviename = "Titanic"
omdb_movie = get_OMDB_data(moviename)
#print(omdb_movie)
movieexample = Movie(omdb_movie)
#print(type(movieexample.rating))
movie_tweets = get_twitter_search_data(moviename)
#print(movie_tweets)
#tweets = [Tweeter(diction) for diction in movie_tweets]
tweets = []
res = json.loads(movie_tweets)
for diction in res:
    x = Tweeter(diction)
    #print(x.favorites)
    tweets.append(x)
#print(tweets[0].favorites)
 
#########database###############
try:
    conn = psycopg2.connect("dbname='finalproject' user='postgres' password='199652yyjYYJ,.'") # No password on the databases yet -- wouldn't want to save that in plain text in the program, anyway
    #print("success")
except:
    print("Unable to connect to the database. Check server and credentials.")
    sys.exit(1)

cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

cur.execute("DROP TABLE IF EXISTS Twitter")
cur.execute("DROP TABLE IF EXISTS Movies")
cur.execute("CREATE TABLE IF NOT EXISTS Movies(Title VARCHAR(64) PRIMARY KEY,Movie_id VARCHAR(64),Director VARCHAR(64),Rating VARCHAR(64))")
cur.execute("CREATE TABLE IF NOT EXISTS Twitter(ID VARCHAR(64) PRIMARY KEY,Text VARCHAR(10000), Users VARCHAR(64), Favorites INTEGER, Retweets INTEGER, Userid VARCHAR(64), Followers INTEGER, Title VARCHAR(64) REFERENCES Movies(Title))")

def insert_movie(title,movie_id,director,rating):
    """Inserts a movie and returns title, None if unsuccessful"""
    sql = """INSERT INTO Movies(Title,Movie_id,Director,Rating) VALUES(%s, %s, %s, %s)"""
    cur.execute(sql,(title,movie_id,director,rating))
    conn.commit()
    return title


def insert_Tweeter(id,text,user,favorites,retweets,userid,followers,title):
    """Returns True if succcessful, False if not"""
    #title = insert_movie(movieexample.title,movieexample.movie_id,movieexample.director,movieexample.rating)
    sql = """INSERT INTO Twitter(ID,Text,Users, Favorites, Retweets, Userid, Followers, Title) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"""
    cur.execute(sql,(id,text,user,favorites,retweets,userid,followers,title))
    conn.commit()
    return True



title = insert_movie(movieexample.title,movieexample.movie_id,movieexample.director,movieexample.rating)
#print(rate)


for tweet in tweets:
    res = insert_Tweeter(tweet.id,tweet.text,tweet.user,tweet.favorites,tweet.retweets,tweet.userid,tweet.followers,title)

#print(len())


cur.execute("SELECT Rating FROM Movies" )
movie_rating = cur.fetchall()
cur.execute("SELECT Text FROM Twitter WHERE Twitter.Favorites=(SELECT MAX(Favorites) FROM Twitter)")
most_favorite_text=cur.fetchall()
print("The movie we search is {}. \nThe rating of OMDB is {}. \nThe most favorites tweet of the movie is {}".format(moviename,movie_rating,most_favorite_text))

