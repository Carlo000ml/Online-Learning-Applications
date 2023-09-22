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
        
        return [self.arms[np.argmax(means* self.arms)] ,means[np.argmax(means* self.arms)] ]
    
    def update(self, pulled_arm , reward):

        pulled_arm_index=self.arms_indexing[pulled_arm]
        
        successes=reward[0]
        fails=reward[1]-successes
        
        self.beta_params[pulled_arm_index][0]=self.beta_params[pulled_arm_index][0]+successes
        self.beta_params[pulled_arm_index][1]=self.beta_params[pulled_arm_index][1]+fails
        self.collect_reward(pulled_arm , reward[2])
        
    def update_tot(self,arms,conversions,clicks):
        ARMS=np.array(arms)
        A=np.array(conversions)
        B=np.array(clicks)
        
        for i in range(self.n_arms):

            succ=sum(A[np.where(ARMS==self.arms[i])])
            insucc=sum(B[np.where(ARMS==self.arms[i])])-succ
            self.beta_params[i][0]+=succ
            self.beta_params[i][1]+=insucc

# In[ ]:




