#!/usr/bin/env python
# coding: utf-8

# In[1]:


from TS import *
from GPTS import *
import numpy as np


class GPTS_TS(Learning_Agent):
    def __init__(self, arms):
        self.probabilities={10:0.4,15:0.6,20:0.3,25:0.2,30:0.1}
        super().__init__(arms)
        self.gpts_clicks = GPTS(arms,1)
        self.gpts_cost = GPTS(arms,2)
        self.ts_conv=TS([10,15,20,25,30])

    def update(self,pulled_price ,  pulled_bid, reward):
    

        self.gpts_clicks.update(pulled_bid, reward[1])
        self.gpts_cost.update(pulled_bid, reward[2])
        self.ts_conv.update(pulled_price , reward)

    def pull_arm(self):
        
        pricing=self.ts_conv.pull_arm()
        
        price=pricing[0]
        
        conv=pricing[1]


        n_clicks = np.random.normal(self.gpts_clicks.estimated_curve , self.gpts_clicks.sigmas)
        cum_cost = np.random.normal(self.gpts_cost.estimated_curve , self.gpts_cost.sigmas)
    
        sample_reward =price * n_clicks*conv - cum_cost

        return [price , self.arms[np.random.choice(np.where(sample_reward == sample_reward.max())[0])]]
    
    def update_tot(self,reward):
        
        self.gpts_clicks.update(reward[1] , reward[3])
        self.gpts_cost.update(reward[1], reward[4])
        self.ts_conv.update_tot(reward[0], reward[2] , reward[3])

# In[ ]:




