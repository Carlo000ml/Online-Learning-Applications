import pandas as pd
import numpy as np

class Context_Generator():
    def __init__(self):
        
        self.generated_context = []
        self.collected_data = pd.DataFrame(columns=['context', 'pulled_price_arm', 'pulled_bid_arm', 'reward',
                                                    'conversion_rate', 'n_clicks', 'cum_cost'])
        self.n_data = 0
        self.confidence = 0.95
        self.variable_number = 0
        self.feature_combination_seen = []

    def collect_samples(self, context, pulled_price_arm, pulled_bid_arm, reward):
        if context not in self.feature_combination_seen:
            self.feature_combination_seen.append(context)
            #print(self.feature_combination_seen)
        i = self.feature_combination_seen.index(context)
        data = pd.DataFrame([{'context': i, 'pulled_price_arm': pulled_price_arm, 'pulled_bid_arm': pulled_bid_arm,
                              'reward': reward[3], 'conversion_rate': reward[0], 'n_clicks': reward[1], 'cum_cost': reward[2]}])
        self.collected_data = pd.concat([self.collected_data, data])
        if(self.variable_number == 0):
            self.variable_number = len(self.feature_combination_seen[0])
        self.n_data += 1
        #print(data)
        
    def get_samples(self, context):
        
        j = []
        for i in context:
            if type(i) is int:
                j.append(self.feature_combination_seen.index(context))
            else:
                for feature in context:
                    j.append(self.feature_combination_seen.index(feature))
        samples = self.collected_data.copy()
        samples = samples.loc[self.collected_data['context'].isin(j)]
        #print(samples)
        samples = samples.filter(items=['pulled_price_arm', 'pulled_bid_arm',
                                            'conversion_rate', 'n_clicks', 'cum_cost'])
        #print(context)
        list_samples = []
        list_samples.append(samples['pulled_price_arm'].values.tolist())
        list_samples.append(samples['pulled_bid_arm'].values.tolist())
        list_samples.append(samples['conversion_rate'].values.tolist())
        list_samples.append(samples['n_clicks'].values.tolist())
        list_samples.append(samples['cum_cost'].values.tolist())
        return list_samples
        
    def generate_context(self, root_context = None, n_data = None):
        
        #find best global arm
        if root_context:
            arms = self.collected_data.loc[self.collected_data['context'].isin(root_context)]
        else : 
            arms = self.collected_data.copy()
            self.generated_context = []
        if not n_data:
            n_data = self.n_data
        #print(arms)
        pulled_arm, mean = self.pull_best_arm(arms)
        #generate lower bound
        lb_mean_root = self.generate_lb_mean(pulled_arm, arms)
        mean_lb_root = mean - lb_mean_root
        #print('root_mean')
        #print(mean_lb_root)
        lb_split = []
        contexts_variables = []
        for i in range(self.variable_number):

            mean_left_leaf = 0
            lb_probability_left_leaf = 0
            n_data_left_leaf = 0
            mean_right_leaf = 0 
            lb_probability_right_leaf = 0
            n_data_right_leaf = 0
            
            context_left_leaf, context_right_leaf = self.generate_split(i, root_context)
            if(len(context_left_leaf)) > 0 :
                filtered_samples_per_feature_0 = self.collected_data.loc[self.collected_data['context'].isin(context_left_leaf)]
                pulled_arm_left_leaf, mean_left_leaf = self.pull_best_arm(filtered_samples_per_feature_0)
                lb_mean_left_leaf = self.generate_lb_mean(pulled_arm_left_leaf, filtered_samples_per_feature_0)
                mean_left_leaf = mean_left_leaf - lb_mean_left_leaf
                #print('mean_left_leaf')
                #print(mean_left_leaf)
                lb_probability_left_leaf, n_data_left_leaf = self.generate_lb_probability(filtered_samples_per_feature_0, n_data)
                
            if(len(context_right_leaf)) > 0 :
                filtered_samples_per_feature_1 = self.collected_data.loc[self.collected_data['context'].isin(context_right_leaf)]
                pulled_arm_right_leaf, mean_right_leaf = self.pull_best_arm(filtered_samples_per_feature_1)
                lb_mean_right_leaf = self.generate_lb_mean(pulled_arm_right_leaf,  filtered_samples_per_feature_1)
                mean_right_leaf = mean_right_leaf - lb_mean_right_leaf
                #print('mean_right_leaf')
                #print(mean_right_leaf)
                lb_probability_right_leaf, n_data_right_leaf = self.generate_lb_probability(filtered_samples_per_feature_1, n_data)
                
            contexts_variables.append([context_left_leaf, context_right_leaf, n_data_left_leaf, n_data_right_leaf])
            lb_split.append(mean_left_leaf * lb_probability_left_leaf + mean_right_leaf * lb_probability_right_leaf)
            #print(lb_split)

        best_split = max(lb_split)
        best_split_index = lb_split.index(best_split)
        #print(best_split_index, best_split)
        new_context = []
        #print(contexts_variables)
        if best_split > mean_lb_root:
            if len(contexts_variables[best_split_index][0]) > 0 :
                if len(contexts_variables[best_split_index][0]) == 1:
                    temp_context = contexts_variables[best_split_index][0]
                    self.generated_context.append(self.feature_combination_seen[temp_context[0]])
                    #print('generated context:')
                    #print(self.feature_combination_seen[temp_context[0]])
                else:
                    self.generate_context(contexts_variables[best_split_index][0], contexts_variables[best_split_index][2])
            if len(contexts_variables[best_split_index][1]) > 0 :
                if len(contexts_variables[best_split_index][1]) == 1:
                    temp_context = contexts_variables[best_split_index][1]
                    self.generated_context.append(self.feature_combination_seen[temp_context[0]])
                    #print('generated context:')
                    #print(self.feature_combination_seen[temp_context[0]])
                else:
                    self.generate_context(contexts_variables[best_split_index][1], contexts_variables[best_split_index][3])
        else:
            if not root_context:
                root_context = [0, 1, 2]
            for i in root_context:
                new_context.append(self.feature_combination_seen[i])
            self.generated_context.append(new_context)
        #print(self.generated_context)
        return (self.generated_context)
        
        
    def pull_best_arm(self, arms):
        
        arms = arms.filter(items=['pulled_price_arm', 'reward'])
        arms = arms.groupby(['pulled_price_arm']).mean().reset_index()
        #print(arms)
        arms = arms.sort_values(by='reward', ascending=False)
        #print(arms)
        best_arm = arms.iat[0,0]
        mean = arms.iat[0,1]
        #print(best_arm, mean)
        return(best_arm, mean)
        
    def generate_lb_mean(self, pulled_arm, data):
        
        counting_times = data.loc[data['pulled_price_arm'] == pulled_arm]
        #print(counting_times)
        counting_times = counting_times.filter(items = ['pulled_price_arm'])
        #print(counting_times)
        times = len(counting_times)
        #print(times)
        #print(pulled_arm)
        mean_lb = np.sqrt(-np.log(self.confidence)/(2*times))*pulled_arm # moltiplicato per prezzo?
        #print(mean_lb)
        return mean_lb
    
    def generate_lb_probability(self, samples, n_data):
        
        n_data_leaf = len(samples)
        #print(n_data_leaf/n_data)
        #print(np.sqrt(-np.log(self.confidence)/(2*n_data)))
        lb_probability = (n_data_leaf/n_data) - np.sqrt(-np.log(self.confidence)/(2*n_data))
        #print('probability:')
        #print(lb_probability)
        return(lb_probability, n_data_leaf)
    
    def generate_split(self, j, root_context = None):
        
        context_left_leaf = []
        context_right_leaf = []
        to_consider = range(len(self.feature_combination_seen))
        if root_context:
            to_consider = root_context
            #print(to_consider)
        for i in range(len(to_consider)):
            if self.feature_combination_seen[to_consider[i]][j] == 0:
                context_left_leaf.append(to_consider[i])
            else:
                context_right_leaf.append(to_consider[i])
        #print(context_left_leaf, context_right_leaf)
        return(context_left_leaf, context_right_leaf)




