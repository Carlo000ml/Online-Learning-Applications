from Learning_Agent import Learning_Agent
import numpy as np
import math as m

class EXP3(Learning_Agent):
    def __init__(self, arms, exploration_param):
        super().__init__(arms)
        self.exploration_param=exploration_param
        self.weights = np.ones(self.n_arms)
        sum_weights=np.sum(self.weights)
        self.probabilities = (1-self.exploration_param)*(self.weights/sum_weights) + (self.exploration_param/self.n_arms)

    def pull_arm(self):
        index=np.random.choice(self.n_arms,p=self.probabilities)
        return self.arms[index]

    def update(self, chosen_arm, reward):
        sum_weights=np.sum(self.weights)
        self.probabilities = (1-self.exploration_param)*(self.weights/sum_weights) + (self.exploration_param/self.n_arms)
        estimated_reward = 0.00001*reward/self.probabilities[self.arms_indexing[chosen_arm]]
        self.weights[self.arms_indexing[chosen_arm]]=np.exp((estimated_reward)/self.n_arms)*self.weights[self.arms_indexing[chosen_arm]]
        self.t=self.t+1