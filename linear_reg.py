import numpy as np
import matplotlib.pyplot as plt

def estimate_coeff(x,y):
    n=np.size(x)

    m_x=np.mean(x)
    m_y=np.mean(y)


    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x
 
  # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x
 
    return (b_0, b_1)

