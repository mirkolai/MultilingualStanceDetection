__author__ = 'mirko'
import pymysql
import config as cfg
import re
import string




class WORDLIST(object):


    def __init__(self,language):

        self.include = set(string.ascii_letters)|set([" ","'","à", "è" , "é" , "ì" , "ò" ,
                                                 "ú","é","è", "à", "ù","ê", "û",
                                                "ô", "â", "î","á", "é", "í", "ó", "ú"])

        db = pymysql.connect(host=cfg.mysql['host'], # your host, usually localhost
                     user=cfg.mysql['user'], # your username
                     passwd=cfg.mysql['passwd'], # your password
                     db=cfg.mysql['db'],
                     charset='utf8') # name of the data base
        self.cur = db.cursor()
        self.cur.execute('SET NAMES utf8mb4')
        self.cur.execute("SET CHARACTER SET utf8mb4")
        self.cur.execute("SET character_set_connection=utf8mb4")
        db.commit()

        #words
        self.wordlist=[]
        self.cur.execute("select word from dictionary where language=%s",(language))
        words=self.cur.fetchall()
        for word in words:
            self.wordlist.append(word[0].lower())

        #mentions
        self.mentionlist={}
        self.cur.execute("select screen_name,name,description,place from dictionary_mentions where language=%s",(language))
        words=self.cur.fetchall()
        for word in words:
            self.mentionlist[word[0].lower()]={ "name":word[1],"description":word[2],"place":word[3] }


        #urls
        self.urllist={}
        self.cur.execute("select  shorturl, `url`, `content` from dictionary_shorturls ")
        words=self.cur.fetchall()
        for word in words:
            self.urllist[word[0]]={ "url":word[1],"content":word[2] }


        #negations
        self.negationList={}
        self.negationList["it"]=["non","senza","nessuno","nessuna","nonostante","niente","nulla","mai","neppure"]
        self.negationList["en"]=["not","n't","never","neither","nobody","no","none","nor","nothing","nowhere","no","without"]
        self.negationList["fr"]=["ne","pas","rien","non","aucun","aucune","jamais","ni","personne","nul","nulle"]
        self.negationList["es"]=["no","nunca","ninguno","ninguna","ningún","sin"]
        self.negationList["ca"]=["no","nai","ni","cap","ningú","res","enlloc","sense"]


        #to vote
        self.votelist=[]
        self.cur.execute("select word from dictionary where language=%s",(language))
        words=self.cur.fetchall()
        for word in words:
            self.votelist.append(word[0])


        return


#hashtag plus
    def ParseHashtag(self,hashtag):

        new_sentence=""
        splituppercases=re.findall('[A-Z]{0,}[a-z]{0,}', hashtag)

        for splituppercase in splituppercases:
            if len(splituppercase)>0:
                mention=self.findMentionName(splituppercase.lower())
                if splituppercase.lower() in self.wordlist:
                    new_sentence+=" "+splituppercase.lower()

                elif mention is not None:
                    new_sentence +=" "+mention
                else:

                    new_sentence +=" "+self.ParseTag(splituppercase.lower())

        if len(new_sentence)<1:
            new_sentence="NORESULTHASHTAGSPLITTING"


        return new_sentence


    def ParseTag(self, term):
        words = []
        word = self.FindWord(term)
        while word != None and len(term) > 0:
            words += [word]
            if len(term) == len(word): # Special case for when eating rest of word
                break
            term = term[len(word):]
            word = self.FindWord(term)
        return " ".join(words)


    def FindWord(self,token):
        i = len(token) + 1
        while i > 1:
            i -= 1
            if token[:i] in self.wordlist:
                return token[:i]
        return None

#mention plus
    def getMentionName(self,mention):

        for m in self.mentionlist.keys():
            if mention.lower() == m.lower():
                return self.mentionlist[mention.lower()]["name"]
        else:
            return " "

    def getMentionDescription(self,mention):

            if mention in self.mentionlist:
                return self.mentionlist[mention]["description"]
            else:
                return " "

    def findMentionName(self, token):

        for mention in sorted(self.mentionlist.keys()):
            if self.mentionlist[mention]["name"].startswith(token):
                return self.mentionlist[mention]["name"]


        return None

#urls

    def getResolvedUrl(self, shorturl):

        if shorturl in self.urllist:
             return self.urllist[shorturl]["url"].replace("."," ").replace("/"," ")

        return ""

    def getContentUrl(self, shorturl):

        if shorturl in self.urllist:
             return self.urllist[shorturl]["content"]

        return ""


#negation
    def isNegation(self, text,language):


        text = ''.join(ch for ch in text.lower() if ch in self.include)
        text = re.sub(' {2,}',' ',text)
        for key in self.negationList[language]:
            if key in text.split(" "):
                return True

        return False

#vote


    def isExplicitVote(self, text):

        text = ''.join(ch for ch in text.lower() if ch in self.include)
        text = re.sub(' {2,}',' ',text)

        for word in self.votelist:
            if word in text:
                return True

        return False


if __name__ == '__main__':

    sentence="iovotono referendumcostituzionale comitatoperilno ComitatoPerIlNO renzièunasino RenziÈunAsino"
    wordlist=WORDLIST("it")

    result=wordlist.ParseHashtag("ReferendumCostituzionale MariaElenaBoschi")
    print("ReferendumCostituzionale",result)
    result=wordlist.ParseHashtag("referendumcostituzionale")
    print("referendumcostituzionale",result)
    result=wordlist.ParseHashtag("MatteoRenziNO")
    print("MatteoRenziNO",result)
    result=wordlist.ParseHashtag("matteorenzino")
    print("matteorenzino",result)
    result=wordlist.ParseHashtag("IoVotoNO")
    print("IoVotoNO",result)
    result=wordlist.ParseHashtag("iovotono")
    print("iovotono",result)
    result=wordlist.ParseHashtag("mariaelenaboschidimettiti")
    print("mariaelenaboschidimettiti",result)
    result=wordlist.ParseHashtag("comitatoperilno")
    print("comitatoperilno",result)
    result=wordlist.ParseHashtag("renzièunasino")
    print("renzièunasino",result)

    wordlist=WORDLIST("en")

    result=wordlist.ParseHashtag("FeelTheBern")
    print("FeelTheBern SemST",result)
