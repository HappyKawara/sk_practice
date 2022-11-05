#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pprint
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.model_selection import KFold
import make_list
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier
from happymimi_voice_msgs.srv import StringToString
import rospy
import re
import csv_load
#from sklearn.linear_model import LinearRegression


class gender_judge():
    '''
    def __init__(self):
        bi_name = []
        name,gender = make_list.make_list()
        for n in name:
            li = make_list.bigram(n)
            bi_name.append(li + ["E" +li[-1]] + ["E" + li[-1][-1]])
        self.gender_list = [1 if i == "m" else 0 for i in gender]
        self.mlb = MultiLabelBinarizer()
        self.mlb.fit_transform(bi_name)
        self.mlb.classes_
        self.train_features = self.mlb.transform(bi_name)
        print("loading")
        self.classifier = XGBClassifier(objective='binary:logistic', n_estimators=300, learning_rate=0.2)
        print("xgboost")
        self.classifier.fit( self.train_features, self.gender_list )
    '''

    def main(self):
        #classifier = XGBClassifier(objective='binary:logistic', n_estimators=300, learning_rate=0.2)
        bi_male = []
        bi_female = []
        male,female = csv_load.main()
        print(male[:100:])
        for m in male:
            bi_male.append([m[i:i+2] for i in range(len(m) - 1)] + ["E" + m[-2] + m[-1]] + ["E" + m[-1]])
        for f in female:
                bi_female.append([f[i:i+2] for i in range(len(f) - 1)] + ["E" + m[-2] + m[-1]] + ["E" + m[-1]])
        train_features = bi_male + bi_female
        print(bi_male[:100:])
        t_test = [0 for i in range(len(male))] + [1 for i in range(len(female))]
        print(t_test)
        #test_features = self.mlb.transform(train_features)
        #classifier.fit(self.train_features,self.gender_list)
        #test_proba = classifier.predict(test_features)
        #print(test_proba)
        #con = 0
        #for i,pro in enumerate(test_proba):
        #    if pro == t_test[i]:
        #        con+=1
        #print(con/len(t_test))
        #for i in range(100):
        #    print()





if __name__ == '__main__':
    #rospy.init_node('gender_jg')
    a =gender_judge()
    a.main()
