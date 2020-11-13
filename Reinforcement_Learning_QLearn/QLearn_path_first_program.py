
# coding: utf-8

# In[1]:


import numpy as np
import random


# In[2]:


#column 0 = left
#column 1 = right
#column 2 = up
#column 3 = down
# ------------- L   R   U   D ------------- #
R = np.array([[-2,  0, -2, -1], #0
              [ 0,  0, -2, -1], #1
              [ 0,  0, -2,  0], #2
              [ 0, -2, -2,  0], #3
              [-2, -1,  0, -1], #4
              [-1,  0,  0,  0], #5
              [-1,  0,  0,  0], #6
              [ 0, -2,  0, -1], #7 
              [-2,  0, -1,  0], #8
              [100, 0, -1,  0], #9
              [ 0, -1,  0,  0], #10
              [ 0, -2,  0, -1], #11
              [-2,  0, 100,-2], #12
              [ 0,  0,  0, -2], #13
              [ 0, -1,  0, -2], #14
              [ 0, -2, -1, -2]]).astype("float32")
Q = np.zeros_like(R)


# In[3]:


size_grid = [4,4]
gamma = 0.8
goal = 8

for _ in range(500):
    current_state = random.randint(0,len(R)-1)
    while (current_state!= goal):
    
        temp = np.asarray(np.where((R[current_state,:]!=-1) & (R[current_state,:]!=-2)))
        action = np.random.choice(temp[0,:])
    
        if (action==0):
            next_state = current_state - 1
        elif (action==1):
            next_state = current_state + 1
        elif (action==2):
            next_state = current_state - size_grid[1]
        elif (action==3):
            next_state = current_state + size_grid[1]

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
            next_state = current_state - size_grid[1]
        elif (action==3):
            next_state = current_state + size_grid[1]
        
        current_state = next_state
    
        print current_state
    print


# In[ ]:




