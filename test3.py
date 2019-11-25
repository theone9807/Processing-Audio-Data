import librosa
import random
import numpy as np
import pandas as pd
import pickle

d = pd.read_csv('q_a_dataset.csv')
#d

#create a function to convert audio into numpy array


#customer_array = []
#for d in d['customer']:
#    #print(d)
#    if d[d.index(':')+2:]!='0.0--0.208.wav':
#        try: 
#            data, sampling_rate = librosa.load('customer_record2/' + str(d.replace(' ', ''))
#            customer_array.append(data.tolist())
#        except:
#            continue
#    else:
#        customer_array.append('NaN')


agent_array = []
for d1 in d['agent']:
    #print(d
    if d1  != 'NaN':
     #   print(d1)   
        try: 
            X, sampling_rate = librosa.load('agent_record2/' + str(d1.replace(' ', '')), res_type='kaiser_fast')
            mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T,axis=0)
      #      print(data1)
            agent_array.append(mfccs)
        except:
            agent_array.append('NaN')
       #     print('NA')
            continue
    else:
        agent_array.append('NaN')



# d['agent_array'] = d.apply(lambda x: audio_array('agent_record2/', d.agent), axis = 1)
#print(customer_array)#create a function to convert audio into numpy array

#d = {'customer_array.append': customer_array, 'agent_array': agent_array}

#with open('customer_array.txt', 'wb') as f:
 #   pickle.dump(customer_array, f)
print(agent_array)
with open('agent_array.txt', 'wb') as f:
    pickle.dump(agent_array, f, protocol=2)
#d.to_csv('1.csv', index= False)
