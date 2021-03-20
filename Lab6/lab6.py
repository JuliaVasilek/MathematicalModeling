#!/usr/bin/env python
# coding: utf-8

# In[26]:


import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


# In[27]:


a = 0.01
b = 0.02
N = 6666
I0 = 83
R0 = 6
S0 = N - I0 - R0


# In[30]:


def syst(x,t):
    #I0<=I*
    #return np.array([0, (-1)*b*x[1], b*x[1]])
    #I0>I*
    return np.array([0, a*S0 - (-1)*b*x[1], b*x[1]])


# In[31]:


t0 = 0
x0 = [S0,I0,R0] 
t = np.linspace(0, 200, 2000)
y = odeint(syst, x0, t)
plt.plot(t, y)


# In[ ]:




