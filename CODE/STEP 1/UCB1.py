#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Learning_Agent import Learning_Agent
import numpy as np

class UCB1(Learning_Agent):
    def __init__(self, arms):
        super().__init__(arms)
        self.empirical_means = np.zeros(self.n_arms)
        self.confidence = np.array([np.inf] * self.n_arms)
        self.n_samples = np.zeros(self.n_arms)

    def pull_arm(self):
        upper_conf = (self.empirical_means + self.confidence)*(self.arms)
        return self.arms[np.random.choice(np.where(upper_conf == upper_conf.max())[0])]

    def update(self, pulled_arm, reward):
        self.collect_reward(pulled_arm,reward[2])
        index=self.arms_indexing[pulled_arm]
        self.empirical_means[index] = (self.empirical_means[index] * self.n_samples[index] + reward[0]) / (self.n_samples[index] + reward[1])
        for i in range(self.n_arms):
            self.confidence[i] = 5*(2 * np.log(self.t) / self.n_samples[i]) ** 0.5 if self.n_samples[i] > 0 else np.inf
        self.collect_reward(pulled_arm, reward[2])
        self.n_samples[index] += reward[1]
        
     

