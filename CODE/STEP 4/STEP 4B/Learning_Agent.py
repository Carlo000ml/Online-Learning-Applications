#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
class Learning_Agent:
    
    def __init__(self , arms):
        self.arms=arms
        self.n_arms=len(arms)
        self.arms_indexing={arms[i] : i for i in range(self.n_arms) }
        self.t=0  # round indicator
        self.reward_per_arm={arm : [] for arm in arms}
        self.collected_reward=np.array([])
        
    def pull_arm(self):
        pass
    
    def collect_reward(self, pulled_arm, reward):
        self.t+=1
        self.collected_reward = np.append(self.collected_reward, reward)
        
    def update(self):
        pass
        
        


# In[ ]:




