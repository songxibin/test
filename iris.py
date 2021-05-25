import numpy as np

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


def load_data():
    # 共150条数据，训练120条，测试30条，进行2,8分进行模型训练
    # 每条数据类型为 x{nbarray} [6.4, 3.1, 5.5, 1.8]
    inputdata = datasets.load_iris()
    # 切分，测试训练2,8分
    x_train, x_test, y_train, y_test = \
        train_test_split(inputdata.data, inputdata.target, test_size = 0.2, random_state=0)
    return x_train, x_test, y_train, y_test


def main():
    # 训练集x ,测试集x,训练集label,测试集label
    x_train, x_test, y_train, y_test = load_data()
    # l2为正则项
    model = LogisticRegression(penalty='l2')
    model.fit(x_train, y_train)

    print("w: ", model.coef_)
    print("b: ", model.intercept_)
    # 准确率
    print("precision: ", model.score(x_test, y_test))
    print("MSE: ", np.mean((model.predict(x_test) - y_test) ** 2))
