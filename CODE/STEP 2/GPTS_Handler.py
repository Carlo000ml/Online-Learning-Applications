#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Learning_Agent import Learning_Agent
import numpy as np
from GPTS import GPTS
import math as m
import matplotlib.pyplot as plt
from scipy.stats import norm



class GPTS_Handler(Learning_Agent):
    def __init__(self, arms):
        self.probabilities={10:0.4,15:0.6,20:0.3,25:0.2,30:0.1}
        super().__init__(arms)
        self.gpts_clicks = GPTS(arms,1)
        self.gpts_cost = GPTS(arms,2)

    def update(self, pulled_arm, reward):
    
        self.collect_reward(pulled_arm, reward[3])
        self.gpts_clicks.update(pulled_arm, reward[1])
        self.gpts_cost.update(pulled_arm, reward[2])
        if(self.t in [15,150,364]):self.plot()
        

    def pull_arm(self, pulled_price):

        n_clicks = np.random.normal(self.gpts_clicks.estimated_curve , self.gpts_clicks.sigmas)
        cum_cost = np.random.normal(self.gpts_cost.estimated_curve , self.gpts_cost.sigmas)
    
        sample_reward =pulled_price * n_clicks*self.probabilities[pulled_price] - cum_cost

        return self.arms[np.random.choice(np.where(sample_reward == sample_reward.max())[0])]

    def plot(self):
        print(self.t)
        plt.figure(self.t)
        plt.plot(self.gpts_clicks.gp.collected_X, self.gpts_clicks.gp.collected_Y , 'ro', label=u'Observed Clicks')
        plt.plot(self.arms ,self.gpts_clicks.estimated_curve, 'b-' , label=u'Predicted Clicks')
        plt.fill_between(self.arms,self.gpts_clicks.estimated_curve-1.96*self.gpts_clicks.sigmas,self.gpts_clicks.estimated_curve+1.96*self.gpts_clicks.sigmas
       ,
        alpha=.5 , fc='b', ec='None', label= '95% conf  interval')
        plt.xlabel('$x$')
        plt.ylabel('$clicks(x)$')
        plt.legend(loc='lower right')
        plt.show
        
        plt.figure(self.t+1)
        
        
        plt.plot(self.gpts_cost.gp.collected_X, self.gpts_cost.gp.collected_Y , 'ro', label=u'Observed Clicks')
        plt.plot(self.arms ,self.gpts_cost.estimated_curve, 'b-' , label=u'Predicted Clicks')
        plt.fill_between(self.arms,self.gpts_cost.estimated_curve-1.96*self.gpts_cost.sigmas,self.gpts_cost.estimated_curve+1.96*self.gpts_cost.sigmas
       ,
        alpha=.5 , fc='b', ec='None', label= '95% conf  interval')
        plt.xlabel('$x$')
        plt.ylabel('$cum(x)$')
        plt.legend(loc='lower right')
        plt.show()
        
        
        
        
        
        
        