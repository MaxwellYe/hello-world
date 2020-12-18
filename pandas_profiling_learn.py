#!/usr/bin/env python
# -*- coding: utf-8 -*-
import seaborn as sns
import pandas_profiling as pp
import pandas as pd
import matplotlib.pyplot as plt


data=sns.load_dataset('aftersales')
# data=data.head()
# download dataset from https://github.com/mwaskom/seaborn-data and put in folder C:\Users\maxwell.ye


report = pp.ProfileReport(data)
report.to_file('ppoutput.html')
