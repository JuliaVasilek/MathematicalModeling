#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


# In[13]:


#1
#g=0
#w=17
#2
#g=22
#w=23
#3
g=5
w=8


# In[14]:


def dx(x, t):
    return np.array([x[1], -w*x[0]-g*x[1]-f(t)])

def f(t):
    #1 and 2
    #return 0
    #3
    return 0.25*np.sin(8*t)


# In[15]:


t = np.linspace(0, 58, 500)
x0 = np.array([0.2, -0.3])
x = odeint (dx, x0, t)


# In[16]:


plt.plot(x[:,0], x[:,1])
plt.grid()
plt.show()


# In[ ]:




