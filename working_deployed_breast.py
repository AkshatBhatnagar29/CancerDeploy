# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

import pickle
#loadin the model
loaded_model=pickle.load(open('C:/Users/admin/Desktop/deploy/traained_model.sav','rb'))
input_data=(19.69,21.25,130,1203,0.1096,0.1599,0.1974,0.1279,0.2069,0.05999,0.7456,0.7869,4.585,94.03,0.00615,0.04006,0.03832,0.02058,0.0225,0.004571,23.57,25.53,152.5,1709,0.1444,0.4245,0.4504,0.243,0.3613,0.08758)
inputdatatonumpy=np.asarray(input_data)
inputdatareshaped=inputdatatonumpy.reshape(1,-1)
prediction=loaded_model.predict(inputdatareshaped)
if(prediction):
    print('Benign')
else:
  print('Malignant')
print(prediction)