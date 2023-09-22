#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np

class CUSUM:
    def __init__(self,arms,M,eps,h):
        self.arms=arms
        self.n_arms=len(arms)
        self.arms_indexing={arms[i] : i for i in range(self.n_arms) }
        
        
        self.M=M
        self.h=h
        self.eps=eps
        self.t=0
        
        self.references=np.zeros(self.n_arms)
        self.g_pluses=np.zeros(self.n_arms)
        self.g_minuses=np.zeros(self.n_arms)
        
        self.number_of_valid_samples={arms[i] : 0 for i in range(self.n_arms) }
        
        
    def update(self,arm,sample):
            arm_index=self.arms_indexing[arm]
            self.number_of_valid_samples[arm]+=1
            valid_samples=self.number_of_valid_samples[arm]
            
            self.t+=1
            if valid_samples <= self.M:
                self.references[arm_index] +=sample/self.M
                return False
            else:
                s_pluses=(sample - self.references[arm_index])-self.eps
                s_minuses=-(sample - self.references[arm_index]) - self.eps
                self.g_pluses[arm_index]=max(0,self.g_pluses[arm_index]+s_pluses)
                self.g_minuses[arm_index]=max(0,self.g_pluses[arm_index] + s_minuses)
                return self.g_pluses[arm_index] > self.h or self.g_minuses[arm_index] > self.h
            
    def reset(self,arm):
            self.number_of_valid_samples[arm]=0
            arm_index=self.arms_indexing[arm]
            
            self.references[arm_index]=0
            self.g_pluses[arm_index]=0
            self.g_minuses[arm_index]=0
            


# In[ ]:




