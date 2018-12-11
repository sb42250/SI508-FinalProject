# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 18:06:08 2018

@author: yyjia
"""

from finalproject import *
import unittest
import sys

class MovieClassTests(unittest.TestCase):
    def test_movie_title(self):
        self.assertEqual(movieexample.title,"Titanic")
    def test_movie_rating(self):
        self.assertEqual(movieexample.rating,"7.8")
    def test_movie_director(self):
        self.assertEqual(movieexample.director,"James Cameron")

class TweeterClassTests(unittest.TestCase):   
    def test_tweet_id(self):
        self.assertEqual(tweets[0].id,"1070130921825816576")
    def test_tweet_retweets(self):
        self.assertEqual(tweets[0].retweets,0)
    def test_tweet_favorites(self):
        self.assertIsInstance(tweets[0].favorites,int)

class DBTests(unittest.TestCase):
    def test_title(self): 
        self.assertIn(title,"Titanic")
    def test_rating(self):
        self.assertEqual(movie_rating,[['7.8']])
    def test_most_favorite_text(self):
        self.assertEqual(most_favorite_text, [['King of the world!\n\n(Alternately, "Titanic\'s box office receipts")\n\n#SuccessIn4Words https://t.co/ZA1hKbc4gz']])
    def test_insert_Tweeter(self):
        self.assertEqual(res, True)


if __name__ == "__main__":
    unittest.main(verbosity=2)