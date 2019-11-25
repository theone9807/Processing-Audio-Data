import os
import sys
import json
import pickle

with open('calls1.json', 'r') as f:
    d = json.loads(f.read())   
    f.close()   
#print(d)
    cr_data = d['c_recording']
    ar_data = d['our agent recording']
    cr_silence_timeslab = d['c silence timestamp']

agent = []
customer = []
q_a_dict = {}
##to itterate throung customer time slab

j = 0

for r in cr_data:
    for l in cr_silence_timeslab:
        
    
        #saperating questiona and answer
        #start = 0.0
        res = [[l[i], l[i+1]] for  i in range(len(l) -1)]
        res_customer = [res[i] for i in range(len(res)) if i%2 != 0]
        res_agent = [res[i] for i in range(len(res)) if i%2 == 0]

        for i in range(len(res_customer)):
            #save files to customer record
            start = float(res_customer[i][0][res_customer[i][0].index(' ') + 1:])
            end_ = float(res_customer[i][1][res_customer[i][1].index(' ') + 1:])

            try:
                
                os.system('ffmpeg -i cust_recording/'+r+' -ss '+str(start)+' -to '+str(end_)+'  -c copy customer_record3/'+str(j)+':'+str(start)+'-'+str(end_)+'.wav')
                customer.append(f'{str(j)}:{str(start)}-{str(end_)}.wav')
            except:
                customer.append('NaN')
    
            j += 1
            ##save files to agent record 

        for i in range(len(res_agent)):
            
            start_ = float(res_agent[i][0][res_agent[i][0].index(' ') + 1:])
            end_ = float(res_agent[i][1][res_agent[i][1].index(' ') + 1:])
            try:
            #try used to ignore list index error
                os.system('ffmpeg -i our_agent/'+r[:-6]+'out.wav -ss '+str(start_)+' -to '+str(end_)+'  -c copy agent_record3/'+str(j)+':'+str(start_)+'-'+str(end_)+'.wav')
                agent.append(f'{str(j)}:{str(start_)}-{str(end_)}.wav')
            except:
                agent.append('NaN')
          
            #start = end_
            #print('Start at end', start)
            j += 1
            #break
    #cr_data.remove(r)
    
   # break
   # sys.exit()
d1  = {}
d1['customer'] = customer
d1['agent'] = agent


with open('customer.txt', 'wb') as f:
     pickle.dump(customer, f)

with open('agent.txt', 'wb') as f2:
     pickle.dump(agent, f2)
#save as json
#import json

#with open('customer_agent.json', 'w') as f:
#     json.dump(d1, f)
#    break
  
      
