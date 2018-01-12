__author__ = 'mirko'
import pymysql
import config as cfg
import re
import string

target_alias = {

    "en": {

        "clinton" : {

                    'TARGET' : ["hillaryclinton","hillary","clinton","hill"],
                    'PRONOUMS' : ["she","her"],
                    'PARTY' : ["dem","democratic","democrat","democrats","progressive"],
                    'OPPOSITEINPARTYTARGET' : ["bernie","sanders",
                                                                     "martin","o malley",
                                                                     "lincoln","chafee",
                                                                     #"jim",
                                                                     "webb",
                                                                     "lawrence","lessig"],

                    'OPPOSITEOUTPARTYTARGET' : [
                                                        "republican","republicans","conservative",
                                                        "realdonaldtrump","donald","trump","gop",
                                                        "ted","cruz",
                                                        "marco","rubio",
                                                        "john","kasich",
                                                        "ben","carson",
                                                        "jeb","bush",
                                                        "rand","paul",
                                                        "mike","huckabee",
                                                        "carly","fiorina",
                                                        "chris","christie",
                                                        "rick","santorum",
                                                        #"jim",
                                                        "gilmore",
                                                        "rick","perry",
                                                        "scott","walker",
                                                        "bobby","jindal",
                                                        "lindsey","graham",
                                                        "george","pataki"
                                                        ],
        },

        "trump"  :  {

                    'TARGET':["donald","trump"],
                    'PRONOUMS' : ["he","his"],
                    'PARTY' : ["republican","republicans","conservative"],

                    'OPPOSITEOUTPARTYTARGET': ["dem","democratic","democrat","democrats","progressive",
                                                      "hillary","clinton",
                                                      "bernie","sanders",
                                                      "martin","o malley",
                                                      "lincoln","chafee",
                                                      #"jim",
                                                      "webb",
                                                      "lawrence","lessig"],

                    'OPPOSITEINPARTYTARGET' :  [
                                                        "ted","cruz",
                                                        "marco","rubio",
                                                        "john","kasich",
                                                        "ben","carson",
                                                        "jeb","bush",
                                                        "rand","paul",
                                                        "mike","huckabee",
                                                        "carly","fiorina",
                                                        "chris","christie",
                                                        "rick","santorum",
                                                        #"jim",
                                                        "gilmore",
                                                        "rick","perry",
                                                        "scott","walker",
                                                        "bobby","jindal",
                                                        "lindsey","graham",
                                                        "george","pataki"
                                                        ]
        },
    },

    "fr": {

        "lepen" : {

            "target":["marine","le pen", "lepen"],
            "supporters":["trump"],
            "supporters_party":["fn","front national"],
            "oppositors":["emmanuel","macron","mélenchon"],
            "oppositors_party":["en marche","enmarce"],
        },

        "macron"  :  {

            "target":["emmanuel","macron"],
            "supporters":["brigitte","obama"],
            "supporters_party":["en marche","enmarche"],
            "oppositors":["marine","le pen", "lepen"],
            "oppositors_party":["fn","front national"],

        },
    },

    "it": {

        "referendum" : {

            "target":["referendum"],
            "supporters":["emma","bonino","enrico","letta","gianni","cuperlo","giuliano",
                          "pisapia","maria","elena","boschi","matteo","renzi","piero","fassino","rosy","bindi"],
            "supporters_party":["italia dei valori","partito democratico","pd","idv"],
            "oppositors":["angelino","alfano","beatrice","lorenzin","beppe","grillo","giorgia","meloni","giuseppe","civati","gustavo","agrebelsky",
                          "luigi","di maio","massimo","d alema","matteo","salvini","pierferdinando","casini","pier luigi","bersani","renato","brunetta",
                          "silvio","berlusconi"],
            "oppositors_party":["cgil","fratelli d italia","lega nord","movimento 5 stelle","sinistra ecologia libertà","sinistra italiana","alleanza nazionale","m5s","ln"],
        },

    },

    "ca": {

        "indipendencia" : {

            "target":["independència"],
            "supporters":["raül romeva", "i rueda", "jordi", "turull", "i negre"
                            "marta rovira", "i vergés", "albert batalla", "i siscart", "artur mas", "i gavarró",
                            "oriol junqueras", "i vies", "carme forcadell", "i lluís","josep lluís","franco rabell"

                          ],
            "supporters_party":["jxsí","junts pel sí","catalunya sí que es pot"
                                ,"juntos por el sí", "cataluña sí se puede", "csqp", "solidaritat catalana per la independència"
                                ],
            "oppositors":["àngel ros","i domingo","albert rivera","díaz","xavier garcía albiol"],
            "oppositors_party":["partit dels socialistes de catalunya","partit popular català","ciutadans","psc","partit de la ciutadania"],
        },

    },
    "es": {

        "indipendencia" : {

            "target":["independència"],
            "supporters":["raül romeva", "i rueda", "jordi", "turull", "i negre"
                            "marta rovira", "i vergés", "albert batalla", "i siscart", "artur mas", "i gavarró",
                            "oriol junqueras", "i vies", "carme forcadell", "i lluís","josep lluís","franco rabell"

                          ],
            "supporters_party":["jxsí","junts pel sí","catalunya sí que es pot"
                                ,"juntos por el sí", "cataluña sí se puede", "csqp", "solidaritat catalana per la independència"
                                ],
            "oppositors":["àngel ros","i domingo","albert rivera","díaz","xavier garcía","albiol"],
            "oppositors_party":["partit dels socialistes de catalunya","partit popular català","ciutadans","psc","partit de la ciutadania"],
        },

    },


}



class TargetRelation(object):

    def __init__(self):

        self.include = set(string.ascii_letters)|set([" ","'","à", "è" , "é" , "ì" , "ò" ,
                                                 "ú","é","è", "à", "ù","ê", "û",
                                                "ô", "â", "î","á", "é", "í", "ó", "ú"])


    def get_feature(self,text,language,target):


        text = ''.join(ch for ch in text.lower() if ch in self.include)
        text = re.sub(' {2,}',' ',text)
        text = text.lower()
        feature=""

        for key in target_alias[language][target].keys():

            for t in target_alias[language][target][key]:
                if " "+t.lower()+" " in text:
                    feature+=" feature_target_in_tweet_x"+key+"x "

        if feature =="":
            feature="feature_target_in_tweet_xNOTHINGx"

        print(text,feature)
        return feature


if __name__ == '__main__':

    sentence="The white male vote is solidly GOP. The black vote is solidly DEM.  That leaves white females and brown ppl. #FeelTheBern #SemST"

    targetRelation=TargetRelation()
    result=targetRelation.get_feature(sentence,"en","clinton")

    print(result)