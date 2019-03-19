# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 14:06:01 2018

@author: luowen
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import os
os.chdir('D:\\数据分析师前置课-微专业\\数据分析师（python）微专业前置课资料_运动员\\classdata\\')
#读取数据
df=pd.read_excel('奥运运动员数据.xlsx',sheetname=1)
data=df[['event','name','height','weight']]
#筛选数据，按照目标字段筛选,去掉运动员少于15人的项目,去掉缺失值
event_count=data['event'].value_counts()
data2=data[data['event']!='swim']
data2.dropna(inplace=True)

#计算BMI
data2['BMI']=data2['weight']/(data2['height']/100)**2
data2['BMI_range']=pd.cut(data2['BMI'],[0,18.5,24,28,50],labels=['Thin','Normal','Strong','ExtremelyStrong'])

#制图
plt.figure(figsize=(12,6))
sns.violinplot(x='event',y='BMI',data=data2,
               scale='count',palette='hls',
               inner='quartile')
sns.swarmplot(x='event',y='BMI',data=data2,color='w',alpha=0.8,s=2)
plt.grid(linestyle='--',alpha=0.5)
plt.title("athlete's BMI ")

