__author__ = 'mirko'
import pymysql
import config as cfg
import oauth2 as oauth
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import string

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, ' ', raw_html)
  return cleantext

db = pymysql.connect(host=cfg.mysql['host'], # your host, usually localhost
             user=cfg.mysql['user'], # your username
             passwd=cfg.mysql['passwd'], # your password
             db=cfg.mysql['db'],
             charset='utf8') # name of the data base

cur = db.cursor()
cur.execute('SET NAMES utf8mb4')
cur.execute("SET CHARACTER SET utf8mb4")
cur.execute("SET character_set_connection=utf8mb4")
db.commit()

#cur.execute("truncate `dictionary_shorturls`")
#db.commit()

for table  in [{"target": "clinton_en", "language":"en"},
               {"target": "trump_en", "language":"en"},
               {"target": "referendum_it", "language":"it"},
               {"target": "indipendencia_ca", "language":"ca"},
               {"target": "indipendencia_es", "language":"es"}
               ]:


    cur.execute("select tweet from "+table["target"])
    tweets=cur.fetchall()

    for tweet in tweets:
        content=""
        for shorturl in re.findall(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", tweet[0]):

            cur.execute("select * from `dictionary_shorturls` where shorturl=%s",(shorturl))
            if cur.fetchone() == None:
                try:
                    response = urlopen(shorturl)
                    url = response.geturl()
                    print(url)

                    response = urlopen(url)
                    data = response.read()
                    encoding = response.info().get_content_charset('utf-8')
                    result=data.decode(encoding)

                    #twitter
                    soup = BeautifulSoup(result)
                    p = soup.findAll('p',{'class':'TweetTextSize TweetTextSize--jumbo js-tweet-text tweet-text'})
                    for i in p:
                        content = cleanhtml(str(p))

                    #facebook
                    if content == "":
                        div = soup.find('div',{'id':'contentArea'})
                        if div is not None:
                            span = div.findAll('span')
                            for i in span:
                                content = cleanhtml(str(p))

                    #others
                    if content == "":
                        content=""
                        p = soup.findAll('p')
                        for i in p:
                            content += cleanhtml(str(i))

                    include = set(string.ascii_letters)|set(" ")
                    content = ''.join(ch for ch in content if ch in include)
                    content = re.sub(' {2,}',' ',content)
                    print(content)

                    cur.execute("INSERT INTO `dictionary_shorturls`(`shorturl`, `url`, `content`,language)"
                                " VALUES"
                                " (%s,%s,%s,%s)"
                                " on duplicate key update shorturl=shorturl",
                                (shorturl,url,content,table["language"]))
                    db.commit()

                except:
                    url = "FOURZEROFOUR"
                    content = "FOURZEROFOUR"
                    print("Error: not found")
                    pass






