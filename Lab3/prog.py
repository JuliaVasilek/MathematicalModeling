#!/usr/bin/env python
# coding: utf-8

# In[24]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


# In[25]:


x0=22222
y0=11111
#a=0.22
a=0.31
#b=0.77
b=0.79
#c=0.66
c=0.59
#h=0.11
h=0.21


# In[26]:


def P(t):
    #p=np.sin(0.5*t)+2
    p=np.sin(2.5*t)+1
    return p

def Q(t):
    #q=np.cos(0.5*t)+2
    q=np.cos(2*t)+2
    return q


# In[27]:


def syst(y, t):
    #return np.array([-a*y[0]-b*y[1]+P(t), -c*y[0]-h*y[1]+Q(t)])
    return np.array([-a*y[0]-b*y[1]+P(t), -c*y[0]*y[1]-h*y[1]+Q(t)])


# In[28]:


v0 = np.array([x0, y0])
t = np.linspace(0, 3)


# In[29]:


sol = odeint(syst, v0, t)


# In[30]:


plt.plot(t, sol[:,0])
plt.plot(t, sol[:,1])
plt.xlabel("Время")
plt.ylabel("Кол-во человек")
#plt.title("Модель №1")
plt.title("Модель №2")
plt.legend(["Армия X","Армия Y"])
plt.show


# In[ ]:




