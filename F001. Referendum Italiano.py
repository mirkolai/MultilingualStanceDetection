__author__ = 'mirko'

import pymysql
import config as cfg
import numpy as np

""" Computes the Fleiss' Kappa value as described in (Fleiss, 1971) """
"""
\kappa 	Interpretation
< 0	Poor agreement
0.01 – 0.20	Slight agreement
0.21 – 0.40	Fair agreement
0.41 – 0.60	Moderate agreement
0.61 – 0.80	Substantial agreement
0.81 – 1.00	Almost perfect agreement

"""


DEBUG = True

def computeKappa(mat):
    """ Computes the Kappa value
        @param n Number of rating per subjects (number of human raters)
        @param mat Matrix[subjects][categories]
        @return The Kappa value """
    n = checkEachLineCount(mat)   # PRE : every line count must be equal to n
    N = len(mat)
    k = len(mat[0])

    if DEBUG:
        print(N, "raters.")
        print(N, "subjects.")
        print(k, "categories.")

    # Computing p[]
    p = [0.0] * k
    for j in range(0,k):
        p[j] = 0.0
        for i in range(0,N):
            p[j] += mat[i][j]
        p[j] /= N*n

    # Computing P[]
    P = [0.0] * N
    for i in range(0,N):
        P[i] = 0.0
        for j in range(0,k):
            P[i] += mat[i][j] * mat[i][j]
        P[i] = (P[i] - n) / (n * (n - 1))

    # Computing Pbar
    Pbar = sum(P) / N

    # Computing PbarE
    PbarE = 0.0
    for pj in p:
        PbarE += pj * pj

    kappa = (Pbar - PbarE) / (1 - PbarE)

    return kappa

def checkEachLineCount(mat):
    """ Assert that each line has a constant number of ratings
        @param mat The matrix checked
        @return The number of ratings
        @throws AssertionError If lines contain different number of ratings """
    n = sum(mat[0])

    assert all(sum(line) == n for line in mat[1:]), "Line count != %d (n value)." % n
    return n


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

SELECT  `Stance` FROM referendum_it_row WHERE 1
""")
rows = cur.fetchall()

categories=[]
for row in rows:

    contributors = [ r.split("|")[0] for r in row[0].split("\n")]
    print(contributors)
    for contributor in contributors:
        if contributor not in categories:
            categories.append(contributor)

mat=[

]
for row in rows:
    object=np.zeros(len(categories))

    contributors = [ r.split("|")[0] for r in row[0].split("\n")]

    for contributor in contributors:
        object[categories.index(contributor)]+=1
    mat.append(object)
kappa = computeKappa(mat)
print(kappa)




