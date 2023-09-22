class Non_Stationary_Class_1:
    def __init__(self,p1,c1,cum1, n_phases):
        self.n_phases=n_phases
        class_1=(1,1) # <=30 , urban
        details_1={'features': (1,1) , 'prob' :{10:[sublist[0] for sublist in p1],15:[sublist[1] for sublist in p1],20:[sublist[2] for sublist in p1],25:[sublist[3] for sublist in p1],30:[sublist[4] for sublist in p1]}
                   , 'num_of_click_params' :c1
                   , 'cumulative_cost_params': cum1,'class_description': "less than 30  &  urban"}
        
        self.classes={class_1 : details_1}