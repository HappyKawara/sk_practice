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
import rospy

#from sklearn.linear_model import LinearRegression


class gender_judge():
    def __init__(self):
        self.bi_name = []
        name,gender = make_list.make_list()
        for n in name:
            li = make_list.bigram(n)
            self.bi_name.append(li + ["E" +li[-1]] + ["E" + li[-1][-1]])
        #pprint.pprint(bi_name)
        self.gender_list = [1 if i == "m" else 0 for i in gender]
        #print(self.gender_list)

        self.mlb = MultiLabelBinarizer()
        self.mlb.fit_transform(self.bi_name)
        self.mlb.classes_
        #pprint.pprint(self.bi_name)
        x_train, self.x_test, self.t_train, self.t_test = train_test_split(self.bi_name, self.gender_list, test_size=0.3, random_state=0)
        self.train_features = self.mlb.transform(x_train)
        self.test_features = self.mlb.transform(self.x_test)
        print("loading")

    def sv(self):
        classifier = svm.SVC(probability=True, C=0.1)
        print("sv")
        classifier.fit( self.train_features, self.t_train )
        test_proba = classifier.predict(self.test_features)
        print(test_proba)
        con = 0
        for i,pro in enumerate(test_proba):
            if pro == self.t_test[i]:
                con+=1
            #else:
            #    print(,self.t_test[i])
        print(con/len(self.t_test))
        #print(reg_model.score(x_train, t_train))
        return None

    def logistic_regression(self):
        classifier = LogisticRegression(C=1.0, penalty='l2')
        print("logistic_regression")
        classifier.fit( self.train_features, self.t_train )
        test_proba = classifier.predict(self.test_features)
        print(test_proba)
        con = 0
        for i,pro in enumerate(test_proba):
            if pro == self.t_test[i]:
                con+=1
        print(con/len(self.t_test))

    def xgboost(self):
        classifier = XGBClassifier(objective='binary:logistic', n_estimators=300, learning_rate=0.2)
        print("xboost")
        classifier.fit( self.train_features, self.t_train )
        test_proba = classifier.predict(self.test_features)
        print(test_proba)
        con = 0
        for i,pro in enumerate(test_proba):
            if pro == self.t_test[i]:
                con+=1
        print(con/len(self.t_test))

    def main(self):
        gender_judge().sv()
        gender_judge().logistic_regression()
        gender_judge().xgboost()

if __name__ == '__main__':
    gender_judge().main()
