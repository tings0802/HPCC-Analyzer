#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

path = '..\\hpcc_results\\'
filelist = os.listdir(path)

resultTitle = ['HPL_N',
               'HPL_NB',
               'HPL_Tflops',
               'PTRANS_GBs', 
               'MPIRandomAccess_GUPs', 
               'MPIFFT_Gflops',  
               'StarSTREAM_Triad', 
               'StarDGEMM_Gflops', 
               'RandomlyOrderedRingBandwidth_GBytes', 
               'RandomlyOrderedRingLatency_usec']

allData = pd.DataFrame(columns = resultTitle)

for file in filelist:
    with open(path + file, 'r') as ifile:
        raw = ifile.readlines()

    startLine = 'Begin of Summary section.'
    endLine = 'End of Summary section.'
    startLinePos = 0
    endLinePos = 0

    while startLine not in raw[startLinePos]:
        startLinePos += 1

    while endLine not in raw[endLinePos]:
        endLinePos += 1

    result = {}
    for i in range(startLinePos + 1, endLinePos):
        res = raw[i].split('=')
        res[1] = res[1].strip()
        result[res[0]] = res[1]
    
    resultData = []
    for i in resultTitle:
        resultData.append(result[i])
    df = pd.DataFrame(np.array([resultData]), columns = resultTitle)
    
    allData = allData.append(df, ignore_index=True)

for col in resultTitle[0:2]:
    allData[col] = allData[col].astype(int)
for col in resultTitle[2:]:
    allData[col] = allData[col].astype(float)
allData.dtypes

allData.to_excel('result.xlsx', sheet_name='Sheet1', index=False)

