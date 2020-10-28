import pandas as pd
import nltk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
import os
from sklearn import metrics

class dmw_mini:
    vectorizer = None
    naive_bayes = None
    knn = None
    rf = None
    x_train = None
    x_train_transform = None
    y_train = None
    x_test = None
    x_test_transform = None
    y_test = None
    nbclf = None
    knnclf = None
    rfclf = None
    
    def __init__(self):
        data_dir = os.getcwd()
        print("Loading Train File ...", end = "\t\t\t")
        data = pd.read_csv(os.path.join(data_dir, "Train.csv"))
        self.x_train = data["text"]
        self.y_train = data["label"]
        print("Completed\nGenerating Transforms ...", end = "\t\t")
        self.vectorizer = TfidfVectorizer(stop_words = 'english')
        self.vectorizer.fit(self.x_train)
        self.x_train_transform = self.vectorizer.transform(self.x_train)
        print("Completed")
        self.naive_bayes = MultinomialNB()
        self.knn = KNeighborsClassifier(n_neighbors=171)
        self.rf = RandomForestClassifier(n_estimators=50, random_state=0)
        print("Training Naive Bayes ...", end = "\t\t")
        self.nbclf = self.naive_bayes.fit(self.x_train_transform, self.y_train)

        print("Completed\nTraining KNN ...", end = "\t\t\t")
        self.knnclf = self.knn.fit(self.x_train_transform, self.y_train)
        print("Completed\nTraining Random Forest ...", end = "\t\t")
        self.rfclf = self.rf.fit(self.x_train_transform, self.y_train)
        print("Completed\nLaunching GUI")
    
    def read_test_data_and_predict(self, filepath):
        data = pd.read_csv(filepath)
        self.x_test = data["text"]
        self.y_test = data["label"]
        self.x_test_transform = self.vectorizer.transform(self.x_test)
        predictions = []
        predictions.append(self.nbclf.predict(self.x_test_transform))
        predictions.append(self.knnclf.predict(self.x_test_transform))
        predictions.append(self.rfclf.predict(self.x_test_transform))
        accuracy = []
        accuracy.append(round(metrics.accuracy_score(self.y_test, predictions[0]) * 100, 4))
        accuracy.append(round(metrics.accuracy_score(self.y_test, predictions[1]) * 100, 4))
        accuracy.append(round(metrics.accuracy_score(self.y_test, predictions[2]) * 100, 4))
        confusionMat = []
        confusionMat.append(metrics.confusion_matrix(self.y_test, predictions[0]))
        confusionMat.append(metrics.confusion_matrix(self.y_test, predictions[1]))
        confusionMat.append(metrics.confusion_matrix(self.y_test, predictions[2]))
        print(accuracy)
        print(confusionMat)
        return accuracy, confusionMat
    
    def read_test_text_and_predict(self, text):
        temp = []
        temp.append(text)
        trans = self.vectorizer.transform(temp)
        predictions = []
        predictions.append(self.nbclf.predict(trans))
        predictions.append(self.knnclf.predict(trans))
        predictions.append(self.rfclf.predict(trans))
        print(predictions)
        return predictions        