from Relations_Targets import TargetRelation

__author__ = 'mirko'

from Linguistic_resource_LIWC import LIWC
from Linguistic_resource_AFINN import AFINN
from Linguistic_resource_DAL import DAL
from Linguistic_resource_HL import HL
from Linguistic_resources import WORDLIST
import string

import re
from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()


liwc      = {"en": LIWC("en") ,"it": LIWC("it") ,"fr": LIWC("fr") ,"es": LIWC("es") ,"ca": LIWC("ca")  }
afinn     = {"en": AFINN("en"),"it": AFINN("it"),"fr": AFINN("fr"),"es": AFINN("es"),"ca": AFINN("ca") }
dal       = {"en": DAL("en")  ,"it": DAL("it")  ,"fr": DAL("fr")  ,"es": DAL("es")  ,"ca": DAL("ca")   }
hl        = {"en": HL("en")   ,"it": HL("it")   ,"fr": HL("fr")   ,"es": HL("es")   ,"ca": HL("ca")    }
wordlist  = {"en": WORDLIST("en"), "it": WORDLIST("it"), "fr": WORDLIST("fr"),"es": WORDLIST("es"),"ca": WORDLIST("ca")}
targetRelations = TargetRelation()

def getHashtag(text):

    hashtags = ' '.join(re.findall(r"#(\w+)", text))

    if len(hashtags)<1:
        hashtags="NOHASHTAG"

    return hashtags

def getHashtagplus(text,language):
    hashtagsplus=""
    for hashtag in re.findall(r"#(\w+)", text):
        hashtagsplus += " "+wordlist[language].ParseHashtag(hashtag)

    if len(hashtagsplus)<1:
        hashtagsplus="NOHASHTAGPLUS"

    return hashtagsplus

def getMention(text):

    mentions = ' '.join(re.findall(r"@(\w+)", text))

    if len(mentions)<1:
        mentions="NOMENTION"

    return mentions

def getMentionplus(text,language):
    mentionsplus=""
    for mention in re.findall(r"@(\w+)", text):
        mentionsplus += " "+wordlist[language].getMentionName(mention)

    include = set(string.ascii_letters)|set(" ")
    mentionsplus = ''.join(ch for ch in mentionsplus if ch in include)
    mentionsplus = re.sub(' {2,}',' ',mentionsplus)

    if len(mentionsplus)<1:
        mentionsplus="NOMENTIONPLUS"

    return mentionsplus

def getMentionplusplus(text,language):
    mentionsplus=""
    for mention in re.findall(r"@(\w+)", text):
        mentionsplus += " "+wordlist[language].getMentionDescription(mention)

    include = set(string.ascii_letters)|set(" ")
    mentionsplus = ''.join(ch for ch in mentionsplus if ch in include)
    mentionsplus = re.sub(' {2,}',' ',mentionsplus)

    if len(mentionsplus)<1:
        mentionsplus="NOMENTIONPLUSPLUS"

    return mentionsplus

def getExtendedText(text,language):

    extended_text=text

    for hashtag in re.findall(r"#(\w+)", text):

        extended_text=extended_text.replace(hashtag," "+wordlist[language].ParseHashtag(hashtag)+" ")

    for mention in re.findall(r"@(\w+)", text):

        extended_text=extended_text.replace(mention," "+wordlist[language].getMentionName(mention)+" ")

    print(extended_text)
    return extended_text

def getURL(text,language):
    urls=""
    for shortURL in re.findall(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", text):
        urls += " "+wordlist[language].getResolvedUrl(shortURL)

    if len(urls)<1:
        urls="NOURl"

    return urls

def getURLplus(text,language):
    conents=""
    for shortURL in re.findall(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", text):
        conents += " "+wordlist[language].getContentUrl(shortURL)

    if len(conents)<1:
        conents="NOURlCONTENT"

    return conents

def isNegation(text,language):
    return wordlist[language].isNegation(text,language)

def isNegationplus(text,language):
    text+=" "+getHashtagplus(text,language)
    return wordlist[language].isNegation(text,language)

def isExplicitVote(text,language):
    return wordlist[language].isExplicitVote(text)

def isExplicitVotePlus(text,language):

    text+=" "+getHashtagplus(text,language)

    return wordlist[language].isExplicitVote(text)

def getPOS(pos):
    pos=pos.replace("['","").replace("']","")
    pos=pos.split("', '")

    return " ".join([ row.split("\\t")[1] for row in pos if (len(row.split("\\t")) == 3)])

def getLemma(pos):
    pos=pos.replace("['","").replace("']","")
    pos=pos.split("', '")
    return " ".join([ row.split("\\t")[2] for row in pos if (len(row.split("\\t")) == 3)])


def getAFINN(text,language):
    return afinn[language].get_afinn_sentiment(text)

def getLIWC(text,language):

    return liwc[language].get_liwc_sentiment(text)

def getHL(text,language):
    return hl[language].get_HL_sentiment(text)

def getDAL(text,language):
    return dal[language].get_dal_sentiment(text)


class Tweet(object):

    tweet_id=0
    text=''
    stance=0 #-1 Against 0 Neither 1 Favour

    def __init__(self, tweet_id, text, pos, stance,language,target):

        #if("vot" in text):
        #    print(re.sub(r"#([a-zA-Z]{0,}vot[a-zA-Z]{1,})"," ",text,flags=re.IGNORECASE))
        #text=re.sub(r"#([a-zA-Z]{0,}vot[a-zA-Z]{1,})"," ",text,flags=re.IGNORECASE)
        #text=re.sub(r"#(\w+)"," ",text)
        #text=re.sub(r"@(\w+)"," ",text)

        self.tweet_id=tweet_id
        self.language=language
        self.text=re.sub(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"," ",text)



        self.pos=getPOS(pos)
        self.lemma=getLemma(pos)

        self.stance=stance
        self.target=target

        self.hashtag=getHashtag(text)
        self.hashtagplus=getHashtagplus(text,language)


        self.mention=getMention(text)
        self.mentionplus=getMentionplus(text,language)


        if language=="en": #the creators of clinton and trump corpora remove urls from text
            self.url="NOURL"
            self.urlplus="NOURL"
        else:
            self.url=getURL(text,language)
            self.urlplus=getURLplus(text,language)

        self.negation=isNegation(text,language)

        self.negationplus=isNegationplus(text,language)

        self.vote=isExplicitVote(text,language)
        self.voteplus=isExplicitVotePlus(text,language)

        self.sentimentAFINN=getAFINN(text,language)
        self.sentimentLIWC=getLIWC(text,language)
        self.sentimentHL=getHL(text,language)
        self.sentimentDAL=getDAL(text,language)

        self.extended_text=getExtendedText(text,language)
        self.targetRelations= targetRelations.get_feature(self.extended_text,language,target)


def make_tweet(tweet_id, text, pos, stance,  language,target):

    tweet = Tweet(tweet_id, text, pos, stance, language,target)

    return tweet



if __name__ == '__main__':

    print(getHashtagplus("ISTRUZIONI AL #VOTO #LEGGERE BENE LA #FOTO #referendumcostituzionale #Referendum #VotaNo #COMITATODIFENDIAMOINOSTRIFIGLI #no","it"))




    tweet = make_tweet("4264",
"@JessieJaneDuff #novoting Results matter. U may feel less safe, but that is ur mental health issues. No 9/11s on Obama's watch #SemST",
"""['@\tSYM\t@', 'JessieJaneDuff\tNP\tJessieJaneDuff', 'Results\tNNS\tresult', 'matter\tNN\tmatter', '.\tSENT\t.', 'U\tNP\tU', 'may\tMD\tmay', 'feel\tVV\tfeel', 'less\tRBR\tless', 'safe\tJJ\tsafe', ',\t,\t,', 'but\tCC\tbut', 'that\tDT\tthat', 'is\tVBZ\tbe', 'ur\tRB\tur', 'mental\tJJ\tmental', 'health\tNN\thealth', 'issues\tNNS\tissue', '.\tSENT\t.', 'No\tDT\tno', '9\tCD\t9', '/\tSYM\t/', '11s\tJJ\t11s', 'on\tIN\ton', 'Obama\tNP\tObama', "'s\tPOS\t's", 'watch\tNN\twatch', '#SemST\tNN\t#SemST']""",
"AGAINST",
"en",
"clinton")

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
    print("pos",tweet.pos)
    print("lemma",tweet.lemma)
    print("afinn",tweet.sentimentAFINN)
    print("liwc",tweet.sentimentLIWC)
    print("dal",tweet.sentimentDAL)
    print("hl",tweet.sentimentHL)
    print("targetRelations",tweet.targetRelations)

    tweet = make_tweet("4264",
"“Perché votare Sì” https://t.co/EKCNn0bSL5… #referendumcostituzionale #Referendum #4dicembre #bastaunsi #RiformaCostituzionale #iovotosi",
"""['@\tSYM\t@', 'JessieJaneDuff\tNP\tJessieJaneDuff', 'Results\tNNS\tresult', 'matter\tNN\tmatter', '.\tSENT\t.', 'U\tNP\tU', 'may\tMD\tmay', 'feel\tVV\tfeel', 'less\tRBR\tless', 'safe\tJJ\tsafe', ',\t,\t,', 'but\tCC\tbut', 'that\tDT\tthat', 'is\tVBZ\tbe', 'ur\tRB\tur', 'mental\tJJ\tmental', 'health\tNN\thealth', 'issues\tNNS\tissue', '.\tSENT\t.', 'No\tDT\tno', '9\tCD\t9', '/\tSYM\t/', '11s\tJJ\t11s', 'on\tIN\ton', 'Obama\tNP\tObama', "'s\tPOS\t's", 'watch\tNN\twatch', '#SemST\tNN\t#SemST']""",
"AGAINST",
"it",
"referendum")

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
    print("pos",tweet.pos)
    print("lemma",tweet.lemma)

