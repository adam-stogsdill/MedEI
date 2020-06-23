import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix


def read_data():
    return pd.read_csv("F:\\MedEI\\Datasets\\WisconsonBreastCancer\\data.csv")


def plain_testing():
    df = read_data()
    df.drop(['id', 'Unnamed: 32'], axis=1, inplace=True)
    X, y = df.drop('diagnosis', axis=1), df['diagnosis']

    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=12)

    classifier = DecisionTreeClassifier(random_state=0)
    classifier.fit(x_train, y_train)

    print("Accuracy:", classifier.score(x_test, y_test))
    print("Confusion Matrix:\n", confusion_matrix(y_test, classifier.predict(x_test)))


plain_testing()
