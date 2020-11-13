
# coding: utf-8

# In[ ]:


import numpy as np
import random


# In[ ]:


#column 0 = left
#column 1 = right
#column 2 = up
#column 3 = down
# ------------- L   R   U   D ------------- #
R = np.array([[-2,  0, -2, -1], #0
              [ 0,  0, -2, -1], #1
              [ 0, -2, -2,  0], #2
              [-2,  0,  0, -2], #3
              [100, 0,  0, -2], #4
              [ 0, -2,  0, -2]]).astype("float32")
Q = np.zeros_like(R)


# In[ ]:


gamma = 0.8
goal = 3
size_grid = [2,3]

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


# In[ ]:


Q


# In[ ]:


R_new = np.array([[-2,  0, -2,  0], #0
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

Q_new = np.zeros_like(R_new)


# In[ ]:


goal = 3
new_size_grid = [5,7]
init_state = 0


# In[ ]:


path_full = []
current_state = init_state
new_current_state = init_state    
path_full.append(init_state)


# In[ ]:


while (current_state != goal):
    action = np.argmax(Q[current_state,:])
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


# In[ ]:


print path_full


# In[ ]:




