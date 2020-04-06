# -*- coding: utf-8 -*-
# @Time    : 2020/4/1 22:59
# @Author  : Marko Li 'lxh800109@gmail.com'
# @Site    : 
# @File    : Charpter7.py
# @Software: PyCharm
# __create_data__=2020/4/1 22:59
# @Description: add Description
import pandas as pd
import matplotlib.pyplot as plt


def base_demo():
    air_quality = pd.read_csv("data/air_quality_no2_long.csv")
    # 列名重命名显示
    air_quality = air_quality.rename(columns={"date.utc": "datetime"})
    # print(air_quality.head())
    # 把文本列转换成时间类型
    air_quality['datetime']=pd.to_datetime(air_quality['datetime'])
    # print(air_quality['datetime'])
    # print(air_quality['datetime'].min()) # 最小时间
    # print(air_quality['datetime'].max())# 最大时间
    # 往几何中添加月份列
    # air_quality['month']=air_quality['datetime'].dt.month
    # print(air_quality.head())
    # 以每个测量位置作为单独的列
    no_2=air_quality.pivot(index='datetime',columns='location',values='value')
    print(no_2.head())



def main():
    base_demo()


if __name__ == '__main__':
    main()
