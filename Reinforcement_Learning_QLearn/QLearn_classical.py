
# coding: utf-8

# In[1]:


import numpy as np
import random


# In[2]:


from QLearn_functions import FindPath


# In[3]:


#column 0 = left
#column 1 = right
#column 2 = up
#column 3 = down
# --------------- L   R   U   D -------------- #
env = np.array([[-2,  0, -2, -1], #0
                [ 0,  0, -2, -1], #1
                [ 0, -2, -2,  0], #2
                [-2,  0,  0, -2], #3
                [ 0,  0,  0, -2], #4
                [ 0, -2,  0, -2]]).astype("float32")


# In[4]:


path = FindPath(3, 0, [2,3], env)


# In[5]:


print path

