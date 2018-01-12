
__author__ = 'mirko'

import pymysql
import config as cfg
import string
import json
import urllib.request
import urllib.parse
import time
from urllib.parse import quote_plus

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

cur.execute("truncate table dictionary")
db.commit()

for i in range(1):

    for language in ["en","it","fr","es","ca"]:

        urlData = "https://"+language+".wikipedia.org/w/api.php?action=query&list=random&rnlimit=20&format=json&rnnamespace=0"
        print(urlData)

        webURL = urllib.request.urlopen(urlData)
        data = webURL.read()
        encoding = webURL.info().get_content_charset('utf-8')

        result=json.loads(data.decode(encoding))
        #time.sleep(2)
        for page1 in result['query']['random']:
            #print(page['title'])
            page1=page1['title'].replace(" ","_")
            #page=(urllib.parse.quote(page['title'].replace(" ","_"), safe=''))
            page1=quote_plus(page1)



            urlData = "https://"+language+".wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles="+page1
            print(urlData)
            time.sleep(2)

            webURL = urllib.request.urlopen(urlData)
            data = webURL.read()
            encoding = webURL.info().get_content_charset('utf-8')
            result=json.loads(data.decode(encoding))
            #time.sleep(2)
            text=""
            for id,page2 in result["query"]["pages"].items():
                if "extract" in page2:
                    text=page2["extract"]


                include = set(string.ascii_letters)|set(" ")
                text = ''.join(ch for ch in text if ch in include)
                for word in text.lower().split(" "):

                    if not word.isdigit() and len(word)>0:

                        cur.execute("""
                        INSERT INTO `dictionary`(`word`, `language`)
                        VALUES
                        (%s,%s)
                        on duplicate key update frequency=frequency+1
                        """,(word,language))

                        db.commit()


        #time.sleep(2)

