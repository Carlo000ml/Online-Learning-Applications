#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import Functions as f
from Classes import *


class Enviroment:
    
    def __init__(self, n_price_arms , n_bid_arms ,classes): 
        
        self.classes=classes
        self.n_price_arms=n_price_arms
        self.n_bid_arms=n_bid_arms
        
        
    def round(self ,pulled_price_arm , pulled_bid_arm):
        # price and bid

        
        # class details

        price_class_1=pulled_price_arm[0]
        bid_class_1=pulled_bid_arm[0]
        
        # class details
   
        class_1=self.classes.classes[(1,1)]
        click_numb_params_class_1=class_1['num_of_click_params']
        conv_prob_class_1=class_1['prob'][price_class_1]
        cum_daily_cost_param_class_1=class_1['cumulative_cost_params']
        
        # Generate quantities
        click_class_1=f.generate_num_of_cliks_given_bid( bid_class_1 , click_numb_params_class_1[0] ,click_numb_params_class_1[1] ,                     click_numb_params_class_1[2] , 50 )
        cum_daily_cost_class_1=f.cumulative_cost_sample( bid_class_1 , cum_daily_cost_param_class_1 , 25)
        conversions_class_1=np.random.binomial(click_class_1,conv_prob_class_1)
        if(click_class_1==0): pricing_rew_1=0
        else: pricing_rew_1=conversions_class_1/click_class_1
        
        # Class 1 reward
        reward_class_1=click_class_1*conv_prob_class_1*price_class_1-cum_daily_cost_class_1
        
        
        # price and bid
        price_class_2=pulled_price_arm[1]
        bid_class_2=pulled_bid_arm[1]
        
        # class details

        class_2=self.classes.classes[(0,1)]
        click_numb_params_class_2=class_2['num_of_click_params']
        conv_prob_class_2=class_2['prob'][price_class_2]
        cum_daily_cost_param_class_2=class_2['cumulative_cost_params']
        
        # Generate quantities
        click_class_2=f.generate_num_of_cliks_given_bid( bid_class_2 , click_numb_params_class_2[0] ,click_numb_params_class_2[1] , click_numb_params_class_2[2] , 50 )
        cum_daily_cost_class_2=f.cumulative_cost_sample( bid_class_2 , cum_daily_cost_param_class_2 , 25)
        conversions_class_2=np.random.binomial(click_class_2,conv_prob_class_2)
        if(click_class_2==0): pricing_rew_2=0
        else: pricing_rew_2=conversions_class_2/click_class_2
        
        # Class 2 reward
        reward_class_2=click_class_2*conv_prob_class_2*price_class_2-cum_daily_cost_class_2
    
    
    # class 3
        # price and bid
        price_class_3=pulled_price_arm[2]
        bid_class_3=pulled_bid_arm[2]
        
        # class details
        class_3=self.classes.classes[(0,0)]
        click_numb_params_class_3=class_3['num_of_click_params']
        conv_prob_class_3=class_3['prob'][price_class_3]
        cum_daily_cost_param_class_3=class_3['cumulative_cost_params']
        
        # Generate quantities
        click_class_3=f.generate_num_of_cliks_given_bid( bid_class_3 , click_numb_params_class_3[0] ,click_numb_params_class_3[1] , click_numb_params_class_3[2] , 50 )
        cum_daily_cost_class_3=f.cumulative_cost_sample( bid_class_3 , cum_daily_cost_param_class_3 , 25)
        conversions_class_3=np.random.binomial(click_class_3,conv_prob_class_3)
        if(click_class_3==0): pricing_rew_3=0
        else: pricing_rew_3=conversions_class_3/click_class_3
       
        # Class 3 reward
        reward_class_3=conversions_class_3*price_class_3-cum_daily_cost_class_3
        
        to_return={'reward_class_1': [conversions_class_1 , click_class_1,cum_daily_cost_class_1,reward_class_1] , 'reward_class_2' : [conversions_class_2 , click_class_2,cum_daily_cost_class_2,reward_class_2] , 'reward_class_3' : [conversions_class_3 , click_class_3,cum_daily_cost_class_3,reward_class_3] }
      
        return(to_return)
        
        
    
 

