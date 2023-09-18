#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Learning_Agent import Learning_Agent
import numpy as np
from GPUCB import GPUCB


class GPUCB_Handler(Learning_Agent):
    def __init__(self, arms):
        self.probabilities={10:0.4,15:0.6,20:0.3,25:0.2,30:0.1}
        super().__init__(arms)
        self.gpucb_clicks = GPUCB(arms)
        self.gpucb_cost = GPUCB(arms)

    def update(self, pulled_arm, reward):
    
        self.collect_reward(pulled_arm, reward[3])
        self.gpucb_clicks.update(pulled_arm, reward[1])
        self.gpucb_cost.update(pulled_arm, reward[2])

    def pull_arm(self, pulled_price):

        n_clicks = self.gpucb_clicks.estimated_curve + self.gpucb_clicks.confidence
        cum_cost = self.gpucb_cost.estimated_curve - self.gpucb_cost.confidence
    
        sample_reward =pulled_price * n_clicks*self.probabilities[pulled_price] - cum_cost

        return self.arms[np.random.choice(np.where(sample_reward == sample_reward.max())[0])]

