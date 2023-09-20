#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import math as m
import matplotlib.pyplot as plt
from scipy.stats import norm
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C

class GP2:
    def __init__(self, std,support):
        
        self.std=std   
        theta=1.0
        l=1.0
        kernel = C(theta, (1e-3, 1e7)) * RBF(l, (0.0001, 1e3))

        self.gp=GaussianProcessRegressor(kernel=kernel, alpha=std**2, normalize_y=False, n_restarts_optimizer=10)
        self.support=support
        
        self.collected_X=np.array([])
        self.collected_Y=np.array([])

        
    def new_datum(self,x,y):
        
        self.collected_X=np.append(self.collected_X,x)
        self.collected_Y=np.append(self.collected_Y,y)
        
        X=np.atleast_2d(self.collected_X).T

        Y=self.collected_Y.ravel()
        
        self.gp.fit(X,Y)
        
        
    def estimate_curve(self,plot=False):
        X=np.atleast_2d(self.support).T
        
        estimated_curve,estimated_sigma=self.gp.predict(X , return_std=True)
        
        if plot:
                plt.figure(1)
               
                plt.plot(X ,estimated_curve, 'b-' , label=u'Estimated curve')
                plt.fill(np.concatenate([X , X[::-1]]),
               np.concatenate([estimated_curve - 1.96*estimated_sigma , (estimated_curve + 1.96*estimated_sigma)[::-1]]),
                alpha=.5 , fc='b', ec='None', label= '95% conf  interval')
                plt.xlabel('$x$')
                plt.ylabel('$f(x)$')
                plt.legend(loc='lower right')
                plt.show()
    

        return [estimated_curve,estimated_sigma]
        
        
        