
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
from QLearn_functions import PathScaler


# In[5]:


#column 0 = left
#column 1 = right
#column 2 = up
#column 3 = down
# --------------- L   R   U   D --------------- #
env = np.array([[-2,  0, -2, -1], #0
                [ 0,  0, -2, -1], #1
                [ 0, -2, -2,  0], #2
                [-2,  0,  0, -2], #3
                [ 0,  0,  0, -2], #4
                [ 0, -2,  0, -2]]).astype("float32")
#environment table


# In[6]:


env_new = np.array([[-2,  0, -2,  0], #0
                    [ 0, -1, -2,  0], #1
                    [ 0,  0, -2,  0], #2
                    [ 0,  0, -2,  0], #3
                    [ 0,  0, -2,  0], #4
                    [ 0,  0, -2,  0], #5
                    [ 0, -2, -2,  0], #6
                    [-2,  0,  0,  0], #7 
                    [ 0,  0,  0,  0], #8
                    [ 0,  0,  0,  0], #9
                    [ 0,  0,  0,  0], #10
                    [ 0,  0,  0,  0], #11
                    [ 0,  0,  0,  0], #12
                    [ 0, -2,  0,  0], #13
                    [-2,  0,  0,  0], #14
                    [ 0,  0,  0,  0], #15
                    [ 0,  0,  0,  0], #16
                    [ 0,  0,  0,  0], #17
                    [ 0,  0,  0,  0], #18
                    [ 0,  0,  0,  0], #19
                    [ 0, -2,  0,  0], #20
                    [-2,  0,  0,  0], #21
                    [ 0,  0,  0,  0], #22
                    [ 0,  0,  0,  0], #23
                    [ 0,  0,  0,  0], #24
                    [ 0,  0,  0,  0], #25
                    [ 0,  0,  0,  0], #26
                    [ 0, -2,  0,  0], #27
                    [-2,  0,  0, -2], #28
                    [ 0,  0,  0, -2], #29
                    [ 0,  0,  0, -2], #30
                    [ 0,  0,  0, -2], #31
                    [ 0,  0,  0, -2], #32
                    [ 0,  0,  0, -2], #33
                    [ 0, -2,  0, -2]]).astype("float32")


# In[7]:


time_start = time.clock()
path = FindPath(3, 0, [2,3], env)
print resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
path


# In[8]:


PathScaler(path, [2,3], [5,7], env_new)


# In[9]:


time_elapsed = (time.clock() - time_start)
time_elapsed

