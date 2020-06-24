import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt


def read_data():
    return pd.read_csv("F:\\MedEI\\Datasets\\WisconsonBreastCancer\\data.csv")


columns = []



def plain_testing():
    df = read_data()
    df.drop(['id', 'Unnamed: 32'], axis=1, inplace=True)
    X, y = df.drop('diagnosis', axis=1), df['diagnosis']
    columns = X.columns
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=12)
    construct_model(x_train, x_test, y_train, y_test)


def model_with_min_max_scaling():
    """
    Returns the same exact model as plain_testing method
    """
    df = read_data()
    df.drop(['id', 'Unnamed: 32'], axis=1, inplace=True)
    X, y = df.drop('diagnosis', axis=1), df['diagnosis']
    columns.extend(X.columns)
    min_max_scaler = MinMaxScaler()
    X = min_max_scaler.fit_transform(X)
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=12)
    construct_model(x_train, x_test, y_train, y_test)


def construct_model(x_train, x_test, y_train, y_test):
    classifier = DecisionTreeClassifier(random_state=0)
    classifier.fit(x_train, y_train)

    print("Accuracy:", classifier.score(x_test, y_test))
    print("Confusion Matrix:\n", confusion_matrix(y_test, classifier.predict(x_test)))

    # Plot the model
    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(8, 8), dpi=500)
    plot_tree(classifier, feature_names=columns, class_names=['M', 'B'])
    fig.savefig('classifier_visualization.png')


model_with_min_max_scaling()
