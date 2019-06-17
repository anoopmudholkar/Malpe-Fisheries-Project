import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

# load data
censusdatachi = pd.read_excel('survey - USSD among FIsher women - final.xlsx')
X = censusdatachi[['age','District','Market Place','Education','Average Per day sales','Bank Acct','Bank Name','Phone Type','Operate SMS','Aadhar Card','Debit Card','Mobile banking Services','Heard about USSD','Customer request for digital payment','Traning for Mobile Banking']]
Y = censusdatachi['Willingness to use Mobile Banking']
# feature extraction
test = SelectKBest(score_func=chi2, k='all')
fit = test.fit(X, Y)
print(fit.scores_)

factors = ('age','District','Market Place','Education','Average Per day sales','Bank Acct','Bank Name','Phone Type','Operate SMS','Aadhar Card','Debit Card','Mobile banking Services','Heard about USSD','Customer request for digital payment','Traning for Mobile Banking')
ypos = np.arange(len(factors))
score = fit.scores_
plt.barh(ypos,score,align='center',alpha=0.5)
plt.yticks(ypos,factors)
plt.ylabel('influencing factors')
plt.xlabel('test scores')
plt.title('Chi square test')

plt.show()
