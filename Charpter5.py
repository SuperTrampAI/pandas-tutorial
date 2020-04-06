# -*- coding: utf-8 -*-
# @Time    : 2020/3/31 9:29
# @Author  : Marko Li 'lxh800109@gmail.com'
# @Site    : 
# @File    : Charpter5.py
# @Software: PyCharm
# __create_data__=2020/3/31 9:29
# @Description: add Description


import pandas as pd
import matplotlib.pyplot as plt


def base_demo():
    titanic = pd.read_csv("data/titanic.csv")
    air_quality = pd.read_csv("data/air_quality_long.csv", index_col='date.utc', parse_dates=True)
    # print(titanic.sort_values(by='Age').head())  # 对age进行排序
    # 按照登记和年龄进项排序
    # print(titanic.sort_values(by=['Pclass','Age'],ascending=False).head())
    # 使用NO2数据，按照地区分组，显示该地区的前两个数据
    no2 = air_quality[air_quality['parameter'] == 'no2']
    no2_subset = no2.sort_index().groupby(['location']).head(2)
    # print(no2_subset)
    # v这个不懂啥意思
    # print(no2_subset.pivot(columns='location', values='value'))
    # no2.pivot(columns='location',values='value').plot()
    # 把no2和pm2.5 显示在表格中
    # print(air_quality.pivot_table(values="value", index="location",columns="parameter", aggfunc="mean",margins=True))
    # plt.show()



def main():
    base_demo()


if __name__ == '__main__':
    main()
