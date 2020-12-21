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


# pandas.DataFrame.query(self, expr, inplace = False, **kwargs)
# expr：要评估的查询字符串；
# inplace=False：查询是应该修改数据还是返回修改后的副本
# kwargs：dict关键字参数
def l_query():
    values_1 = np.random.randint(10, size=10)
    values_2 = np.random.randint(10, size=10)
    years = np.arange(2010, 2020)
    groups = ['A', 'A', 'B', 'A', 'B', 'B', 'C', 'A', 'C', 'C']
    df = pd.DataFrame({'group': groups, 'year': years, 'value_1': values_1, 'value_2': values_2})
    print(df.query('value_1 < value_2'))
    df2=df.query('year >= 2016 ')
    print(df2)

# Dataframe.insert(loc, column, value, allow_duplicates=False)
# loc: int型，表示插入位置在第几列；若在第一列插入数据，则 loc=0
# column: 给插入的列取名，如 column='新的一列'
# value：新列的值，数字、array、series等都可以
# allow_duplicates: 是否允许列名重复，选择Ture表示允许新的列名与已存在的列名重复

def l_insert():
    values_1 = np.random.randint(10, size=10)
    values_2 = np.random.randint(10, size=10)
    years = np.arange(2010, 2020)
    groups = ['A', 'A', 'B', 'A', 'B', 'B', 'C', 'A', 'C', 'C']
    df = pd.DataFrame({'group': groups, 'year': years, 'value_1': values_1, 'value_2': values_2})
    print(df)
    new_col = np.random.randn(10)
    df.insert(2, 'new_col', new_col)
    print(df)
    return df

# DataFrame.cumsum(axis=None, skipna=True, args, kwargs)
# axis：index或者轴的名字
# skipna：排除NA/null值

def l_cumsum():
    df=l_insert()
    df['cumsum_2'] = df[['value_2', 'group']].groupby('group').cumsum()
    print(df)

# DataFrame.sample(n=None, frac=None, replace=False, weights=None, random_state=None, axis=None)
# n：要抽取的行数
# frac：抽取行的比例 例如frac=0.8，就是抽取其中80%
# replace：是否为有放回抽样， True:有放回抽样 False:未放回抽样
# weights：字符索引或概率数组
# random_state ：随机数发生器种子
# axis：选择抽取数据的行还是列 axis=0:抽取行 axis=1:抽取列

def l_sample():
    df=l_insert()
    sample1=df.sample(n=2,axis=1)
    sample2=df.sample(n=4)
    sample3=df.sample(frac=0.3)
    print(sample1)
    print(sample2)
    print(sample3)

# DataFrame.where(cond, other=nan, inplace=False, axis=None, level=None, errors='raise', try_cast=False, raise_on_error=None)
# cond：布尔条件，如果 cond 为真，保持原来的值，否则替换为other
# other：替换的特殊值
# inplace：inplace为真则在原数据上操作，为False则在原数据的copy上操作
# axis：行或列

def l_where():
    df=l_insert()
    df['value_1'].where(df['value_1'] > 5, 0, inplace=True)
    print(df)

# DataFrame.isin(values)
def l_isin():
    df=l_insert()
    years = ['2010', '2014', '2017']
    df=df[df.year.isin(years)]
    print(df)

def l_loc():
    df=l_insert()
    print(df.iloc[:2,:3])
    print(df.loc[:2,['group','year']])
    print(df.loc[[1,3,5],['year','value_1']])

# rank(axis=0, method: str = 'average', numeric_only: Union[bool, NoneType] = None, na_option: str = 'keep', ascending: bool = True, pct: bool = False)
# axis：行或者列
# method：返回名次的方式，可选{‘average’, ‘min’, ‘max’, ‘first’, ‘dense’}
# method=average 默认设置: 相同的值占据前两名，分不出谁是1谁是2，那么去中值即1.5，下面一名为第三名
# method=max: 两人并列第 2 名，下一个人是第 3 名
# method=min: 两人并列第 1 名，下一个人是第 3 名
# method=dense: 两人并列第1名，下一个人是第 2 名
# method=first: 相同值会按照其在序列中的相对位置定值
# ascending：正序和倒序
def l_rank():
    df=l_insert()
    df['rank_1'] = df['value_1'].rank(method='min')
    print(df)



if __name__=='__main__':
    # l_explode()
    # l_nunique()
    # l_replace()
    # l_query()
    # l_insert()
    # l_cumsum()
    # l_sample()
    # l_where()
    # l_isin()
    # l_loc()
    l_rank()
    pass



