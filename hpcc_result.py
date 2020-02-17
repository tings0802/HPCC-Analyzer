#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

openFileName = '10000N_4proc_4NB'
with open(openFileName, 'r') as ifile:
    filename = ifile.name
    raw = ifile.readlines()

startLine = 'Begin of Summary section.'
endLine = 'End of Summary section.'
startLinePos = 0
endLinePos = 0

while startLine not in raw[startLinePos]:
    startLinePos += 1
#startLinePos += 1

while endLine not in raw[endLinePos]:
    endLinePos += 1
#endLinePos -= 1

result = {}
for i in range(startLinePos+1,endLinePos):
    res = raw[i].split('=')
    res[1] = res[1].strip()
    result[res[0]] = res[1]

resultTitle = ['HPL_N', 'HPL_NB',
               'HPL_Tflops',
               'PTRANS_GBs', 
               'MPIRandomAccess_GUPs', 
               'MPIFFT_Gflops',  
               'StarSTREAM_Triad', 
               'StarDGEMM_Gflops', 
               'RandomlyOrderedRingBandwidth_GBytes', 
               'RandomlyOrderedRingLatency_usec']
resultData = []
for i in resultTitle:
    resultData.append(result[i])
df = pd.DataFrame(np.array([resultData]), columns = resultTitle)

df.to_excel('result.xlsx', sheet_name='Sheet1', index=False)