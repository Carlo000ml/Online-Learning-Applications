#!/usr/bin/env python
# coding: utf-8

# In[1]:


from TS import *
from GPUCB import *
import numpy as np


class GPUCB1_TS(Learning_Agent):
    
    def __init__(self, arms):
        self.probabilities={10:0.4,15:0.6,20:0.3,25:0.2,30:0.1}
        super().__init__(arms)
        self.gpucb_clicks = GPUCB(arms)
        self.gpucb_cost = GPUCB(arms)
        self.ts_conv=TS([10,15,20,25,30])

    def update(self,pulled_arm_price, pulled_arm_bid, reward):
    
        self.gpucb_clicks.update(pulled_arm_bid, reward[1])
        self.gpucb_cost.update(pulled_arm_bid, reward[2])
        self.ts_conv.update(pulled_arm_price , [reward[0] , reward[1]])

    def pull_arm(self):
        
        pricing=self.ts_conv.pull_arm()
        
        price=pricing[0]
        
        conv=pricing[1]

        n_clicks = self.gpucb_clicks.estimated_curve + self.gpucb_clicks.confidence
        cum_cost = self.gpucb_cost.estimated_curve - self.gpucb_cost.confidence
    
        sample_reward =price * n_clicks*conv - cum_cost
        sample_reward=turn_nan(sample_reward)


        return [price , self.arms[np.random.choice(np.where(sample_reward == sample_reward.max())[0])]]
    

def turn_nan(arr):
        for i in range(arr.shape[0]):
            if np.isnan(arr[i]):
                arr[i]=np.inf
                
        return arr
                

# In[ ]:




