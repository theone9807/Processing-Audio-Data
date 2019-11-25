#from os import listdir
import pickle
import pandas as pd
import json
#
##with open('agent.txt', 'rb') as f:
##    d = pickle.load(f)
#
##print(len(d))
#
##
#with open('customer.txt', 'rb') as f:
#    d1 = pickle.load(f)
#
##print(len(d1))
##print(len(d1))
##
##customer = listdir('customer_record1')
##agent = listdir('agent_record1')
##d=  {'customer': customer, 'agent': agent}
##
##with open('q_a_dataset1.json', 'w') as f:
##    json.dump(d, f)
##
##
#d = { 'customer_audio': d1[:14570]}
#df = pd.DataFrame(d)
#df.to_csv('customer_audio_dataset.csv', index = False)
data1 = pd.read_csv('customer_audio_array_csv1.csv')
# data2 = pd.read_csv('agent_audio_dataset.csv')
data2 = pd.read_csv('customer_audio_dataset.csv')
data3 = pd.read_csv('agent_audio_array_csv1.csv')
data4 = pd.read_csv('agent_audio_dataset.csv')
data = pd.concat([data1, data2, data3, data4], axis=1)
data.to_csv('final_dataset.csv', index = False)
