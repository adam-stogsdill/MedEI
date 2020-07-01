import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import seaborn as sns


def read_data():
    return pd.read_csv("F:\\MedEI\\Datasets\\WisconsonBreastCancer\\data.csv")


columns = []


def plain_testing():
    df = read_data()
    df.drop(['id', 'Unnamed: 32'], axis=1, inplace=True)
    X, y = df.drop('diagnosis', axis=1), df['diagnosis']
    columns.extend(X.columns)
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

    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=12)
    construct_model(x_train, x_test, y_train, y_test)


def construct_model(x_train, x_test, y_train, y_test):
    classifier = DecisionTreeClassifier(random_state=0)
    classifier.fit(x_train, y_train)


    cm = confusion_matrix(y_test, classifier.predict(x_test))
    tp, fp, fn, tn = cm[0][0], cm[0][1], cm[1][0], cm[1][1]
    print("Confusion Matrix:\n", cm)
    precision, recall = tp / (tp + fp), tp / (tp + fn)
    print("Accuracy:", classifier.score(x_test, y_test))
    print("Precision:", precision)
    print("Recall:", recall)
    print("F1 Score:", 2 * (recall * precision) / (recall + precision))


    # Plot the model
    '''fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(8, 8), dpi=500)
    plot_tree(classifier, feature_names=columns, class_names=['M', 'B'])
    fig.savefig('classifier_visualization.png')'''


def run_dataset_metrics():
    df = read_data()
    df.drop(['id', 'Unnamed: 32'], axis=1, inplace=True)
    X, y = df.drop('diagnosis', axis=1), df['diagnosis']
    columns.extend(X.columns)
    min_max_scaler = MinMaxScaler()
    X = min_max_scaler.fit_transform(X)

    percent_of_malignant = df[df['diagnosis'].str.match('M')].shape[0] / df.shape[0]
    percent_of_benign = df[df['diagnosis'].str.match('B')].shape[0] / df.shape[0]
    print("Percent of malignant:", percent_of_malignant * 100)
    print("Percent of benign:", percent_of_benign * 100)

    # plt.bar(['M', 'B'], [df[df['diagnosis'].str.match('M')].shape[0], df[df['diagnosis'].str.match('B')].shape[0]])
    # plt.savefig('class_distribution.png')
    print(X.shape,  len(columns))
    plt.figure(figsize=(10, 10))
    plt.boxplot(X, labels=columns, vert=True)
    plt.xticks(fontsize=12, rotation=90)
    plt.gcf().subplots_adjust(bottom=0.30)
    plt.savefig('data_distribution.png')


def correlation_plot():
    df = read_data()
    df.drop(['id', 'Unnamed: 32'], axis=1, inplace=True)
    X, y = df.drop('diagnosis', axis=1), df['diagnosis']
    columns.extend(X.columns)
    min_max_scaler = MinMaxScaler()
    X = min_max_scaler.fit_transform(X)

    plt.figure(figsize=(10, 10))
    ax = sns.heatmap(pd.DataFrame(X).corr(), xticklabels=columns, yticklabels=columns)
    plt.gcf().subplots_adjust(bottom=0.30)
    plt.gcf().subplots_adjust(left=0.30)
    plt.savefig('correlation_plot.png')
    plt.show()


correlation_plot()
