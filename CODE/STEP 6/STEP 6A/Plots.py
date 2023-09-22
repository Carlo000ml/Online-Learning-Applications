import numpy as np
import math as m
import matplotlib.pyplot as plt
from scipy.stats import norm

def plot_with_confidence(x,arr , name):
    y = np.mean(arr,axis=0)
    
    var = np.var(arr,axis=0)
    std=np.sqrt(var)
    quantile_up = norm.ppf(0.975 , y , std)

    quantile_down = norm.ppf(0.025 , y , std)

    # Plot the line
    plt.plot(x, y, color='blue', label=name)

    # Plot the upper confidence bound
    plt.fill_between(x, quantile_down, quantile_up, color='gray', alpha=0.5, label='95% confidence bound')

    # Add labels and legend
    plt.xlabel('time istant')
    plt.ylabel(name)
    plt.legend()

    # Show the plot
    plt.show()
    

def plot_comparison(x,arr1,arr2,name1,name2,yname):
    y1 = np.mean(arr1,axis=0)
    y2 = np.mean(arr2,axis=0)

    
    
    var1 = np.var(arr1,axis=0)
    std1=np.sqrt(var1)
    quantile_up1 = norm.ppf(0.975 , y1 , std1)

    quantile_down1 = norm.ppf(0.025 , y1 , std1)

    # Plot the line
    plt.plot(x, y1, color='red', label=name1)

    # Plot the upper confidence bound
    plt.fill_between(x, quantile_down1, quantile_up1, color='red', alpha=0.5, label='95% confidence bound')
    
        
    var2 = np.var(arr2,axis=0)
    std2=np.sqrt(var2)
    quantile_up2 = norm.ppf(0.975 , y2 , std2)

    quantile_down2 = norm.ppf(0.025 , y2 , std2)

    # Plot the line
    plt.plot(x, y2, color='green', label=name2)

    # Plot the upper confidence bound
    plt.fill_between(x, quantile_down2, quantile_up2, color='green', alpha=0.5, label='95% confidence bound')

    # Add labels and legend
    plt.xlabel('time instant')
    plt.ylabel(yname)
    plt.legend()

    # Show the plot
    plt.show()
def plot_comparison_multi(x, arr1, arr2, arr3,name1,name2, name3,yname):
    y1 = np.mean(arr1,axis=0)
    y2 = np.mean(arr2,axis=0)
    y3 = np.mean(arr3,axis=0)
    
    
    var1 = np.var(arr1,axis=0)
    std1=np.sqrt(var1)
    quantile_up1 = norm.ppf(0.975 , y1 , std1)

    quantile_down1 = norm.ppf(0.025 , y1 , std1)

    # Plot the line
    plt.plot(x, y1, color='red', label=name1)

    # Plot the upper confidence bound
    plt.fill_between(x, quantile_down1, quantile_up1, color='red', alpha=0.5, label='95% confidence bound')
    
        
    var2 = np.var(arr2,axis=0)
    std2=np.sqrt(var2)
    quantile_up2 = norm.ppf(0.975 , y2 , std2)

    quantile_down2 = norm.ppf(0.025 , y2 , std2)

    # Plot the line
    plt.plot(x, y2, color='green', label=name2)

    # Plot the upper confidence bound
    plt.fill_between(x, quantile_down2, quantile_up2, color='green', alpha=0.5, label='95% confidence bound')
    
    var3 = np.var(arr3,axis=0)
    std3=np.sqrt(var3)
    quantile_up3 = norm.ppf(0.975 , y3 , std3)

    quantile_down3 = norm.ppf(0.025 , y3 , std3)

    # Plot the line
    plt.plot(x, y3, color='blue', label=name3)

    # Plot the upper confidence bound
    plt.fill_between(x, quantile_down3, quantile_up3, color='blue', alpha=0.5, label='95% confidence bound')
    
    # Add labels and legend
    plt.xlabel('time instant')
    plt.ylabel(yname)
    plt.legend()

    # Show the plot
    plt.show()