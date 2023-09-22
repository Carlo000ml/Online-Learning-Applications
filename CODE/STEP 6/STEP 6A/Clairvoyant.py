import Functions as f
import numpy as np

class Clairvoyant:  
    
    def __init__(self , enviroment ,class_features ,  arms):  # Clairvoyant knows the enviroment, the class to optimize and the arms 
        self.enviroment=enviroment
        self.arms=arms
        self.classe=enviroment.classes.classes[class_features]
        
        
        
    def expected_reward(self,arm):
        pass
    
    
    def optimal_arm(self):
        pass
    
    
class Clairvoyant_pricing(Clairvoyant):
    
    def __init__(self,enviroment, class_features , arms):
        super().__init__(enviroment , class_features , arms)
        
    def expected_reward(self,arm):
        #parameters
        conv_prob=self.classe['prob'][arm]
        
        #reward
        expected_reward=conv_prob*arm
        
        return expected_reward
    
    def optimal_arm(self):# the Clairvoyant pulls the arm with the largest expected reward
        rewards=np.zeros(len(self.arms))
        for i in range(len(self.arms)):
            rewards[i]=self.expected_reward(self.arms[i])
            
        return self.arms[np.argmax(rewards)]
            
        

class Clairvoyant_bid(Clairvoyant):
    
    def __init__(self , enviroment , class_features , arms):
        super().__init__(enviroment , class_features , arms)
        
    def expected_reward(self,arm , optimal_price):
        #parameters
        daily_click_params=self.classe['num_of_click_params']
        conv_prob=self.classe['prob'][optimal_price]
        cum_daily_cost_param=self.classe['cumulative_cost_params']
        
        #quantities to generate
        clicks=f.number_of_clicks_given_bid(arm , daily_click_params[0] , daily_click_params[1] , daily_click_params[2])
        cum_daily_cost=f.cumulative_daily_cost(arm , cum_daily_cost_param)
        
        #reward
        expected_reward=clicks*conv_prob*optimal_price - cum_daily_cost
        
        return expected_reward
    
    def optimal_arm(self,optimal_price):# the Clairvoyant pulls the arm with the largest expected reward
        rewards=np.zeros(len(self.arms))
        for i in range(len(self.arms)):
            rewards[i]=self.expected_reward(self.arms[i],optimal_price)
            
        return self.arms[np.argmax(rewards)]