__author__ = 'mirko'
import codecs
import re
import numpy

class AFINN(object):

    afinn={}

    def __init__(self,language):
        self.afinn = {}
        #http://www2.imm.dtu.dk/pubdb/views/publication_details.php?id=6010
        file=codecs.open('resources/'+language+'/AFINN/AFINN-111.txt', encoding='UTF-8')
        for line in file:
            word, score = line.strip().split('\t')
            if word not in self.afinn:
                self.afinn[word] = []

            self.afinn[word].append(int(score))

        for key in self.afinn.keys():
            self.afinn[key]=numpy.average(self.afinn[key])

        self.pattern_split = re.compile(r"\W+")

        return

    def get_afinn_sentiment(self,text):

        sentiments=0
        words = self.pattern_split.split(text.lower())
        for word in words:
            if word in self.afinn:
                sentiments+=self.afinn[word]


        return sentiments


if __name__ == '__main__':
    afinn = AFINN()
    sentiment=afinn.get_afinn_sentiment("@tedcruz And, #HandOverTheServer she wiped clean + 30k deleted emails, explains dereliction of duty/lies re #Benghazi,etc #tcot #SemST")
    print(sentiment)

