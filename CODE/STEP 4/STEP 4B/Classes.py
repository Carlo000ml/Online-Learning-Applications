#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Classes:
    def __init__(self): 
        
        class_1=(1,1) # <=30 , urban
        details_1={'features': (1,1) , 'prob' :{10:0.4,15:0.6,20:0.3,25:0.2,30:0.1} , 'num_of_click_params' :(3,85,10000)  , 'cumulative_cost_params': 700
                , 'class_description': "less than 30  &  urban"}
        
        self.classes={class_1 : details_1 }
        
        # for every class specify a dictionry containing all the necessary information ( prob , parameters , desctiption)
        
        class_1=(1,1) # <=30 , urban
        details_1={'features': (1,1) , 'prob' :{10:0.4,15:0.6,20:0.3,25:0.2,30:0.1} , 'num_of_click_params' :(3,85,10000)  , 'cumulative_cost_params': 700
                , 'class_description': "less than 30  &  urban"}
            
        class_2=(0,1) # >30 , urban        
        details_2={'features': (0,1) ,'prob' :{10:0.1,15:0.2,20:0.4,25:0.7,30:0.4} , 'num_of_click_params' :(3,95,9000)  , 'cumulative_cost_params': 500
                , 'class_description': "More than 30  &  urban"}
            
        class_3=(0,0)  # >30, rural        
        details_3={'features': (0,0) ,'prob' :{10:0.1,15:0.1,20:0.3,25:0.5,30:0.6} , 'num_of_click_params' :(3,100,8000)  , 'cumulative_cost_params': 400
                , 'class_description': "More than 30  &  Rural"}
        
        # the final object is a dictionary 
        
        self.classes={class_1 : details_1 , class_2: details_2  ,  class_3 : details_3}
            
            
class Context:
    def __init__(self, classes):
        if sum(partition)!=1: raise Exception("wrong Partition")
        if len(classes.classes)!=len(partition):raise Exception("Number of classes not align with the partition")
            
        self.classes=classes
 
    