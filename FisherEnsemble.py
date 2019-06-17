import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from mlens.visualization import corrmat
from sklearn.metrics import roc_curve
from sklearn.metrics import confusion_matrix
import seaborn as sns
import time

# Importing the dataset
df = pd.read_excel('survey - USSD among FIsher women - final.xlsx')
X = df[['age','Education','Average Per day sales','Operate SMS','Debit Card','Heard about USSD','Customer request for digital payment','Traning for Mobile Banking']]
y = df['Willingness to use Mobile Banking']

# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)


def get_models():
    """Generate a library of base learners."""
    nb = GaussianNB()
    svc = SVC(kernel='rbf')
    knn = KNeighborsClassifier(n_neighbors=3)
    lr = LogisticRegression(random_state=0)
    dt = DecisionTreeClassifier(criterion='entropy', random_state=0)
    models = {'svm': svc,
              'knn': knn,
              'naive bayes': nb,
              'decision tree': dt,
              'logistic': lr
              }
    return models


def train_predict(model_list):
    """Fit models in list on training set and return preds"""
    P = np.zeros((y_test.shape[0], len(model_list)))
    P = pd.DataFrame(P)
    print("Fitting models.")
    cols = list()
    for i, (name, m) in enumerate(model_list.items()):
        print("%s..." % name, end=" ", flush=False)
        m.fit(X_train, y_train)
        P.iloc[:, i] = m.predict(X_test)
        cm = confusion_matrix(y_test, P.iloc[:, i])
        print_confusion_matrix(cm, ['0', '1'])
        cols.append(name)
        print("done")
    P.columns = cols
    print("Done.\n")
    return P


def score_models(P, y):
    """Score model in prediction DF"""
    print("Scoring models.")
    for m in P.columns:
        score = roc_auc_score(y, P.loc[:, m])
        print("ROC-AUC score: %-26s: %.3f" % (m, score))
    print("Done.\n")


def print_confusion_matrix(confusion_matrix, class_names, figsize=(10, 7), fontsize=14):
    print("Confusion Matrix:")
    print(confusion_matrix)
    print("Accuracy: ", (confusion_matrix[0, 0] + confusion_matrix[1, 1]) / (np.sum(confusion_matrix)))
    print("Precision: ", (confusion_matrix[1, 1] / (confusion_matrix[0, 1] + confusion_matrix[1, 1])))
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


def count(df1):
    zeros = np.sum(df1 == 0)
    ones = np.sum(df1 == 1)
    if zeros > ones:
        df1['Stacked'] = 0
    else:
        df1['Stacked'] = 1
    return df1


start_time = time.time()

models = get_models()
P = train_predict(models)
score_models(P, y_test)

print("--- %s seconds ---" % (time.time() - start_time))

corrmat(P.corr(), inflate=False)
plt.show()
print("Ensemble ROC-AUC score: %.3f" % roc_auc_score(y_test, P.mean(axis=1)))


def plot_roc_curve(ytest, P_base_learners, P_ensemble, labels, ens_label):
    """Plot the roc curve for base learners and ensemble."""
    plt.figure(figsize=(10, 8))
    plt.plot([0, 1], [0, 1], 'k--')

    cm = [plt.cm.rainbow(i)
          for i in np.linspace(0, 1.0, P_base_learners.shape[1] + 1)]

    for i in range(P_base_learners.shape[1]):
        p = P_base_learners[:, i]
        fpr, tpr, _ = roc_curve(ytest, p)
        plt.plot(fpr, tpr, label=labels[i], c=cm[i + 1])

    fpr, tpr, _ = roc_curve(ytest, P_ensemble)
    plt.plot(fpr, tpr, label=ens_label, c=cm[0])

    plt.xlabel('False positive rate')
    plt.ylabel('True positive rate')
    plt.title('ROC curve')
    plt.legend(frameon=False)
    plt.show()


plot_roc_curve(y_test, P.values, P.mean(axis=1), list(P.columns), "ensemble")

P = P.apply(count, axis=1)
cm = confusion_matrix(y_test, P['Stacked'])
print("Confusion Matrix:")
print(cm)
print("Accuracy: ", (cm[0, 0] + cm[1, 1]) / (np.sum(cm)))
print("Precision: ", (cm[1, 1] / (cm[0, 1] + cm[1, 1])))
print_confusion_matrix(cm,  ['0', '1'])