
__author__ = 'mirko'
import pymysql
import config as cfg
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re
import string


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


for language  in ["en","fr","it","ca","es"]:


    file= open("resources/"+language+"/wordlist.txt","w")
    cur.execute("select word from dictionary where language =%s order by length(word) desc",(language))
    words=cur.fetchall()

    for word in words:
        file.write(word[0]+"\n")



