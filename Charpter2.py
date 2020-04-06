# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 21:14
# @Author  : Marko Li 'lxh800109@gmail.com'
# @Site    : 
# @File    : Charpter2.py
# @Software: PyCharm
# __create_data__=2020/3/29 21:14
# @Description: add Description
import pandas as pd
import matplotlib.pyplot as plt


def air_quality():
    air_quality = pd.read_csv("air_quality_no2.csv", index_col=0, parse_dates=True)
    # air_quality.plot()
    # air_quality['station_paris'].plot() # 使用某一列绘制数据
    # air_quality.plot.scatter(x='station_london',y='station_paris',alpha=0.5) # alpha 设置透明度
    # 各类图的形状：area,bar,barh,box,density,hexbin,hist,kde,line,pie,scatter
    # air_quality.plot.box() # 适用于控制质量示例数据
    # air_quality.plot.area(figsize=(12,4),subplots=True)

    # 保存为图片
    # fig, axs = plt.subplots(figsize=(12, 4))
    # air_quality.plot.area(ax=axs)
    # axs.set_ylabel("NO_2$ concntration")
    # fig.savefig("no2_concentrations.png")
    plt.show()  # 在pycharm中显示图像


def main():
    air_quality()


if __name__ == '__main__':
    main()
