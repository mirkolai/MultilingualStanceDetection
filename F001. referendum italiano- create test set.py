__author__ = 'mirko'

import pymysql
import config as cfg
import numpy as np


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

cur.execute("""

SELECT  count(*) FROM referendum_it
""")
rows = cur.fetchone()[0]

twentypercent=round(rows*0.20)
print(twentypercent)



while twentypercent>0:
    twentypercent-=1
    cur.execute("""

    SELECT id FROM referendum_it where `set` = "Training" order by rand() limit 0,1
    """)
    id = cur.fetchone()[0]
    cur.execute("""

    UPDATE  `referendum_it` SET  `Set` =  "Test" where id=%s
    """,(id))
    print(id,twentypercent)






