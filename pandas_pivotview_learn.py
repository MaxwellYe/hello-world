#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
data = pd.read_csv(r"C:\Users\maxwell.ye\seaborn-data\tips.csv")
# print(data.head())
result1 = pd.pivot_table(data,
                         index='day' ,
                         values = ['tip','total_bill'],
                         aggfunc = np.sum)
print(result1.head())


# pandas.pivot_table(*data*,
#                    *values=None*,
#                     *index=None*,
#                     *columns=None*, 
#                     *aggfunc='mean'*, 
#                     *fill_value=None*, 
#                     *margins=False*, 
#                     *dropna=True*, 
#                     *margins_name='All'*, 
#                     *observed=False*)

# data：dataframe格式数据
# values：需要汇总计算的列，可多选
# index：行分组键，一般是用于分组的列名或其他分组键，作为结果DataFrame的行索引
# columns：列分组键，一般是用于分组的列名或其他分组键，作为结果DataFrame的列索引
# aggfunc：聚合函数或函数列表，默认为平均值
# fill_value：设定缺失替换值
# margins：是否添加行列的总计
# dropna：默认为True，如果列的所有值都是NaN，将不作为计算列，False时，被保留
# margins_name：汇总行列的名称，默认为All
# observed：是否显示观测值
