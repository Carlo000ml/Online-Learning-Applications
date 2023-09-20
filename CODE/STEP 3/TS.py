#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Learning_Agent import Learning_Agent
import numpy as np

class TS(Learning_Agent):
    
    def __init__(self, arms):
        super().__init__(arms)
        
        self.beta_params=np.ones([len(arms) , 2])
        
    def pull_arm(self):
        
        means=np.random.beta(self.beta_params[:,0] , self.beta_params[:,1])
        
        return [self.arms[np.argmax(means) ] , np.argmax(means)]
    
    def update(self, pulled_arm , reward):
        self.t+=1
        pulled_arm_index=self.arms_indexing[pulled_arm]
        
        successes=reward[0]
        fails=reward[1]-successes
        
        self.beta_params[pulled_arm_index][0]=self.beta_params[pulled_arm_index][0]+successes
        self.beta_params[pulled_arm_index][1]=self.beta_params[pulled_arm_index][1]+fails
        
       


# In[ ]:




