# -*- coding: utf-8 -*-
# @Time    : 2020/4/6 19:02
# @Author  : Marko Li 'lxh800109@gmail.com'
# @Site    : 
# @File    : Charpter8.py
# @Software: PyCharm
# __create_data__=2020/4/6 19:02
# @Description: 处理文本

import pandas as pd
import matplotlib.pyplot as plt


def base_demo():
    titanic = pd.read_csv("data/titanic.csv")
    # 全部传唤成小写字母
    #  print(titanic['Name'].str.lower())
    # 提取逗号前的部分，创建一个包含乘客姓氏的新列
    # print(titanic['Name'].str.split(','))
    # str.split() 将以逗号分隔的以列表形式返回
    # titanic['Surname']= titanic['Name'].str.split(',').str.get(0)
    # print(titanic['Surname'])
    # 找到数据中名字为Countess的数据
    print(titanic['Name'].str.contains('Countess'))
    print(titanic[titanic["Name"].str.contains('Countess')])
    # 名字最长的下标
    print(titanic['Name'].str.len().idxmax())
    print(titanic.loc[titanic['Name'].str.len().idxmax(),"Name"])
    # 把sex列中的男性替换成M，将所有女性替换成F
    titanic['Sex_short']=titanic['Sex'].replace({'male':'M',"female":"F"})
    print(titanic['Sex_short'])



def main():
    base_demo()


if __name__ == '__main__':
    main()



