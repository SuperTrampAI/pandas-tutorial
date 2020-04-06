# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 16:01
# @Author  : Marko Li 'lxh800109@gmail.com'
# @Site    : 
# @File    : BaseDemo.py
# @Software: PyCharm
# __create_data__=2020/3/30 16:01
# @Description: add Description
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def base_demo():
    # 创建包含1月1号在内的八天日期
    index = pd.date_range('1/1/2000', periods=8)
    # print(index)
    # 为index中的键赋值
    s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
    # print(s)
    # 为index对象中的每一个天赋值三个字
    df = pd.DataFrame(np.random.randn(8, 3), index=index,columns=['A', 'B', 'C'])
    # print(df)
    long_series = pd.Series(np.random.randn(1000))
    # print(long_series.head())# 查看前五个
    # print(long_series.tail(3))# 查看后三个
    # 列表的前两个
    # print(df[:2])
    # df.columns=[x.lower() for x in df.columns]
    # print(df)
    # print(s.array)
    # print(s.index.array)
    # 获得一个Numpy数组
    # print(s.to_numpy())





def main():
    base_demo()


if __name__ == '__main__':
    main()
