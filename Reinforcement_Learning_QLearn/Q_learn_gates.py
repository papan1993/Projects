
# coding: utf-8
# link to the question :
# http://mnemstudio.org/path-finding-q-learning-tutorial.htm
# In[1]:


import numpy as np
import random


# In[2]:


#reward matrix
R = np.array([[-1, -1, -1, -1,  0,  -1],
              [-1, -1, -1,  0, -1, 100],
              [-1, -1, -1,  0, -1,  -1],
              [-1,  0,  0, -1,  0,  -1],
              [ 0, -1, -1,  0, -1, 100],
              [-1,  0, -1, -1,  0, 100]]).astype("float32")

#initializing Q matrix
Q = np.zeros_like(R) 


# In[3]:


gamma = 0.8
goal = 5

for _ in range(100):
    current_state = random.randint(0,5)
    while (current_state!= goal):

        next_state = np.random.choice(np.asarray(np.where(R[current_state,:]!=-1))[0,:])    
        Q[current_state,next_state] = R[current_state, next_state] + (gamma * Q[next_state, :].max())

        current_state = next_state

       # print current_state
       # print Q


# In[4]:


print Q


# In[5]:


goal = 5
for current_state in range(len(Q)):
    print current_state
    while (current_state!= goal):
        next_state = np.argmax(Q[current_state,:])
        current_state = next_state
    
        print current_state
    print

