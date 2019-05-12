import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

train = pd.read_csv("train.csv")  # loading the train CSV file as the dataframe
X = train.drop(['label'], axis=1)  # creating the feature set
y = train['label']  # setting the target column
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.3, random_state=0)  # splitting the testing and training set
neu = MLPClassifier(max_iter=200)  # creating the model
neu.fit(train_X, train_y)  # fitting the model on the training set
y_neu = neu.predict(test_X)  # predicting the test set
print(neu.score(test_X, test_y))  # getting the score for the model

from sklearn.externals import joblib
joblib.dump(neu, 'MLP_model.pkl')  # dumping the model


