# -*- coding: utf-8 -*-
# @Time    : 2020/3/31 10:07
# @Author  : Marko Li 'lxh800109@gmail.com'
# @Site    : 
# @File    : Charpter6.py
# @Software: PyCharm
# __create_data__=2020/3/31 10:07
# @Description: add Description


import pandas as pd
import matplotlib.pyplot as plt


def base_demo():
    air_quality_no2 = pd.read_csv("data/air_quality_no2_long.csv", parse_dates=True)
    air_quality_no2 = air_quality_no2[["date.utc", "location","parameter", "value"]]
    # print(air_quality_no2.head())

    air_quality_pm25 = pd.read_csv("data/air_quality_pm25_long.csv",parse_dates=True)
    air_quality_pm25 = air_quality_pm25[["date.utc", "location","parameter", "value"]]
    # print(air_quality_pm25.head())

    air_quality=pd.concat([air_quality_pm25,air_quality_no2],axis=0)
    # print(air_quality.head())
    # 按照时间排序，输出两个表中时间升序排序
    air_quality=air_quality.sort_values("date.utc")
    # print(air_quality.head())
    #
    air_quality_=pd.concat([air_quality_pm25,air_quality_no2],
                           keys=['PM25','NO2'])
    # print(air_quality_.head())
    stations_coord=pd.read_csv('data/air_quality_stations.csv')
    # print(stations_coord.head())
    # 把两个表中的数据,放在一起显示.两个表都有一个location,该列作为组合信息的键.
    # 只想左表中的才会最终出现在结果表中.类似于数据库的左链接查询
    air_quality=pd.merge(air_quality,stations_coord,how='left',on='location')
    # print(air_quality.head())


def main():
    base_demo()


if __name__ == '__main__':
    main()
