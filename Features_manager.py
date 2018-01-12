__author__ = 'mirko'

from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import re
from scipy.sparse import csr_matrix, hstack



class Features_manager(object):

    def __init__(self):


        return

    def get_stance(self,tweets):

        stance  = []

        for tweet in tweets:
            stance.append(tweet.stance)


        return stance


    #features extractor
    def create_feature_space(self , tweets , featureset , tweet_test=None):


        global_featureset={
            "baseline"      : self.get_Baseline(tweets, tweet_test),
            #stylistic
            "BoW"           : self.get_BoW_features(tweets, tweet_test),
            "BoP"           : self.get_BoP_features(tweets, tweet_test),
            "BoL"           : self.get_BoL_features(tweets, tweet_test),
            "BoC"           : self.get_BoC_features(tweets, tweet_test),
            #structural
            "hashtagplus"   : self.get_hashtagplus_features(tweets, tweet_test),
            "hashtag"       : self.get_hashtag_features(tweets, tweet_test),
            "numhashtag"    : self.get_numhashtag_features(tweets, tweet_test),
            "mention"       : self.get_mention_features(tweets, tweet_test), #micai
            "nummention"    : self.get_nummention_features(tweets, tweet_test), #micai
            "uppercase"     : self.get_uppercase_features(tweets, tweet_test),
            "punctuation"   : self.get_puntuaction_marks_features(tweets, tweet_test),
            "length"        : self.get_length_features(tweets, tweet_test),
            #contextual
            "language"      : self.get_language(tweets, tweet_test),
            "BoURL"         : self.get_BoURL_features(tweets, tweet_test),
            "targetrelation": self.get_targetrelation_feature(tweets, tweet_test),
            #sentiment
            "afinn"         : self.get_sentimen_AFINN(tweets, tweet_test), #micai
            "liwc"          : self.get_sentimen_LIWC(tweets, tweet_test),#micai
            "hl"            : self.get_sentimen_HL(tweets, tweet_test),#micai
            "dal"           : self.get_sentimen_DAL(tweets, tweet_test),#micai






        }

        if tweet_test is None:
            all_feature_names=[]
            all_feature_index=[]
            all_X=[]
            index=0
            for key in featureset:
                X,feature_names=global_featureset[key]

                current_feature_index=[]
                for i in range(0,len(feature_names)):
                    current_feature_index.append(index)
                    index+=1
                all_feature_index.append(current_feature_index)

                all_feature_names=np.concatenate((all_feature_names,feature_names))
                if all_X!=[]:
                    all_X=csr_matrix(hstack((all_X,X)))
                else:
                    all_X=X

            return all_X, all_feature_names, np.array(all_feature_index)
        else:
            all_feature_names=[]
            all_feature_index=[]
            all_X=[]
            all_X_test=[]
            index=0
            for key in featureset:
                X,X_test,feature_names=global_featureset[key]

                current_feature_index=[]
                for i in range(0,len(feature_names)):
                    current_feature_index.append(index)
                    index+=1
                all_feature_index.append(current_feature_index)

                all_feature_names=np.concatenate((all_feature_names,feature_names))
                if all_X!=[]:
                    all_X=csr_matrix(hstack((all_X,X)))
                    all_X_test=csr_matrix(hstack((all_X_test,X_test)))
                else:
                    all_X=X
                    all_X_test=X_test

            return all_X, all_X_test, all_feature_names, np.array(all_feature_index)

    def get_Baseline(self, tweets,tweet_test=None):

        tfidfVectorizer = CountVectorizer(ngram_range=(1,1),
                                          lowercase=True,
                                          binary=True,
                                          max_features=500000)

        if tweet_test is None:
            feature  = []
            for tweet in tweets:

                feature.append(tweet.text)


            tfidfVectorizer = tfidfVectorizer.fit(feature)

            X = tfidfVectorizer.transform(feature)

            feature_names=tfidfVectorizer.get_feature_names()

            return X, feature_names
        else:
            feature  = []
            feature_test  = []
            for tweet in tweets:
                feature.append(tweet.text)

            for tweet in tweet_test:
                feature_test.append(tweet.text)


            tfidfVectorizer = tfidfVectorizer.fit(feature)

            X_train = tfidfVectorizer.transform(feature)
            X_test = tfidfVectorizer.transform(feature_test)

            feature_names=tfidfVectorizer.get_feature_names()

            return X_train, X_test, feature_names


    def get_BoW_features(self, tweets,tweet_test=None):

        tfidfVectorizer = CountVectorizer(ngram_range=(1,3),
                                          lowercase=True,
                                          binary=True,
                                          max_features=500000)

        if tweet_test is None:
            feature  = []
            for tweet in tweets:

                feature.append(tweet.text)


            tfidfVectorizer = tfidfVectorizer.fit(feature)

            X = tfidfVectorizer.transform(feature)

            feature_names=tfidfVectorizer.get_feature_names()

            return X, feature_names
        else:
            feature  = []
            feature_test  = []
            for tweet in tweets:
                feature.append(tweet.text)

            for tweet in tweet_test:
                feature_test.append(tweet.text)


            tfidfVectorizer = tfidfVectorizer.fit(feature)

            X_train = tfidfVectorizer.transform(feature)
            X_test = tfidfVectorizer.transform(feature_test)

            feature_names=tfidfVectorizer.get_feature_names()

            return X_train, X_test, feature_names

    def get_BoC_features(self, tweets,tweet_test=None):

        tfidfVectorizer = CountVectorizer(ngram_range=(2,5),
                                          analyzer="char",
                                          lowercase=True,
                                          binary=True,
                                          max_features=500000)

        if tweet_test is None:
            feature  = []
            for tweet in tweets:

                feature.append(tweet.text)


            tfidfVectorizer = tfidfVectorizer.fit(feature)

            X = tfidfVectorizer.transform(feature)

            feature_names=tfidfVectorizer.get_feature_names()

            return X, feature_names
        else:
            feature  = []
            feature_test  = []
            for tweet in tweets:
                feature.append(tweet.text)

            for tweet in tweet_test:
                feature_test.append(tweet.text)


            tfidfVectorizer = tfidfVectorizer.fit(feature)

            X_train = tfidfVectorizer.transform(feature)
            X_test = tfidfVectorizer.transform(feature_test)

            feature_names=tfidfVectorizer.get_feature_names()

            return X_train, X_test, feature_names

    def get_BoP_features(self, tweets,tweet_test=None):


        tfidfVectorizer = CountVectorizer(ngram_range=(1,3),
                                          lowercase=False,
                                          binary=True,
                                          max_features=500000)

        if tweet_test is None:
            feature  = []
            for tweet in tweets:

                feature.append(tweet.pos)


            tfidfVectorizer = tfidfVectorizer.fit(feature)

            X = tfidfVectorizer.transform(feature)

            feature_names=tfidfVectorizer.get_feature_names()

            return X, feature_names
        else:
            feature  = []
            feature_test  = []
            for tweet in tweets:
                feature.append(tweet.pos)

            for tweet in tweet_test:
                feature_test.append(tweet.pos)


            tfidfVectorizer = tfidfVectorizer.fit(feature)

            X_train = tfidfVectorizer.transform(feature)
            X_test = tfidfVectorizer.transform(feature_test)

            feature_names=tfidfVectorizer.get_feature_names()

            return X_train, X_test, feature_names

    def get_BoL_features(self, tweets,tweet_test=None):


        tfidfVectorizer = CountVectorizer(ngram_range=(1,3),
                                          lowercase=False,
                                          binary=True,
                                          max_features=500000)

        if tweet_test is None:
            feature  = []
            for tweet in tweets:

                feature.append(tweet.lemma)


            tfidfVectorizer = tfidfVectorizer.fit(feature)

            X = tfidfVectorizer.transform(feature)

            feature_names=tfidfVectorizer.get_feature_names()

            return X, feature_names
        else:
            feature  = []
            feature_test  = []
            for tweet in tweets:
                feature.append(tweet.lemma)

            for tweet in tweet_test:
                feature_test.append(tweet.lemma)


            tfidfVectorizer = tfidfVectorizer.fit(feature)

            X_train = tfidfVectorizer.transform(feature)
            X_test = tfidfVectorizer.transform(feature_test)

            feature_names=tfidfVectorizer.get_feature_names()

            return X_train, X_test, feature_names

    def get_hashtag_features(self, tweets,tweet_test=None):


        tfidfVectorizer = CountVectorizer(ngram_range=(1,1),
                                          lowercase=True,
                                          binary=True,
                                          max_features=500000)


        if tweet_test is None:
            feature  = []
            for tweet in tweets:

                feature.append(tweet.hashtag)


            tfidfVectorizer = tfidfVectorizer.fit(feature)

            X = tfidfVectorizer.transform(feature)

            feature_names=tfidfVectorizer.get_feature_names()

            return X, feature_names
        else:
            feature  = []
            feature_test  = []
            for tweet in tweets:
                feature.append(tweet.hashtag)

            for tweet in tweet_test:
                feature_test.append(tweet.hashtag)


            tfidfVectorizer = tfidfVectorizer.fit(feature)

            X_train = tfidfVectorizer.transform(feature)
            X_test = tfidfVectorizer.transform(feature_test)

            feature_names=tfidfVectorizer.get_feature_names()

            return X_train, X_test, feature_names

    def get_mention_features(self, tweets,tweet_test=None):


        tfidfVectorizer = CountVectorizer(ngram_range=(1,1),
                                          lowercase=True,
                                          binary=True,
                                          max_features=500000)



        if tweet_test is None:
            feature  = []
            for tweet in tweets:

                feature.append(tweet.mention)


            tfidfVectorizer = tfidfVectorizer.fit(feature)

            X = tfidfVectorizer.transform(feature)

            feature_names=tfidfVectorizer.get_feature_names()

            return X, feature_names
        else:
            feature  = []
            feature_test  = []
            for tweet in tweets:
                feature.append(tweet.mention)

            for tweet in tweet_test:
                feature_test.append(tweet.mention)


            tfidfVectorizer = tfidfVectorizer.fit(feature)

            X_train = tfidfVectorizer.transform(feature)
            X_test = tfidfVectorizer.transform(feature_test)

            feature_names=tfidfVectorizer.get_feature_names()

            return X_train, X_test, feature_names


    def get_hashtagplus_features(self, tweets,tweet_test=None):


        tfidfVectorizer = CountVectorizer(ngram_range=(1,1),
                                          lowercase=True,
                                          binary=True,
                                          max_features=500000)

        if tweet_test is None:
            feature  = []
            for tweet in tweets:

                feature.append(tweet.hashtagplus)


            tfidfVectorizer = tfidfVectorizer.fit(feature)

            X = tfidfVectorizer.transform(feature)

            feature_names=tfidfVectorizer.get_feature_names()

            return X, feature_names
        else:
            feature  = []
            feature_test  = []
            for tweet in tweets:
                feature.append(tweet.hashtagplus)

            for tweet in tweet_test:
                feature_test.append(tweet.hashtagplus)


            tfidfVectorizer = tfidfVectorizer.fit(feature)

            X_train = tfidfVectorizer.transform(feature)
            X_test = tfidfVectorizer.transform(feature_test)

            feature_names=tfidfVectorizer.get_feature_names()

            return X_train, X_test, feature_names

    def get_mentionplus_features(self, tweets,tweet_test=None):


        tfidfVectorizer = CountVectorizer(ngram_range=(1,2),
                                          lowercase=True,
                                          binary=True,
                                          max_features=500000)

        if tweet_test is None:
            feature  = []
            for tweet in tweets:

                feature.append(tweet.mentionplus)


            tfidfVectorizer = tfidfVectorizer.fit(feature)

            X = tfidfVectorizer.transform(feature)

            feature_names=tfidfVectorizer.get_feature_names()

            return X, feature_names
        else:
            feature  = []
            feature_test  = []
            for tweet in tweets:
                feature.append(tweet.mentionplus)

            for tweet in tweet_test:
                feature_test.append(tweet.mentionplus)


            tfidfVectorizer = tfidfVectorizer.fit(feature)

            X_train = tfidfVectorizer.transform(feature)
            X_test = tfidfVectorizer.transform(feature_test)

            feature_names=tfidfVectorizer.get_feature_names()

            return X_train, X_test, feature_names

    def get_numhashtag_features(self, tweets,tweet_test=None):


        if tweet_test is None:
            feature  = []

            for tweet in tweets:
                feature.append(len(re.findall(r"#(\w+)", tweet.text)))

            return csr_matrix(np.vstack(feature)),[""]

        else:
            feature  = []
            feature_test  = []

            for tweet in tweets:
                feature.append(len(re.findall(r"#(\w+)", tweet.text)))

            for tweet in tweet_test:
                feature_test.append(len(re.findall(r"#(\w+)", tweet.text)))

            return csr_matrix(np.vstack(feature)),csr_matrix(np.vstack(feature_test)),["feature_hashtag"]


    def get_nummention_features(self, tweets,tweet_test=None):


        if tweet_test is None:
            feature  = []

            for tweet in tweets:
                feature.append(len(re.findall(r"@(\w+)", tweet.text)))

            return csr_matrix(np.vstack(feature)),[""]

        else:
            feature  = []
            feature_test  = []

            for tweet in tweets:
                feature.append(len(re.findall(r"@(\w+)", tweet.text)))

            for tweet in tweet_test:
                feature_test.append(len(re.findall(r"@(\w+)", tweet.text)))

            return csr_matrix(np.vstack(feature)),csr_matrix(np.vstack(feature_test)),["feature_mention"]

    def get_BoURL_features(self, tweets,tweet_test=None):


        tfidfVectorizer = CountVectorizer(ngram_range=(1,3),
                                          lowercase=False,
                                          binary=True,
                                          max_features=500000)

        if tweet_test is None:
            feature  = []
            for tweet in tweets:

                feature.append(tweet.url)


            tfidfVectorizer = tfidfVectorizer.fit(feature)

            X = tfidfVectorizer.transform(feature)

            feature_names=tfidfVectorizer.get_feature_names()

            return X, feature_names
        else:
            feature  = []
            feature_test  = []
            for tweet in tweets:
                feature.append(tweet.url)

            for tweet in tweet_test:
                feature_test.append(tweet.url)


            tfidfVectorizer = tfidfVectorizer.fit(feature)

            X_train = tfidfVectorizer.transform(feature)
            X_test = tfidfVectorizer.transform(feature_test)

            feature_names=tfidfVectorizer.get_feature_names()

            return X_train, X_test, feature_names

    def get_BoURLplus_features(self, tweets,tweet_test=None):


        tfidfVectorizer = CountVectorizer(ngram_range=(1,3),
                                          lowercase=False,
                                          binary=True,
                                          max_features=500000)

        if tweet_test is None:
            feature  = []
            for tweet in tweets:

                feature.append(tweet.urlplus)


            tfidfVectorizer = tfidfVectorizer.fit(feature)

            X = tfidfVectorizer.transform(feature)

            feature_names=tfidfVectorizer.get_feature_names()

            return X, feature_names
        else:
            feature  = []
            feature_test  = []
            for tweet in tweets:
                feature.append(tweet.urlplus)

            for tweet in tweet_test:
                feature_test.append(tweet.urlplus)


            tfidfVectorizer = tfidfVectorizer.fit(feature)

            X_train = tfidfVectorizer.transform(feature)
            X_test = tfidfVectorizer.transform(feature_test)

            feature_names=tfidfVectorizer.get_feature_names()

            return X_train, X_test, feature_names

    def get_negation_feature(self,tweets,tweet_test=None):

        if tweet_test is None:
            feature  = []

            for tweet in tweets:
                feature.append([   tweet.negation     ])

            return csr_matrix(np.vstack(feature)),["feature_negation"]

        else:
            feature  = []
            feature_test  = []

            for tweet in tweets:
                feature.append([   tweet.negation     ])

            for tweet in tweet_test:
                feature_test.append([   tweet.negation     ])

            return csr_matrix(np.vstack(feature)),csr_matrix(np.vstack(feature_test)),["feature_negation"]



    def get_negationplus_feature(self,tweets,tweet_test=None):
        if tweet_test is None:
            feature  = []

            for tweet in tweets:
                feature.append([   tweet.negationplus     ])

            return csr_matrix(np.vstack(feature)),["feature_negationplus"]

        else:
            feature  = []
            feature_test  = []

            for tweet in tweets:
                feature.append([   tweet.negationplus     ])

            for tweet in tweet_test:
                feature_test.append([   tweet.negationplus     ])

            return csr_matrix(np.vstack(feature)),csr_matrix(np.vstack(feature_test)),["feature_negationplus"]

    def get_explicitvote_feature(self,tweets,tweet_test=None):
        if tweet_test is None:
            feature  = []

            for tweet in tweets:
                feature.append([   tweet.vote     ])

            return csr_matrix(np.vstack(feature)),["feature_vote"]

        else:
            feature  = []
            feature_test  = []

            for tweet in tweets:
                feature.append([   tweet.vote     ])

            for tweet in tweet_test:
                feature_test.append([   tweet.vote     ])

            return csr_matrix(np.vstack(feature)),csr_matrix(np.vstack(feature_test)),["feature_vote"]

    def get_explicitvoteplus_feature(self,tweets,tweet_test=None):
        if tweet_test is None:
            feature  = []

            for tweet in tweets:
                feature.append([   tweet.voteplus     ])

            return csr_matrix(np.vstack(feature)),["feature_voteplus "]

        else:
            feature  = []
            feature_test  = []

            for tweet in tweets:
                feature.append([   tweet.voteplus      ])

            for tweet in tweet_test:
                feature_test.append([   tweet.voteplus      ])

            return csr_matrix(np.vstack(feature)),csr_matrix(np.vstack(feature_test)),["feature_voteplus "]




    def get_puntuaction_marks_features(self,tweets,tweet_test=None):
        if tweet_test is None:
            feature  = []

            for tweet in tweets:
                feature.append([
                    len(re.findall(r"[!]", tweet.text)),
                    len(re.findall(r"[?]", tweet.text)),
                    len(re.findall(r"[.]", tweet.text)),
                    len(re.findall(r"[,]", tweet.text)),
                    len(re.findall(r"[;]", tweet.text)),
                    len(re.findall(r"[!?.,;]", tweet.text)),
                    ]

                )
            return csr_matrix(np.vstack(feature)),["feature_pun1","feature_pun2","feature_pun3","feature_pun4","feature_pun5","feature_pun6"]

        else:
            feature  = []
            feature_test  = []

            for tweet in tweets:
                feature.append([
                    len(re.findall(r"[!]", tweet.text)),
                    len(re.findall(r"[?]", tweet.text)),
                    len(re.findall(r"[.]", tweet.text)),
                    len(re.findall(r"[,]", tweet.text)),
                    len(re.findall(r"[;]", tweet.text)),
                    len(re.findall(r"[!?.,;]", tweet.text)),
                    ]

                )
            for tweet in tweet_test:
                feature_test.append([
                    len(re.findall(r"[!]", tweet.text)),
                    len(re.findall(r"[?]", tweet.text)),
                    len(re.findall(r"[.]", tweet.text)),
                    len(re.findall(r"[,]", tweet.text)),
                    len(re.findall(r"[;]", tweet.text)),
                    len(re.findall(r"[!?.,;]", tweet.text)),
                    ]

                )

            return csr_matrix(np.vstack(feature)),csr_matrix(np.vstack(feature_test)),["feature_pun1","feature_pun2","feature_pun3","feature_pun4","feature_pun5","feature_pun6"]


    def get_length_features(self,tweets,tweet_test=None):
        if tweet_test is None:
            feature  = []

            for tweet in tweets:
                feature.append([
                            len(tweet.text),
                            np.average([len(w) for w in tweet.text.split(" ")]),
                            len(tweet.text.split(" ")),

                            ]

                        )
            return csr_matrix(np.vstack(feature)),["feature_charlen","feature_avgwordleng","feature_numword"]

        else:
            feature  = []
            feature_test  = []

            for tweet in tweets:
                feature.append([
                            len(tweet.text),
                            np.average([len(w) for w in tweet.text.split(" ")]),
                            len(tweet.text.split(" ")),

                            ]

                        )
            for tweet in tweet_test:
                feature_test.append([
                            len(tweet.text),
                            np.average([len(w) for w in tweet.text.split(" ")]),
                            len(tweet.text.split(" ")),

                            ]

                        )

            return csr_matrix(np.vstack(feature)),csr_matrix(np.vstack(feature_test)),["feature_charlen","feature_avgwordleng","feature_numword"]

    def get_lengthplus_features(self,tweets,tweet_test=None):

        if tweet_test is None:
            feature  = []

            for tweet in tweets:
                feature.append([
                len(re.sub(r"[#@](\w+)"," ",tweet.text)),
                np.average([len(w) for w in re.sub(r"[#@](\w+)"," ",tweet.text).split(" ") ]),
                len(re.sub(r"[#@](\w+)"," ",tweet.text).split(" ")),

                ]

                 )
            return csr_matrix(np.vstack(feature)),["feature_charlenplus","feature_avgwordlengplus","feature_numwordplus"]

        else:
            feature  = []
            feature_test  = []

            for tweet in tweets:
                feature.append([
                len(re.sub(r"[#@](\w+)"," ",tweet.text)),
                np.average([len(w) for w in re.sub(r"[#@](\w+)"," ",tweet.text).split(" ") ]),
                len(re.sub(r"[#@](\w+)"," ",tweet.text).split(" ")),

                ]

                 )
            for tweet in tweet_test:
                feature_test.append([
                len(re.sub(r"[#@](\w+)"," ",tweet.text)),
                np.average([len(w) for w in re.sub(r"[#@](\w+)"," ",tweet.text).split(" ") ]),
                len(re.sub(r"[#@](\w+)"," ",tweet.text).split(" ")),

                ]

                 )

            return csr_matrix(np.vstack(feature)),csr_matrix(np.vstack(feature_test)),["feature_charlenplus","feature_avgwordlengplus","feature_numwordplus"]


    def get_uppercase_features(self, tweets,tweet_test=None):

        if tweet_test is None:
            feature  = []

            for tweet in tweets:
                feature.append(len(re.findall(r"[A-Z]{1,}", tweet.text)))

            return csr_matrix(np.vstack(feature)),["feature_uppercase"]

        else:
            feature  = []
            feature_test  = []

            for tweet in tweets:
                feature.append(len(re.findall(r"[A-Z]{1,}", tweet.text)))

            for tweet in tweet_test:
                feature_test.append(len(re.findall(r"[A-Z]{1,}", tweet.text)))


            return csr_matrix(np.vstack(feature)),csr_matrix(np.vstack(feature_test)),["feature_uppercase"]

    def get_language(self, tweets,tweet_test=None):
        languages=["en","fr","ca","es","it"]
        if tweet_test is None:
            feature  = []

            for tweet in tweets:
                index_of_language=languages.index(tweet.language)
                current_feature=np.zeros(len(languages))
                current_feature[index_of_language]=1
                feature.append(current_feature)

            return csr_matrix(np.vstack(feature)),languages

        else:
            feature  = []
            feature_test  = []

            for tweet in tweets:
                index_of_language=languages.index(tweet.language)
                current_feature=np.zeros(len(languages))
                current_feature[index_of_language]=1
                feature.append(current_feature)

            for tweet in tweet_test:
                index_of_language=languages.index(tweet.language)
                current_feature=np.zeros(len(languages))
                current_feature[index_of_language]=1
                feature_test.append(current_feature)


            return csr_matrix(np.vstack(feature)),csr_matrix(np.vstack(feature_test)),languages

    def get_sentimen_AFINN(self, tweets,tweet_test=None):

        if tweet_test is None:
            feature  = []

            for tweet in tweets:
                feature.append(tweet.sentimentAFINN)

            return csr_matrix(np.vstack(feature)),["feature_sentimentAFINN"]

        else:
            feature  = []
            feature_test  = []

            for tweet in tweets:
                feature.append(tweet.sentimentAFINN)

            for tweet in tweet_test:
                feature_test.append(tweet.sentimentAFINN)


            return csr_matrix(np.vstack(feature)),csr_matrix(np.vstack(feature_test)),["sentimentAFINN"]


    def get_sentimen_LIWC(self, tweets,tweet_test=None):

        if tweet_test is None:
            feature  = []

            for tweet in tweets:
                feature.append(tweet.sentimentLIWC)

            return csr_matrix(np.vstack(feature)),["feature_sentimentLIWC"]

        else:
            feature  = []
            feature_test  = []

            for tweet in tweets:
                feature.append(tweet.sentimentLIWC)

            for tweet in tweet_test:
                feature_test.append(tweet.sentimentLIWC)


            return csr_matrix(np.vstack(feature)),csr_matrix(np.vstack(feature_test)),["sentimentLIWC"]



    def get_sentimen_HL(self, tweets,tweet_test=None):

        if tweet_test is None:
            feature  = []

            for tweet in tweets:
                feature.append(tweet.sentimentHL)

            return csr_matrix(np.vstack(feature)),["feature_sentimentHL"]

        else:
            feature  = []
            feature_test  = []

            for tweet in tweets:
                feature.append(tweet.sentimentHL)

            for tweet in tweet_test:
                feature_test.append(tweet.sentimentHL)


            return csr_matrix(np.vstack(feature)),csr_matrix(np.vstack(feature_test)),["sentimentHL"]


    def get_sentimen_DAL(self, tweets,tweet_test=None):

        if tweet_test is None:
            feature  = []

            for tweet in tweets:
                feature.append(tweet.sentimentDAL)

            return csr_matrix(np.vstack(feature)),["feature_sentiment_dal_pleasantness", "feature_sentiment_dal_activation", "feature_sentiment_dal_imagery","feature_sentiment_dal_pleasantness_sum", "feature_sentiment_dal_activation_sum", "feature_sentiment_dal_imagery_sum"]

        else:
            feature  = []
            feature_test  = []

            for tweet in tweets:
                feature.append(tweet.sentimentDAL)

            for tweet in tweet_test:
                feature_test.append(tweet.sentimentDAL)


            return csr_matrix(np.vstack(feature)),csr_matrix(np.vstack(feature_test)),["feature_sentiment_dal_pleasantness", "feature_sentiment_dal_activation", "feature_sentiment_dal_imagery","feature_sentiment_dal_pleasantness_sum", "feature_sentiment_dal_activation_sum", "feature_sentiment_dal_imagery_sum"]


    def get_targetrelation_feature(self, tweets,tweet_test=None):


        tfidfVectorizer = CountVectorizer(ngram_range=(1,1),
                                          binary=False,
                                          max_features=500000)





        if tweet_test is None:
            feature  = []

            for tweet in tweets:
                feature.append(tweet.targetRelations)

            tfidfVectorizer = tfidfVectorizer.fit(feature)

            X = tfidfVectorizer.transform(feature)

            feature_names=tfidfVectorizer.get_feature_names()

            return X,feature_names

        else:
            feature  = []
            feature_test  = []

            for tweet in tweets:
                feature.append(tweet.targetRelations)

            for tweet in tweet_test:
                feature_test.append(tweet.targetRelations)


            tfidfVectorizer = tfidfVectorizer.fit(feature)

            X_train = tfidfVectorizer.transform(feature)
            X_test = tfidfVectorizer.transform(feature_test)

            feature_names=tfidfVectorizer.get_feature_names()

            return X_train, X_test, feature_names

#inizializer


def make_feature_manager():

    features_manager = Features_manager()

    return features_manager

