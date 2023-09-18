#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Learning_Agent import Learning_Agent
import numpy as np
from GP import GP
class GPTS(Learning_Agent):
    def __init__(self, arms):
        super().__init__(arms)
        self.estimated_curve = np.zeros(self.n_arms)
        self.sigmas = np.ones(self.n_arms)*50000
        alpha = 1000
        self.gp = GP(alpha,arms)


    def update(self, pulled_arm, reward):
        self.t+=1

        self.gp.new_datum(pulled_arm,reward)
        estimation = self.gp.estimate_curve()
        self.estimated_curve= estimation[0]
        self.sigmas =estimation[1]
        self.sigmas=np.maximum(self.sigmas, 100)
    

    def pull_arm(self):
        sampled_values = np.random.normal(self.means, self.sigmas)
        return self.arms[np.argmax(sampled_values)]

