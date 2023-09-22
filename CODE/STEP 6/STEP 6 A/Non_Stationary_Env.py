import Functions as f
import numpy as np
from Non_Stationary_Class_1 import *

class Non_Stationary_Env:
    def __init__(self, n_price_arms, n_bid_arms, horizon , class_1):
        self.t = 0
        self.n_phases = class_1.n_phases
        self.phases_size = horizon/self.n_phases
        self.current_phase=0
        self.classes=class_1

    def round(self ,pulled_price_arm , pulled_bid_arm):
        self.current_phase = (int(self.t / self.phases_size))%self.n_phases
        

    # class 1

        click_numb_params_class_1=self.classes.classes[(1,1)]['num_of_click_params']
        conv_prob_class_1=self.classes.classes[(1,1)]['prob'][pulled_price_arm][self.current_phase]
        cum_daily_cost_param_class_1=self.classes.classes[(1,1)]['cumulative_cost_params']

        # Generate quantities
        click_class_1=f.generate_num_of_cliks_given_bid( pulled_bid_arm , click_numb_params_class_1[0] ,click_numb_params_class_1[1]
                                                      ,click_numb_params_class_1[2] , 50 )
        cum_daily_cost_class_1=f.cumulative_cost_sample( pulled_bid_arm , cum_daily_cost_param_class_1 , 25)
        conversions_class_1=np.random.binomial(click_class_1,conv_prob_class_1)
        if(click_class_1==0): pricing_rew_1=0
        else: pricing_rew_1=conversions_class_1/click_class_1

        # Class 1 reward
      
        reward_class_1=conversions_class_1*pulled_price_arm-cum_daily_cost_class_1


   
     
        to_return=(conversions_class_1,click_class_1,reward_class_1)

        self.t += 1

        return(to_return)