#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Learning_Agent import Learning_Agent
import numpy as np
from GP_ts_1 import *
from GP_ts_2 import *
class GPTS(Learning_Agent):
    def __init__(self, arms ,label):
        super().__init__(arms)
        self.estimated_curve = np.zeros(self.n_arms)
        self.sigmas = np.ones(self.n_arms)*10000
        alpha = 100
        if label==1:self.gp = GP_ts_1(alpha,arms)
        if label==2:self.gp = GP_ts_2(alpha,arms)
        


    def update(self, pulled_arm, reward):
        self.collect_reward(pulled_arm,reward)
        
        self.gp.new_datum(pulled_arm,reward)
        estimation = self.gp.estimate_curve()
        self.estimated_curve= estimation[0]
        self.sigmas =estimation[1]
        self.sigmas=self.sigmas  # np.maximum
    

    def pull_arm(self):
        sampled_values = np.random.normal(self.means, self.sigmas)
        return self.arms[np.argmax(sampled_values)]

