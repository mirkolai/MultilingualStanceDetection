__author__ = 'mirko'

from sklearn.externals import joblib
from Tweet import make_tweet
import os.path
import pymysql
import config as cfg

class Database_manager(object):

    db=None
    cur=None

    def __init__(self):

        self.db = pymysql.connect(host=cfg.mysql['host'],
                 user=cfg.mysql['user'],
                 passwd=cfg.mysql['passwd'],
                 db=cfg.mysql['db'],
                 charset='utf8')
        self.cur = self.db.cursor()
        self.cur.execute('SET NAMES utf8mb4')
        self.cur.execute("SET CHARACTER SET utf8mb4")
        self.cur.execute("SET character_set_connection=utf8mb4")
        self.db.commit()

    def return_tweets(self,language,target,set=None):


        if os.path.isfile('tweets_'+language+'_'+target+'_'+str(set)+'.pkl') :
            tweets= joblib.load('tweets_'+language+'_'+target+'_'+str(set)+'.pkl')
            return tweets

        where=""
        if set is not None:
            where=" WHERE `set`='"+set+"'"


        tweets=[]
        self.cur.execute(" SELECT id, tweet, pos,  stance from "+target+"_"+language+" "+where+"  order by id")
        i=0
        not_founds=0
        for tweet in self.cur.fetchall():
                i+=1
                print(i,not_founds)
                tweet_id=tweet[0]

                text=tweet[1]
                pos=tweet[2]
                stance=tweet[3]


                this_tweet=make_tweet(tweet_id, text, pos, stance,language,target)

                tweets.append(this_tweet)


        joblib.dump(tweets, 'tweets_'+language+'_'+target+'_'+str(set)+'.pkl')

        return tweets



    def return_tweets_ids(self,language,target,ids,set=None):


        where="WHERE id in "+str(ids)+" "

        if set is not None:
            where+=" and  `set`='"+set+"'"


        tweets=[]
        self.cur.execute(" SELECT id, tweet, pos,  stance from "+target+"_"+language+" "+where+"  order by id")
        i=0
        not_founds=0
        for tweet in self.cur.fetchall():
                i+=1
                tweet_id=tweet[0]

                text=tweet[1]
                pos=tweet[2]
                stance=tweet[3]


                this_tweet=make_tweet(tweet_id, text, pos, stance,language,target)

                tweets.append(this_tweet)


        return tweets




def make_database_manager():
    database_manager = Database_manager()

    return database_manager



if __name__ == '__main__':

    database_manager = Database_manager()
    for tweet in database_manager.return_tweets("en","clinton"):
        print("TWEET")
        print("TEXT",tweet.text)
        print("pos",tweet.pos)
        print("stance",tweet.stance)
        print("hashtag",tweet.hashtag)
        print("hashtagplus",tweet.hashtagplus)
        print("mention",tweet.mention)
        print("mentionplus",tweet.mentionplus)
        print("url",tweet.url)
        print("urlplus",tweet.urlplus)
        print("negation",tweet.negation)
        print("negation plus",tweet.negationplus)
        print("vote",tweet.vote)
        print("vote plus",tweet.voteplus)