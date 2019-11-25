import pandas as pd
import numpy as np
import librosa
import os
import sys
import pickle
import json

def parser(data_dir, f):
   # function to load files and extract features
   file_name = os.path.join(data_dir, str(f))
   #print(file_name)
   
   try:
      # here kaiser_fast is a technique used for faster extraction
      X, sample_rate = librosa.load(file_name,res_type='kaiser_fast') 
      # we extract mfcc feature from data
      mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T,axis=0)
      print('Yes!!!!')
   except Exception as e:
      
      print("Error encountered while parsing file: ", f )
      return None
 
   feature = mfccs
   #label = f.Class
 
   return feature.tolist()

#temp = train.apply(parser, axis=1)
#temp.columns = ['feature', 'label']

d = pd.read_csv('q_a_dataset1.csv')
agent_array_list = []
for d1 in d['agent_audio']:
    
   agent_array_list.append(parser('agent_record3/',d1))


d = {'agent_audio_array': agent_array_list}
df = pd.DataFrame(d)
df.to_csv('agent_audio_array_csv1.csv', index= False)
#with open('agent_audio_array_json1.txt', 'wb') as f:
 #   pickle.dump(d, f)
