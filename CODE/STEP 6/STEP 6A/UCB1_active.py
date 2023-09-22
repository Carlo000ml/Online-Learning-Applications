import numpy as np
from Learning_Agent import Learning_Agent
import math as m

class UCB1_active(Learning_Agent):
    
    def __init__(self,arms,alpha):
        super().__init__(arms)
        
        self.empirical_means=np.zeros(self.n_arms)
        
        self.confidence= np.array([np.inf]*self.n_arms)
        
        self.tau=np.zeros(self.n_arms)
        
        self.crono={arm:[0,0,0] for arm in self.arms}  # dictionary della cronologia arm : (conversions da tau ad ora, clicks da tau ad ora , n_plays)
        
        self.alpha=alpha
        
    def pull_arm(self):
        upper_conf = (self.empirical_means + self.confidence)*self.arms
        
        sample=np.random.binomial(1,self.alpha)
        
        if sample==0 : return self.arms[np.random.choice(np.where(upper_conf==upper_conf.max())[0])]
        
        return np.random.choice(self.arms)
        
       
    
    def update(self,pulled_arm,reward):
        self.t+=1
        pulled_arm_index=self.arms_indexing[pulled_arm]
        self.collect_reward(pulled_arm,reward[2])
        
        self.crono[pulled_arm][0]+=reward[0]
        self.crono[pulled_arm][1]+=reward[1]
        self.crono[pulled_arm][2]+=1
        
        self.empirical_means[pulled_arm_index]=self.crono[pulled_arm][0]/self.crono[pulled_arm][1]
        
        n_tot=0
        for arm in self.arms:
            n_tot+=self.crono[arm][1]
            
        for el in self.arms:
            idx=self.arms_indexing[el]
            n_samples=self.crono[el][1]
            self.confidence[idx]=(2*np.log(n_tot)/n_samples)**0.5 if n_samples >0 else np.inf
            
            
    def change_detected(self,arm):
        
        self.crono[arm]=[0,0,0]