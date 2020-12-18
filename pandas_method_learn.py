#!/usr/bin/env python
# -*- coding: utf-8 -*-

# explode: 将一行数据展开成多行
# nunique: 去重计数
# replace: 替换df中的值，赋以新的值

import pandas as pd
import numpy as np


# DataFrame.explode(self, column: Union[str, Tuple])
def l_explode():
    id = ['a','b','c']
    measurement = [4,6,[2,3,8]]
    day = [1,1,1]
    df1 = pd.DataFrame({'id':id, 'measurement':measurement, 'day':day})
    print(df1)

    df2=df1.explode('measurement').reset_index(drop=True)
    print(df2)

# Series.nunique(dropna=True)
# # 或者
# DataFrame.nunique(axis=0, dropna=True)
# axis：int型，0代表行，1代表列，默认0；
# dropna：bool类型，默认为True，计数中不包括NaN；

def l_nunique():
    values_1 = np.random.randint(10, size=10)
    values_2 = np.random.randint(10, size=10)
    years = np.arange(2010, 2020)
    groups = ['A', 'A', 'B', 'A', 'B', 'B', 'C', 'A', 'C', 'C']
    df = pd.DataFrame({'group': groups, 'year': years, 'value_1': values_1, 'value_2': values_2})
    print(df)
    print(df.year.nunique())
    print(df.nunique())

# DataFrame.replace(to_replace=None,
#                   value=None,
#                   inplace=False,
#                   limit=None,
#                   regex=False,
#                   method='pad')

# to_replace：被替换的值
# value：替换后的值
# inplace：是否要改变原数据，False是不改变，True是改变，默认是False
# limit：控制填充次数
# regex：是否使用正则,False是不使用，True是使用，默认是False
# method：填充方式，pad,ffill,bfill分别是向前、向前、向后填充

def l_replace():
    values_1 = np.random.randint(10, size=10)
    values_2 = np.random.randint(10, size=10)
    years = np.arange(2010, 2020)
    groups = ['A', 'A', 'B', 'A', 'B', 'B', 'C', 'A', 'C', 'C']
    df = pd.DataFrame({'group': groups, 'year': years, 'value_1': values_1, 'value_2': values_2})
    print(df)
    df=df.replace('A', 'D')
    print(df)
    df=df.replace({'B': 'E', 'C': 'F'})
    print(df)


if __name__=='__main__':
    # l_explode()
    # l_nunique()
    l_replace()
    pass
