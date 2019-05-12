import pandas as pd
from sklearn.externals import joblib
import csv

csv_file = open('submit.csv', 'w', newline='')  # opening the CSV file, if file not found, it will create a new file
csv_write = csv.writer(csv_file)
csv_write.writerow(['ImageId', 'Label'])  # giving headers
model = joblib.load("MLP_model.pkl")  # loading the model created in Recognizer.py
test = pd.read_csv("test.csv")  # loading the test CSV file as the data frame
y_kaggle = model.predict(test)  # predicting the feature set given in test.csv

i=0
list=[]
for i in range(len(y_kaggle)):
    list = [i+1, y_kaggle[i]]  # creating the prescribed format
    csv_write.writerow(list)  # writing the prediction to the csv file
    i = i+1

csv_file.close()  # closing the file
