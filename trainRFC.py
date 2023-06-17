import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import pandas as pd


url = r"SwedishCWItrainingDataset.csv"
df = pd.read_csv(url, encoding="Latin-1", delimiter=",")

print(df.head())

# Loads the dataset and splits it into training and testing sets
#df = pd.read_csv(url, header = 0, encoding='UTF-8')
X = df.drop('Difficulty', 1)
#X = X.values
Y = df['Difficulty']
#Y = Y.values
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.1, random_state=0)

# Initialises Random Forest classifier object
regressor = RandomForestClassifier(n_estimators=250, min_samples_split = 3, min_samples_leaf = 2)



def train_model():
    '''Trains and tests the benchmark model trained on 4 features'''
    X_train_baseline = X_train.filter(['Frequency_SUC', 'Length', "FreqBlog", "FreqTwitter"], axis=1).values
    X_test_baseline = X_test.filter(['Frequency_SUC', 'Length', "FreqBlog", "FreqTwitter"], axis=1).values
    regressor.fit(X_train_baseline, y_train)
    y_pred = regressor.predict(X_test_baseline)
    return y_pred


def model_classification_report(y_test, y_pred):
    '''Evaluated the model in terms of F1 score, accuracy, recall and precision'''
    return classification_report(y_test, y_pred)


def model_accuracy(y_test, y_pred):
    '''Returns accuracy score only'''
    result = 'Accuracy score: ' + str(accuracy_score(y_test, y_pred))
    return result


if __name__ == "__main__":
    print('\nFrequency model results (trained on 4 features):')
    y_pred = train_model()
    print(model_classification_report(y_test, y_pred))
    print(model_accuracy(y_test, y_pred))

    #saves the model as a joblib-file for reusing
    joblib.dump(regressor, "./SwedishCWI_RFC.joblib")

    
