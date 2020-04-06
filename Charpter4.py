# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 16:19
# @Author  : Marko Li 'lxh800109@gmail.com'
# @Site    : 
# @File    : Charpter4.py
# @Software: PyCharm
# __create_data__=2020/3/30 16:19
# @Description: add Description
import pandas as pd
import matplotlib.pyplot as plt


def base_demo():
    titanic = pd.read_csv("data/titanic.csv")
    # age这一列的平均值
    # age_mean = titanic['Age'].mean()
    # 年龄和票价的中位数
    # age_fare_median=titanic[["Age","Fare"]].median()
    # 为多个列统计算汇总统计信息
    # age_fare_describe=titanic[["Age", "Fare"]].describe()
    # 使用agg方法自定义总计的组合
    # age_fare_describe = titanic.agg({
    #     'Age': ['min', 'max', 'median', 'skew'],
    #     'Fare': ['min', 'max', 'median', 'mean']
    # })
    # print(age_fare_describe.head())
    # 男性和女性的平均年龄是多少,如果不指定列，mean方法将包含值类型是数字的每一列
    # groupby_sex_mean = titanic[['Sex','Age']].groupby("Sex").mean()
    # print(groupby_sex_mean)
    # 按照性别和座位级别的平均票价
    # groupby_sex_pclass_and_fare_mean=titanic.groupby(["Sex","Pclass"])["Fare"].mean()
    # print(groupby_sex_pclass_and_fare_mean)
    # 每个座位的乘客人数
    # 如下value_counts 等同于titanic.groupby("Pclass")["Pclass"].count()
    pclass_value_counts=titanic["Pclass"].value_counts()
    print(pclass_value_counts)


def main():
    base_demo()


if __name__ == '__main__':
    main()
