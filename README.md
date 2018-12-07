# SI508-FinalProject
Yujia Yang

dependencies: tweepy,psycopg2,sys,requests,json,psycopg2.extras

This project hopes to find out the rating of "Titanic" and the most fovorites tweet by searching "Titanic".

The sample output are as follows:
#The movie we search is Titanic.
#The rating of OMDB is [['7.8']].
#The most favorites tweet of the movie is [['King of the world!\n\n(Alternately, "Titanic\'s box office receipts")\n\n#SuccessIn4Words https://t.co/ZA1hKbc4gz']]

How to run the project:
1. Please clone all the files in one folder.
2. (optional)The file named "twitter_info" is my own consumer_key,consumer_secret,access_token,access_token_secret of twitter, you can use it or you can use your own.
3. "508_final_project_cache.json" is the json after caching. It already was saved in the information of "Titanic".
4. The main python file named final project.
  4.1 (optional) in this file, line 66 I use my own apikey of OMDB, you can use it or you can change it to your own.
  4.2 (REQUIRED!!!!!!) The most important part!!!!!!!!!!!!!!!
      
      !!!!!!!!!!!!!!Please! Change! The! dbname! And! the! user! to your own!!!!!!!!!!!
     
      !!!!!!!!!!!!!!Please! Change! The! dbname! And! the! user! to your own!!!!!!!!!!!
      
      !!!!!!!!!!!!!!Please! Change! The! dbname! And! the! user! to your own!!!!!!!!!!!
5. If you make sure you have already changed the dbname and the user, you can run the "finalproject" directly and the output is shown before.

How to run the test:
run it directly, and it will show like below:
test_insert_Tweeter (__main__.DBTests) ... ok
test_most_favorite_text (__main__.DBTests) ... ok
test_rating (__main__.DBTests) ... ok
test_title (__main__.DBTests) ... ok
test_movie_director (__main__.MovieClassTests) ... ok
test_movie_rating (__main__.MovieClassTests) ... ok
test_movie_title (__main__.MovieClassTests) ... ok
test_tweet_favorites (__main__.TweeterClassTests) ... ok
test_tweet_id (__main__.TweeterClassTests) ... ok
test_tweet_retweets (__main__.TweeterClassTests) ... ok

----------------------------------------------------------------------
Ran 10 tests in 0.000s

OK
The movie we search is Titanic.
The rating of OMDB is [['7.8']].
The most favorites tweet of the movie is [['King of the world!\n\n(Alternately, "Titanic\'s box office receipts")\n\n#SuccessIn4Words https://t.co/ZA1hKbc4gz']]

list of the final project requirements I have chosen to fulfill:
0. It is writen by python.
1. two data sources: Twitter and OMDB, both of them using API
2. Caching is implemented
3. Process data from each source and put in each class.
4. Import and use functionality from at least one Python module sys.
5. A test suite file containing 3 unittest.TestSuite subclasses and at least 10 test methods (beginning with test) which are non-trivial tests.
6. Running the project should produce a product that is the result of processing data:a sql database.
7. Define 2 classes: Movie and Tweeter.
8. an example of output named "output".
9. Using a library in Python that we did not study in SI 508 or use in any assignment / project: Tweepy
10. Accessing two REST APIs
11. A PostgreSQL database that includes two tables which have one relationship, from which useful queries can be made.
