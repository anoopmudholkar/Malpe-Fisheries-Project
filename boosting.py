# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import  seaborn as sns

# Importing the dataset
featured_data = pd.read_excel('survey - USSD among FIsher women - final.xlsx')

X = featured_data[['age','Education','Average Per day sales','Operate SMS','Debit Card','Heard about USSD','Customer request for digital payment','Traning for Mobile Banking']]
Y = featured_data['Willingness to use Mobile Banking']

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.25, random_state = 0)

# Fitting XGBoost to the Training set
from xgboost import XGBClassifier
classifier = XGBClassifier()
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

def print_confusion_matrix(confusion_matrix, class_names, figsize=(10, 7), fontsize=14):
    df_cm = pd.DataFrame(
        confusion_matrix, index=class_names, columns=class_names,
    )
    fig = plt.figure(figsize=figsize)
    try:
        heatmap = sns.heatmap(df_cm, annot=True, fmt="d")
    except ValueError:
        raise ValueError("Confusion matrix values must be integers.")
    heatmap.yaxis.set_ticklabels(heatmap.yaxis.get_ticklabels(), rotation=0, ha='right', fontsize=fontsize)
    heatmap.xaxis.set_ticklabels(heatmap.xaxis.get_ticklabels(), rotation=45, ha='right', fontsize=fontsize)
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()

print_confusion_matrix(cm, ['0', '1'])


print("Accuracy: ", (cm[0, 0] + cm[1, 1]) / (np.sum(cm)))
print("Precision: ", (cm[1, 1] / (cm[0, 1] + cm[1, 1])))