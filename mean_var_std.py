import numpy as np

def calculate(list):
    ls = np.array(list) 
    if len(list) != 9:
           raise ValueError("List must contain nine numbers.")  
    
    calculations = {'mean':[[np.mean(ls[:7:3]),np.mean(ls[1:-1:3]),np.mean(ls[2::3])],
                            [np.mean(ls[:3]),np.mean(ls[3:6]),np.mean(ls[6:])],
                            np.mean(ls)],
                    'variance':[[np.var(ls[:7:3]),np.var(ls[1:-1:3]),np.var(ls[2::3])],
                                [np.var(ls[:3]),np.var(ls[3:6]),np.var(ls[6:])],
                                np.var(ls)],
                    'standard deviation':[[np.std(ls[:7:3]),np.std(ls[1:-1:3]),np.std(ls[2::3])],
                                          [np.std(ls[:3]),np.std(ls[3:6]),np.std(ls[6:])],
                                          np.std(ls)],
                    'max':[[max(ls[:7:3]),max(ls[1:-1:3]),max(ls[2::3])],
                           [max(ls[:3]),max(ls[3:6]),max(ls[6:])],
                           max(ls)],
                    'min':[[min(ls[:7:3]),min(ls[1:-1:3]),min(ls[2::3])],
                           [min(ls[:3]),min(ls[3:6]),min(ls[6:])],
                           min(ls)],
                     'sum':[[sum(ls[:7:3]),sum(ls[1:-1:3]),sum(ls[2::3])],
                            [sum(ls[:3]),sum(ls[3:6]),sum(ls[6:])],
                            sum(ls)]                            
                    }
    return calculations