
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
              [ 0, -2, -2,  0], #1
              [-2,  0,  0, -2], #2
              [100,-2,  0, -2]]).astype("float32")
Q = np.zeros_like(R)


# In[3]:


gamma = 0.8
goal = 2
size_grid = [2,2]

for _ in range(500):
    current_state = random.randint(0,len(R)-1)
    while (current_state!= goal):
    
        action = np.random.choice(np.asarray(np.where((R[current_state,:]!=-1) & (R[current_state,:]!=-2)))[0,:])
    
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


R_new = np.array([[-2, -1, -2,  0], #0
                  [ 0,  0, -2,  0], #1
                  [ 0,  0, -2,  0], #2
                  [ 0, -2, -2,  0], #3
                  [-2,  0,  0,  0], #4
                  [ 0, -1,  0,  0], #5
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

Q_new = np.zeros_like(R_new)


# In[6]:


goal = 2
new_size_grid = [4,4]
init_state = 0


# In[7]:


path_full = []
current_state = init_state
new_current_state = init_state    
path_full.append(init_state)


# In[9]:


def Action(q_matrix, current_step):
    return np.argmax(q_matrix[current_state,:])


# In[10]:


while (current_state != goal):
    action = Action(Q, current_state)
    print "first while loop"
    if (action==0):
        current_state = current_state - 1
        new_next_state = new_current_state - int(new_size_grid[1]/size_grid[1])
        print "while -> if"
        while (new_current_state!=new_next_state):
            if ((R_new[new_current_state, action]!=-1) & (R_new[new_current_state, action]!=-2)):
                new_current_state = new_current_state -1 
                path_full.append(new_current_state)
                print "while -> if -> while -> if "
                    
            else:
                print "while -> if -> while -> else "
                for _ in range(100):
                    new_current_state_temp = new_current_state
                    while (new_current_state_temp!= new_next_state):
                        print "while -> if -> while -> else ->for -> while "    
                        action = np.random.choice(np.asarray(np.where((R_new[new_current_state_temp,:]!=-1) & (R_new[new_current_state_temp,:]!=-2)))[0,:])
    
                        if (action==0):
                            new_next_state_temp = new_current_state_temp - 1
                        elif (action==1):
                            new_next_state_temp = new_current_state_temp + 1
                        elif (action==2):
                            new_next_state_temp = new_current_state_temp - new_size_grid[1]
                        elif (action==3):
                            new_next_state_temp = new_current_state_temp + new_size_grid[1]
                            
                        if (new_next_state_temp == new_next_state):
                            R_new[new_current_state_temp, action] = 100
                            
                        Q_new[new_current_state_temp, action] = R_new[new_current_state_temp, action] + (gamma * Q_new[new_next_state_temp, :].max())
                        new_current_state_temp = new_next_state_temp
                    
                while (new_current_state != new_next_state):
                    print "while -> if -> while -> else -> while 2" 
                    action = np.argmax(Q_new[new_current_state,:])
        
                    if (action==0):
                        new_next_state_temp = new_current_state - 1
                    elif (action==1):
                        new_next_state_temp = new_current_state + 1
                    elif (action==2):
                        new_next_state_temp = new_current_state - new_size_grid[1]
                    elif (action==3):
                        new_next_state_temp = new_current_state + new_size_grid[1]
                        
                    new_current_state = new_next_state_temp
                    path_full.append(new_current_state)
                    
    
    elif (action==1):
        current_state = current_state + 1
        new_next_state = new_current_state + int(new_size_grid[1]/size_grid[1])
        print "while -> elif1"
        while (new_current_state!=new_next_state):
            if ((R_new[new_current_state, action]!=-1) & (R_new[new_current_state, action]!=-2)):
                new_current_state = new_current_state + 1 
                path_full.append(new_current_state)
                print "while -> elif1 -> while -> if "
                    
            else:
                print "while -> elif1 -> while -> else "
                for _ in range(100):
                    new_current_state_temp = new_current_state                        
                    while (new_current_state_temp!= new_next_state):
                        print "while -> elif1 -> while -> else ->for -> while "     
                        action_temp = np.random.choice(np.asarray(np.where((R_new[new_current_state_temp,:]!=-1) & (R_new[new_current_state_temp,:]!=-2)))[0,:])
    
                        if (action_temp==0):
                            new_next_state_temp = new_current_state_temp - 1
                        elif (action_temp==1):
                            new_next_state_temp = new_current_state_temp + 1
                        elif (action_temp==2):
                            new_next_state_temp = new_current_state_temp - new_size_grid[1]
                        elif (action_temp==3):
                            new_next_state_temp = new_current_state_temp + new_size_grid[1]
                            
                        if (new_next_state_temp == new_next_state):
                            R_new[new_current_state_temp, action_temp] = 100
                            
                        Q_new[new_current_state_temp, action_temp] = R_new[new_current_state_temp, action_temp] + (gamma * Q_new[new_next_state_temp, :].max())
                        new_current_state_temp = new_next_state_temp
                    
                while (new_current_state != new_next_state):
                    print "while -> elif1 -> while -> else -> while 2" 
                    action_temp = np.argmax(Q_new[new_current_state,:])
        
                    if (action_temp==0):
                        new_next_state_temp = new_current_state - 1
                    elif (action_temp==1):
                        new_next_state_temp = new_current_state + 1
                    elif (action_temp==2):
                        new_next_state_temp = new_current_state - new_size_grid[1]
                    elif (action_temp==3):
                        new_next_state_temp = new_current_state + new_size_grid[1]
                        
                    new_current_state = new_next_state_temp
                    path_full.append(new_current_state)
                    
                    
    elif (action==2):
        current_state = current_state - size_grid[1]
        new_next_state = new_current_state - (int(new_size_grid[0]/size_grid[0]) * new_size_grid[1])
        print "while -> elif2"
        while (new_current_state!=new_next_state):
            if ((R_new[new_current_state, action]!=-1) & (R_new[new_current_state, action]!=-2)):
                new_current_state = new_current_state - new_size_grid[1] 
                path_full.append(new_current_state)
                print "while -> elif2 -> while -> if "
                    
            else:
                print "while -> elif2 -> while -> else "
                for _ in range(100):
                    new_current_state_temp = new_current_state                        
                    while (new_current_state_temp!= new_next_state):
                        print "while -> elif2 -> while -> else ->for -> while "     
                        action_temp = np.random.choice(np.asarray(np.where((R_new[new_current_state_temp,:]!=-1) & (R_new[new_current_state_temp,:]!=-2)))[0,:])
    
                        if (action_temp==0):
                            new_next_state_temp = new_current_state_temp - 1
                        elif (action_temp==1):
                            new_next_state_temp = new_current_state_temp + 1
                        elif (action_temp==2):
                            new_next_state_temp = new_current_state_temp - new_size_grid[1]
                        elif (action_temp==3):
                            new_next_state_temp = new_current_state_temp + new_size_grid[1]
                            
                        if (new_next_state_temp == new_next_state):
                            R_new[new_current_state_temp, action_temp] = 100
                            
                        Q_new[new_current_state_temp, action_temp] = R_new[new_current_state_temp, action_temp] + (gamma * Q_new[new_next_state_temp, :].max())
                        new_current_state_temp = new_next_state_temp
                    
                while (new_current_state != new_next_state):
                    print "while -> elif2 -> while -> else -> while 2" 
                    action_temp = np.argmax(Q_new[new_current_state,:])
        
                    if (action_temp==0):
                        new_next_state_temp = new_current_state - 1
                    elif (action_temp==1):
                        new_next_state_temp = new_current_state + 1
                    elif (action_temp==2):
                        new_next_state_temp = new_current_state - new_size_grid[1]
                    elif (action_temp==3):
                        new_next_state_temp = new_current_state + new_size_grid[1]
                        
                    new_current_state = new_next_state_temp
                    path_full.append(new_current_state)
                    
                    
    elif (action==3):
        current_state = current_state + size_grid[1]
        new_next_state = new_current_state + (int(new_size_grid[0]/size_grid[0]) * new_size_grid[1])
        print "while -> elif3"
        while (new_current_state!=new_next_state):
            if ((R_new[new_current_state, action]!=-1) & (R_new[new_current_state, action]!=-2)):
                new_current_state = new_current_state + new_size_grid[1]
                path_full.append(new_current_state)
                print "while -> elif3 -> while -> if "
                    
            else:
                print "while -> elif3 -> while -> else "
                for _ in range(100):
                    new_current_state_temp = new_current_state                        
                    while (new_current_state_temp!= new_next_state):
                        print "while -> elif3 -> while -> else ->for -> while "     
                        action_temp = np.random.choice(np.asarray(np.where((R_new[new_current_state_temp,:]!=-1) & (R_new[new_current_state_temp,:]!=-2)))[0,:])
    
                        if (action_temp==0):
                            new_next_state_temp = new_current_state_temp - 1
                        elif (action_temp==1):
                            new_next_state_temp = new_current_state_temp + 1
                        elif (action_temp==2):
                            new_next_state_temp = new_current_state_temp - new_size_grid[1]
                        elif (action_temp==3):
                            new_next_state_temp = new_current_state_temp + new_size_grid[1]
                            
                        if (new_next_state_temp == new_next_state):
                            R_new[new_current_state_temp, action_temp] = 100
                            
                        Q_new[new_current_state_temp, action_temp] = R_new[new_current_state_temp, action_temp] + (gamma * Q_new[new_next_state_temp, :].max())
                        new_current_state_temp = new_next_state_temp
                    
                while (new_current_state != new_next_state):
                    print "while -> elif3 -> while -> else -> while 2" 
                    action_temp = np.argmax(Q_new[new_current_state,:])
        
                    if (action_temp==0):
                        new_next_state_temp = new_current_state - 1
                    elif (action_temp==1):
                        new_next_state_temp = new_current_state + 1
                    elif (action_temp==2):
                        new_next_state_temp = new_current_state - new_size_grid[1]
                    elif (action_temp==3):
                        new_next_state_temp = new_current_state + new_size_grid[1]
                        
                    new_current_state = new_next_state_temp
                    path_full.append(new_current_state)


# In[11]:


print path_full


# In[ ]:




