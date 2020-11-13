
# coding: utf-8

# In[1]:


import resource


# In[2]:


resource.getrusage(resource.RUSAGE_SELF).ru_maxrss


# In[3]:


import numpy as np
import random
import time


# In[4]:


from QLearn_functions import FindPath


# In[5]:


#column 0 = left
#column 1 = right
#column 2 = up
#column 3 = down
# ------------------- L   R   U   D ------------------- #
env_new = np.array([[-2, -1, -2,  0], #0
                    [ 0,  0, -2,  0], #1
                    [ 0,  0, -2,  0], #2
                    [ 0, -2, -2,  0], #3
                    [-2,  0,  0, -1], #4
                    [ 0, -1,  0, -1], #5
                    [ 0,  0,  0,  0], #6
                    [ 0, -2,  0,  0], #7 
                    [-2,  0,  0,  0], #8
                    [ 0,  0,  0,  0], #9
                    [ 0,  0,  0,  0], #10
                    [ 0, -2,  0,  0], #11
                    [-2,  0,  0, -2], #12
                    [ 0,  0,  0, -2], #13
                    [ 0,  0,  0, -2], #14
                    [ 0, -2,  0, -2]]).astype("float32")


# In[6]:


time_start = time.clock()
path = FindPath(8, 0, [4,4], env_new)  #FindPath(Goal, state, size_of_grid, environment_table)
print resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
path


# In[7]:


time_elapsed = (time.clock() - time_start)
time_elapsed

