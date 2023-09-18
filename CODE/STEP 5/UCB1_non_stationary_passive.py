#!/usr/bin/env python
# coding: utf-8

# In[2]:


from FIFO import FIFO
import numpy as np
from Learning_Agent import Learning_Agent
import math as m


class UCB1_non_stationary_passive(Learning_Agent):
    
    def __init__(self, arms , window_size):
        super().__init__(arms)
        
        self.empirical_means=np.zeros(self.n_arms)
        self.confidence= np.array([np.inf]*self.n_arms)
        
        self.window_size=window_size
        
        self.tau_crono=FIFO(window_size) # FIFO di liste [arm played , conversions,clicks]
        
        
        
    def pull_arm(self):
        plays=np.zeros(self.n_arms)
        
# Gioca una volta tutti gli arms      
        for arm in self.arms:
            idx=self.arms_indexing[arm]
            
            # number of times arm has been played in the last tau rounds
            plays[idx]=sum(el[0]==arm for el in self.tau_crono.queue)
            
        zeros=np.where(plays== 0)[0]
        
        # if not all the arms have been played yet in the last tau rounds
        if len(zeros)>0:
            idx=int(np.random.choice(zeros))
          
            return self.arms[idx]
        
        
        
        upper_conf=(self.empirical_means + self.confidence) # up
        
        expected_pricing_rew=np.zeros(self.n_arms)
        for i in range(self.n_arms):
            expected_pricing_rew[i]=self.arms[i]*upper_conf[i]
            
        idx=int(np.random.choice(np.where(expected_pricing_rew==expected_pricing_rew.max())[0]))
    
        return self.arms[idx]
    
    
    def update(self,pulled_arm , reward):
        
        idx=self.arms_indexing[pulled_arm]
        
        self.collect_reward(pulled_arm,reward[2])
        
        self.tau_crono.add([pulled_arm,reward[0],reward[1]])
        
        self.empirical_means=self.compute_empirical_means_tau()
        
        self.confidence=self.compute_confidence_tau()
        
        self.t+=1
        

        
        
        
        
    def compute_empirical_means_tau(self):
        
        empirical_means=np.zeros(self.n_arms)
        
        for arm in self.arms:
            idx=self.arms_indexing[arm]
            
            n_plays=0
            successes=0
            
            for el in self.tau_crono.queue:
                if el[0]==arm:
                    n_plays+=el[2]
                    successes+=el[1]
                    
            empirical_means[idx]=0 if n_plays==0 else successes/n_plays
            
            
        return empirical_means
    
    
    def compute_confidence_tau(self):
        
        confidence=np.zeros(self.n_arms)+np.inf
        
        for arm in self.arms:
            
            idx=self.arms_indexing[arm]
            
            # number of times arm has been played in the last tau rounds
            n_plays_arm=0
            for el in self.tau_crono.queue:
                 if el[0]==arm: n_plays_arm+=el[2]
            
            if n_plays_arm>0: confidence[idx]=5*( (2*m.log(self.t+1))/n_plays_arm)**0.5
                
        
        return confidence
                
            


# In[ ]:




