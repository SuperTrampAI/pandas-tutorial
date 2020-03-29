# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 19:23
# @Author  : Marko Li 'lxh800109@gmail.com'
# @Site    : 
# @File    : Chapters.py
# @Software: PyCharm
# __create_data__=2020/3/29 19:23
# @Description: add Description


import pandas as pd


def pandas_print():
    df = pd.DataFrame({
        "Name": ["braund22", "Allen22", "Bonnell22"],
        "Age": [23, 34, 45],
        "Sex": ['male', 'male', 'female'],
    })
    df.to_excel("excel.xlsx", sheet_name='passengers', index=False)  # 该函数会替换到原来的数据
    print(df)


def read_excel():
    # pandas 读取文件，支持csv，excel，sql，json，parquet等，读取的方法就是使用：read_*() 使用前缀read...
    titanic = pd.read_excel("excel.xlsx", sheet_name='passengers')  # sheet_name 设置读取的哪一个sheet
    # print(titanic.head(3))  # 使用head限制返回的行数
    # print(titanic.tail(3))  # 查看倒数三行
    # print(titanic.dtypes) # 查看数据的类型

    info = titanic.info()
    ages = titanic['Age']  # 获取特别列的数据
    age_sex = titanic[['Age', 'Sex']]  # 返回多列
    above = titanic[titanic["Age"] > 35]  # 筛选 年龄在35岁以上的
    in_name = titanic[titanic["Name"].isin(['braund22', 'Bonnell22'])]  # isin 等同于如下方法
    # class_23 = titanic[(titanic["Name"] == "braund22") | (titanic["Name"] == "Bonnell22")]
    # age_no_na = titanic[titanic["Age"].notna()] Age这一列不为空的数据

    # 筛选年龄在35岁以上的名字
    adult_names = titanic.loc[titanic["Age"] > 35, "Name"]
    titanic.iloc[9:25,2:5] # 10~25行，3~5列
    # titanic.iloc[0:3, 3] = "anonymous"  把值赋值给第三列的前三行


def main():
    pandas_print()
    print("-------------------------")
    read_excel()


if __name__ == '__main__':
    main()
