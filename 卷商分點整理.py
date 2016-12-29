# -*- coding: utf-8 -*-
import pandas as pd

#--------------------------------------------------------
#讀取CSV File至DataFrame
#--------------------------------------------------------

filename = './/2330台積電.csv'
df = pd.read_csv( filename, sep = ',', encoding  = 'utf-8' )
#--------------------------------------------------------

#--------------------------------------------------------
#新增欄位-買進價格*股數
#新增欄位-賣出價格*股數
#--------------------------------------------------------

df[ '買進價格*股數' ] = df[ '買進股數' ] * df[ '價格' ]
df[ '賣出價格*股數' ] = df[ '賣出股數' ] * df[ '價格' ]
#--------------------------------------------------------

#--------------------------------------------------------
#依據券商群組分類
#--------------------------------------------------------

df = df.groupby( '券商' ).sum( )
#--------------------------------------------------------

#--------------------------------------------------------
#新增欄位-買賣超
#新增欄位-買進均價
#新增欄位-賣出均價
#--------------------------------------------------------

df[ '買賣超' ] =  df[ '買進股數' ] - df[ '賣出股數' ]
df[ '買進均價' ] = df[ '買進價格*股數'] / df[ '買進股數' ]
df[ '賣出均價' ] = df[ '賣出價格*股數'] / df[ '賣出股數' ]
#--------------------------------------------------------

#-------------------------------------------------------
#刪除序號欄位，axis = 1 代表x軸
#刪除價格欄位，axis = 1 代表x軸
#-------------------------------------------------------

df.drop( '價格', axis = 1, level = None, inplace = True )
df.drop( '序號', axis = 1, level = None, inplace = True )
#-------------------------------------------------------

df.to_csv( '卷商分點-2330台積電.csv', sep=',', line_terminator='\n' )