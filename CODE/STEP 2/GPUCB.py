#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Learning_Agent import Learning_Agent
import numpy as np
from GP_ucb_1 import *
from GP_ucb_2 import *
class GPUCB(Learning_Agent):
   
    def __init__(self,arms,label):
        super().__init__(arms)
        self.arms = arms
        self.confidence = np.array([np.inf] * self.n_arms)
        self.estimated_curve = np.zeros(self.n_arms)
        self.sigmas = np.ones(self.n_arms) * 100
        alpha = 100
        if label==1:self.gp = GP_ucb_1(alpha,arms)
        if label==2:self.gp = GP_ucb_2(alpha,arms)
        
        
    def  pull_arm(self):
        uppers=self.estimated_curve+self.confidence
        return self.arms[np.random.choice(np.where(upper_conf == upper_conf.max())[0])]
    
    def update(self , pulled_arm , reward):
        self.collect_reward(pulled_arm,reward)

        self.gp.new_datum(pulled_arm,reward)
        estimation = self.gp.estimate_curve()
        self.estimated_curve= estimation[0]
        self.sigmas =estimation[1]
        self.confidence = self.sigmas *5   # sigmas * sqrt(beta)  si trovano articoli a riguardo
        

