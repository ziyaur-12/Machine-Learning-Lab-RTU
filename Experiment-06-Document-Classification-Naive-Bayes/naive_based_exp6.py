import pandas as pd

# load dataset
msg = pd.read_csv('naivetext.csv', names=['message','label'])
print('The dimensions of the dataset', msg.shape)

# convert labels into numbers
msg['labelnum'] = msg.label.map({'pos':1, 'neg':0})

X = msg.message
y = msg.labelnum

print(X)
print(y)

# split dataset
from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(
    X, y, test_size=0.3, random_state=42
)

print('\n The total number of Training Data :', ytrain.shape)
print('\n The total number of Test Data :', ytest.shape)

# vectorization
from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()

xtrain_dtm = count_vect.fit_transform(xtrain)
xtest_dtm = count_vect.transform(xtest)

print('\n The words or Tokens in the text documents \n')
print(count_vect.get_feature_names_out())

# convert to dataframe
df = pd.DataFrame(
    xtrain_dtm.toarray(),
    columns=count_vect.get_feature_names_out()
)

# train model
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB()
clf.fit(xtrain_dtm, ytrain)

# prediction
predicted = clf.predict(xtest_dtm)

# evaluation
from sklearn import metrics

print('\n Accuracy of the classifier is',
      metrics.accuracy_score(ytest, predicted))

print('\n Confusion matrix')
print(metrics.confusion_matrix(ytest, predicted))

print('\n The value of Precision',
      metrics.precision_score(ytest, predicted))

print('\n The value of Recall',
      metrics.recall_score(ytest, predicted))

print("\nProgram finished successfully")