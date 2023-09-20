#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Learning_Agent import Learning_Agent
import numpy as np
from GPTS import GPTS


class GPTS_Handler(Learning_Agent):
    def __init__(self, arms):
        self.probabilities={10:0.4,15:0.6,20:0.3,25:0.2,30:0.1}
        super().__init__(arms)
        self.gpts_clicks = GPTS(arms)
        self.gpts_cost = GPTS(arms)

    def update(self, pulled_arm, reward):
    
        self.collect_reward(pulled_arm, reward[3])
        self.gpts_clicks.update(pulled_arm, reward[1])
        self.gpts_cost.update(pulled_arm, reward[2])

    def pull_arm(self, pulled_price):

        n_clicks = np.random.normal(self.gpts_clicks.estimated_curve , self.gpts_clicks.sigmas)
        cum_cost = np.random.normal(self.gpts_cost.estimated_curve , self.gpts_cost.sigmas)
    
        sample_reward =pulled_price * n_clicks*self.probabilities[pulled_price] - cum_cost

        return self.arms[np.random.choice(np.where(sample_reward == sample_reward.max())[0])]

