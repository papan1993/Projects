
# coding: utf-8

# In[1]:


import numpy as np
import random


# In[2]:


# ------------- L   R   U   D ------------- #
R = np.array([[-1,  0, -1, -1], #0
              [ 0,  0, -1, -1], #1
              [ 0,  0, -1,  0], #2
              [ 0, -1, -1,  0], #3
              [-1, -1,  0, -1], #4
              [-1,  0,  0,  0], #5
              [-1,  0,  0,  0], #6
              [ 0, -1,  0, -1], #7 
              [-1,  0, -1,  0], #8
              [100, 0, -1,  0], #9
              [ 0, -1,  0,  0], #10
              [ 0, -1,  0, -1], #11
              [-1,  0, 100,-1], #12
              [ 0,  0,  0, -1], #13
              [ 0, -1,  0, -1], #14
              [ 0, -1, -1, -1]]).astype("float32")
Q = np.zeros_like(R)


# In[3]:


gamma = 0.8
goal = 8

for _ in range(500):
    current_state = random.randint(0,15)
    while (current_state!= goal):
    
        temp = np.asarray(np.where(((R[current_state,:]!=-1) * 1)==1))
        action = np.random.choice(temp[0,:])
    
        if (action==0):
            next_state = current_state - 1
        elif (action==1):
            next_state = current_state + 1
        elif (action==2):
            next_state = current_state - Q.shape[1]
        elif (action==3):
            next_state = current_state + Q.shape[1]

        Q[current_state, action] = R[current_state, action] + (gamma * Q[next_state, :].max())

        current_state = next_state
        
       # print current_state
       # print Q


# In[4]:


Q


# In[5]:


goal = 8
for current_state in range(len(Q)):    
    print current_state
    
    while (current_state!= goal):
        action = np.argmax(Q[current_state,:])
        
        if (action==0):
            next_state = current_state - 1
        elif (action==1):
            next_state = current_state + 1
        elif (action==2):
            next_state = current_state - Q.shape[1]
        elif (action==3):
            next_state = current_state + Q.shape[1]
        
        current_state = next_state
    
        print current_state
    print

