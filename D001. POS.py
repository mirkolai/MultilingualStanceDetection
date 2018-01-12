__author__ = 'mirko'
import pymysql
import config as cfg
import treetaggerwrapper



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

treetaggerwrapper.g_langsupport["ca"]={
        "encoding": "utf-8",
        "tagparfile": "catalan-utf8.par",
        "abbrevfile": "",
        "pchar": treetaggerwrapper.ALONEMARKS + "'",
        "fchar": treetaggerwrapper.ALONEMARKS + "'",
        "pclictic": "",
        "fclictic": "",
        "number": treetaggerwrapper.NUMBER_EXPRESSION,
        "dummysentence": "Felicitats pel nou títol mundial @noramurla, i a tota la família",
        "replurlexp": 'sustituir-url>',
        "replemailexp": 'sustituir-email',
        "replipexp": 'sustituir-ip',
        "repldnsexp": 'sustituir-dns'
    }

tagger = { "es" : treetaggerwrapper.TreeTagger(TAGLANG="es") , "ca" : treetaggerwrapper.TreeTagger(TAGLANG="ca"),
           "it" : treetaggerwrapper.TreeTagger(TAGLANG="it") , "fr" : treetaggerwrapper.TreeTagger(TAGLANG="fr"),
           "en" : treetaggerwrapper.TreeTagger(TAGLANG="en") , }


for table  in [{"target": "clinton", "language":"en"},
               {"target": "trump", "language":"en"},
               {"target": "referendum", "language":"it"},
               {"target": "indipendencia", "language":"ca"},
               {"target": "indipendencia", "language":"es"},
               {"target": "macron", "language":"fr"}
               ]:

    print(table)

    cur.execute("select id, tweet from "+table["target"]+"_"+table["language"])
    tweets=cur.fetchall()

    for tweet in tweets:


        pos = tagger[table["language"]].tag_text(tweet[1])


        cur.execute(" UPDATE "+table["target"]+"_"+table["language"]+" SET POS=%s"
                    " WHERE id=%s ",
                    (str(pos),tweet[0],))
        db.commit()







