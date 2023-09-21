#!/usr/bin/env python
# coding: utf-8

# In[1]:


import Functions as f
import numpy as np


class Enviroment:
    
    def __init__(self, n_price_arms , n_bid_arms ,classe): 
        
        self.classe=classe
        self.n_price_arms=n_price_arms
        self.n_bid_arms=n_bid_arms
        
        
    def round(self ,pulled_price_arm , pulled_bid_arm):
        # price and bid

        
        # class details

        classe=self.classe.classes[(1,1)]
        click_numb_params=classe['num_of_click_params']
        conv_prob=classe['prob'][pulled_price_arm]
        cum_daily_cost_param=classe['cumulative_cost_params']
        
        # Generate quantities
        clicks=f.generate_num_of_cliks_given_bid( pulled_bid_arm , click_numb_params[0] ,click_numb_params[1] , click_numb_params[2] , 100 )
        cum_daily_cost=f.cumulative_cost_sample( pulled_bid_arm , cum_daily_cost_param , 100)
        
        conversions=np.random.binomial(clicks,conv_prob)
        
        if(clicks==0): pricing_rew=0
        else: pricing_rew=conversions/clicks
        
        # Class 1 reward
        reward=conversions*pulled_price_arm-cum_daily_cost
        
    
        
        to_return=(conversions,clicks,reward)
                  
      
        return(to_return)
 

