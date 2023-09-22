import math as m
import numpy as np

def number_of_clicks_given_bid(x,a,b,c):
    return(-((1/a)*x-b)**2+c )


def generate_num_of_cliks_given_bid(x,a,b,c,sig):
    samp=number_of_clicks_given_bid(x,a,b,c) +np.random.normal(0,sig)
    if samp>=0: return samp
    return 0
def cumulative_daily_cost(x,a):
    return a*m.log(x)

def cumulative_cost_sample(x,a,std):
    samp=cumulative_daily_cost(x,a) +np.random.normal(0,std)
    if samp>=0: return samp
    return 0