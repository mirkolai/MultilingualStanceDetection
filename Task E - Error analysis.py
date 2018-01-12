from sklearn.linear_model.logistic import LogisticRegression

__author__ = 'mirko'
import Features_manager
import Database_manager
from itertools import combinations
from sklearn.metrics.classification import precision_recall_fscore_support, accuracy_score
from sklearn.naive_bayes import GaussianNB, MultinomialNB
import numpy
from collections import Counter
from sklearn.svm.classes import SVC
import copy



print("Task Error  Analisis ")


database_manager=Database_manager.make_database_manager()
feature_manager=Features_manager.make_feature_manager()

training=[
    numpy.array(database_manager.return_tweets("en","clinton","Training")),
    numpy.array(database_manager.return_tweets("en","clinton","Training")),
    numpy.array(database_manager.return_tweets("fr","macron","Training")),
    numpy.array(database_manager.return_tweets("fr","macron","Training")),
    numpy.array(database_manager.return_tweets("it","referendum","Training")),
    numpy.array(database_manager.return_tweets("es","indipendencia","Training")+database_manager.return_tweets("ca","indipendencia","Training")),
    numpy.array(database_manager.return_tweets("es","indipendencia","Training")+database_manager.return_tweets("ca","indipendencia","Training")),
]


test=[
    numpy.array(database_manager.return_tweets("en","clinton","test")),
    numpy.array(database_manager.return_tweets("en","trump","test")),
    numpy.array(database_manager.return_tweets("fr","macron","test")),
    numpy.array(database_manager.return_tweets("fr","lepen","test")),
    numpy.array(database_manager.return_tweets("it","referendum","test")),
    numpy.array(database_manager.return_tweets("ca","indipendencia","test")),
    numpy.array(database_manager.return_tweets("es","indipendencia","test")),
]

label=[
    "en clinton test",
    "en trump test",
    "fr macron test",
    "fr lepen test",
    "it referendum test",
    "ca indipendencia test",
    "es indipendencia test",
]


bestfeature=[
    ["BoW","BoP","BoL","BoC",
     #"hashtagplus","hashtag","mention","nummention","numhashtag","uppercase","punctuation","length",
     "afinn","dal","liwc","hl",
     "language","BoURL","targetrelation"],
    [#"BoW","BoP","BoL","BoC",
     "hashtagplus","hashtag","mention","nummention","numhashtag","uppercase","punctuation","length",
     "afinn","dal","liwc","hl",
     "language","BoURL","targetrelation"],
    ["BoW","BoP","BoL","BoC",
     "hashtagplus","hashtag","mention","nummention","numhashtag","uppercase","punctuation","length",
     #"afinn","dal","liwc","hl",
     #"language","BoURL","targetrelation"
     ],
    [#"BoW","BoP","BoL","BoC",
     #"hashtagplus","hashtag","mention","nummention","numhashtag","uppercase","punctuation","length",
     "afinn","dal","liwc","hl",
     "language","BoURL","targetrelation"
     ],
    ["BoW","BoP","BoL","BoC",
     "hashtagplus","hashtag","mention","nummention","numhashtag","uppercase","punctuation","length",
     #"afinn","dal","liwc","hl",
     #"language","BoURL","targetrelation"
     ],
    [#"BoW","BoP","BoL","BoC",
     "hashtagplus","hashtag","mention","nummention","numhashtag","uppercase","punctuation","length",
     "afinn","dal","liwc","hl",
     #"language","BoURL","targetrelation"
     ],
    ["BoW","BoP","BoL","BoC",
     "hashtagplus","hashtag","mention","nummention","numhashtag","uppercase","punctuation","length",
     "afinn","dal","liwc","hl",
     #"language","BoURL","targetrelation"
     ],
]



bestclf=[
    "SVM",
    "LR",
    "LR",
    "LR",
    "LR",
    "LR",
    "SVM",
]

clfs = {
        #"NB" : GaussianNB(),
        "SVM": SVC(kernel="linear"),
        "LR" : LogisticRegression()
        }



for i in range(0,len(training)):

    key=bestclf[i]
    clf=clfs[bestclf[i]]
    feature_names=numpy.array([ bestfeature[i]])
    print(key,label[i],i)

    tweets_training=training[i]
    tweets_test=test[i]
    stance_training=numpy.array(feature_manager.get_stance(tweets_training))
    stance_test=numpy.array(feature_manager.get_stance(tweets_test))








    max=0
    for k in range(0,len(feature_names)):

            feature_filtered=feature_names[k]


            if key == "NB":
                current_clf=copy.copy(clf)
                X_train,X_test,feature_name_global,feature_index_global=feature_manager.create_feature_space(tweets_training,feature_filtered,tweets_test)

                size=1000
                length=len(tweets_training)
                #print(length)
                if length>size:
                    #print(round(length/size))
                    for j in range(0,round(length/size)):
                        #print(j)
                        if ((j+1)*size) < length:
                            current_training=X_train[(j*size):((j+1)*size),:]
                        else:
                            current_training=X_train[(j*size):,:]
                        current_clf.partial_fit(current_training.toarray(),numpy.array(stance_training[(j*size):((j+1)*size)]), classes=stance_training)

                else:
                    X_train,X_test,feature_name_global,feature_index_global=feature_manager.create_feature_space(tweets_training,feature_filtered,tweets_test)
                    current_clf.fit(X_train.toarray(),stance_training)

                test_predict=[]
                for index in range(0,len(stance_test)):
                    test_predict.append(current_clf.predict(X_test[i,:].toarray()))

            else:
                X_train,X_test,feature_name_global,feature_index_global=feature_manager.create_feature_space(tweets_training,feature_filtered,tweets_test)

                clf.fit(X_train,stance_training)

                test_predict = clf.predict(X_test)

            dic={}
            file = open("Task A "+key+" "+label[i]+" .csv","w")
            file.write( "tweet_id"+"\t"+
                        "text"+"\t"+
                        "stance"+"\t"+
                        "predict"+"\n")
            for i in range(0,len(tweets_test)):

                file.write( str(tweets_test[i].tweet_id)+"\t"+
                            tweets_test[i].text.replace("\t"," ").replace("\n"," ")+"\t"+
                            str(tweets_test[i].stance)+"\t"+
                            str(test_predict[i])+"\n")
                if str(tweets_test[i].stance)+str(test_predict[i]) in dic:
                    dic[str(tweets_test[i].stance)+str(test_predict[i])]+=1
                else:
                    dic[str(tweets_test[i].stance)+str(test_predict[i])]=1

            print(dic)
            file.close()
