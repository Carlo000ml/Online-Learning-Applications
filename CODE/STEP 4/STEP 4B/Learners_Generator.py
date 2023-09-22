from Learning_Agent import *
from GPUCB import *
from GPTS import *
from GPTS_TS import *
from GPUCB1_TS import *
from GPTS_TS import *
from GPUCB1_TS import *
from Context_Generator import *

class Learners_Generator:
    def __init__(self, GP_type, bid_arms):
        
        self.ct_generator = Context_Generator()
        self.GP_type = GP_type
        self.generated_GPs = {
            tuple([(1,1), (0,1), (0,0)]): self.GP_type(bid_arms)
        }
        self.T = 0
        self.bid_arms = bid_arms
        self.collected_rewards = []
        
    def pull_arms(self):
        
        pulled_arms = {}
        #print(self.generated_GPs.keys())
        for context in self.generated_GPs.keys():
            arms = self.generated_GPs[context].pull_arm()
            if type(context[0]) is not int :
                for feature in context:
                    pulled_arms[self.map_features(feature)] = arms
            else:
                pulled_arms[self.map_features(context)] = arms
        #print(pulled_arms)
        return pulled_arms
            
        
    def update(self, pulled_price_arms, pulled_bid_arms, reward_arr):
        
        self.T += 1
        #print(self.T)
        cumulative_reward = 0
        #print(reward_arr)
        for context in self.generated_GPs.keys():
            
            if type(context[0]) is int:
            
                n_conversions = reward_arr[context][0]
                n_clicks = reward_arr[context][1]
                cum_cost = reward_arr[context][2]
                reward = reward_arr[context][3]
                cumulative_reward += reward
                update_reward = [n_conversions,n_clicks, cum_cost]
                #print(update_reward)
                self.generated_GPs[context].update(pulled_price_arms[self.map_features(context)], pulled_bid_arms[self.map_features(context)], update_reward)
                self.ct_generator.collect_samples(context, pulled_price_arms[self.map_features(context)], pulled_bid_arms[self.map_features(context)], reward_arr[context])
                
            else:
                n_conversions = sum(reward_arr[feature][0] for feature in context)
                n_clicks = sum(reward_arr[feature][1] for feature in context)
                cum_cost = sum(reward_arr[feature][2] for feature in context)
                reward = sum(reward_arr[feature][3] for feature in context)
                cumulative_reward += reward
                update_reward = [n_conversions,n_clicks, cum_cost]
                #print(update_reward)
                self.generated_GPs[context].update(pulled_price_arms[self.map_features(context)], pulled_bid_arms[self.map_features(context)], update_reward)
                for feature in context:
                    self.ct_generator.collect_samples(feature, pulled_price_arms[self.map_features(feature)], pulled_bid_arms[self.map_features(feature)], reward_arr[feature])
                    
        self.collected_rewards.append(cumulative_reward)
        
        
        if self.T % 14 == 0:
            generated_context = self.ct_generator.generate_context()
            keys = list(self.generated_GPs.keys()).copy()
            for context in keys:
                if context not in generated_context:
                    del self.generated_GPs[context]
            for context in generated_context:
                if context not in keys:
                    #print(context)
                    self.generated_GPs[tuple(context)] = self.GP_type(self.bid_arms)
                    # retrieve samples
                    samples = self.ct_generator.get_samples(context)
                    #print(samples)
                    self.generated_GPs[tuple(context)].update_tot([samples[0], samples[1], samples[2], 
                                                                             samples[3], samples[4]])
            #print(self.generated_GPs)
            #print(self.generated_GPs.keys())
            #print(len(self.generated_GPs))
            
        return cumulative_reward
    
    def map_features(self, context):
        if context == (1,1):
            return 0
        elif context == (0,1):
            return 1
        elif context == (0,0):
            return 2
        else:
            return self.map_features(context[0])



