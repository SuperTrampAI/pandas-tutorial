# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 16:00
# @Author  : Marko Li 'lxh800109@gmail.com'
# @Site    : 
# @File    : Charpter3.py
# @Software: PyCharm
# __create_data__=2020/3/30 16:00
# @Description: add Description
import pandas as pd


def base_demo():
    air_quality = pd.read_csv("air_quality_no2.csv",index_col=0, parse_dates=True)
    air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882
    air_quality["ratio_paris_antwerp"] = \
        air_quality["station_paris"] / air_quality["station_antwerp"]
    # 给列重命名
    air_quality_renamed = air_quality.rename(columns={"station_antwerp": "BETR801","station_paris": "FR04014","station_london": "London Westminster"})
    # 将列明转换为小写
    air_quality_renamed = air_quality_renamed.rename(columns=str.lower)
    print(air_quality_renamed.head())


def main():
    base_demo()


if __name__ == '__main__':
    main()
