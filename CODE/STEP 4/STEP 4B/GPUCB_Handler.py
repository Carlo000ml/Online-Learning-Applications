#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Learning_Agent import Learning_Agent
import numpy as np
from GPUCB import GPUCB
import math as m
import matplotlib.pyplot as plt
from scipy.stats import norm


class GPUCB_Handler(Learning_Agent):
    def __init__(self, arms):
        self.probabilities={10:0.4,15:0.6,20:0.3,25:0.2,30:0.1}
        super().__init__(arms)
        self.gpucb_clicks = GPUCB(arms,1)
        self.gpucb_cost = GPUCB(arms,2)

    def update(self, pulled_arm, reward):
        
    
        self.collect_reward(pulled_arm, reward[3])
        self.gpucb_clicks.update(pulled_arm, reward[1])
        self.gpucb_cost.update(pulled_arm, reward[2])
        if(self.t in [15,150,364]):self.plot()

    def pull_arm(self, pulled_price):

        n_clicks = self.gpucb_clicks.estimated_curve + self.gpucb_clicks.confidence
        cum_cost = self.gpucb_cost.estimated_curve - self.gpucb_cost.confidence
    
        sample_reward =pulled_price * n_clicks*self.probabilities[pulled_price] - cum_cost

        return self.arms[np.random.choice(np.where(sample_reward == sample_reward.max())[0])]
   
    def plot(self):
        print(self.t)
        plt.figure(self.t)
        plt.plot(self.gpucb_clicks.gp.collected_X, self.gpucb_clicks.gp.collected_Y , 'ro', label=u'Observed Clicks')
        plt.plot(self.arms ,self.gpucb_clicks.estimated_curve, 'b-' , label=u'Predicted Clicks')
        plt.fill_between(self.arms,self.gpucb_clicks.estimated_curve-self.gpucb_clicks.confidence,self.gpucb_clicks.estimated_curve+self.gpucb_clicks.confidence
       ,
        alpha=.5 , fc='b', ec='None', label= '95% conf  interval')
        plt.xlabel('$x$')
        plt.ylabel('$clicks(x)$')
        plt.legend(loc='lower right')
        plt.show
        
        plt.figure(self.t+1)
        
        
        plt.plot(self.gpucb_cost.gp.collected_X, self.gpucb_cost.gp.collected_Y , 'ro', label=u'Observed Clicks')
        plt.plot(self.arms ,self.gpucb_cost.estimated_curve, 'b-' , label=u'Predicted Clicks')
        plt.fill_between(self.arms,self.gpucb_cost.estimated_curve-self.gpucb_cost.confidence,self.gpucb_cost.estimated_curve+self.gpucb_cost.confidence
       ,
        alpha=.5 , fc='b', ec='None', label= '95% conf  interval')
        plt.xlabel('$x$')
        plt.ylabel('$cum(x)$')
        plt.legend(loc='lower right')
        plt.show()
