#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install numpy')


# # question 1

# In[17]:


import numpy as np
import matplotlib.pyplot as plt
pi = np.pi
vals = np.array([-pi, -pi/4, -pi/2, 0, pi/4, pi/2, pi])
tan, cot, sec, cosec = np.tan(vals), 1/np.tan(vals), 1/np.cos(vals), 1/np.sin(vals)
plt.plot(vals, tan, label = 'Tan(x)')
plt.plot(vals, cot, label = 'Cot(x)')
plt.plot(vals, sec, label = 'Sec(x)')
plt.plot(vals, cosec, label = 'Cosec(x)')
plt.legend()
plt.show()


# # question 2

# In[18]:


method = np.array(['A','B','C','D'])
res1 = np.array([2,5,8,5])
res2 = np.array([3,2,5,7])
x2 = [x + 0.25 for x in x1]
plt.bar(x1, res1, width=0.25, label='Result 1')
plt.bar(x2, res2, width=0.25, label='Result 2')
plt.xticks([x + 0.1 for x in x1], method)
plt.legend()
plt.show()


# In[ ]:




