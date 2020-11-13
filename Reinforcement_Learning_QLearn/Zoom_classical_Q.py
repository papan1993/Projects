
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
env = np.array([[-2,  0, -2, -1], #0
                [ 0, -2, -2,  0], #1
                [-2,  0,  0, -2], #2
                [ 0, -2,  0, -2]]).astype("float32")
#environment table


# In[3]:


def LearnTable(Goal, size_of_grid, environment_table):
    epoch = 100
    Gamma = 0.8
    Q_value_table = np.zeros_like(environment_table)
    for _ in range(epoch):
        current_state = random.randint(0,Q_value_table.shape[0]-1)
        while (current_state!= Goal):       
            action = random.randint(0,Q_value_table.shape[1]-1)       
            next_state = Move(action, current_state, size_of_grid, environment_table)
        
            if (next_state==Goal):
                Q_value_table[current_state, action] = 100 + (Gamma * Q_value_table[next_state, :].max())

            elif (next_state == current_state):
                Q_value_table[current_state, action] = -1 + (Gamma * Q_value_table[next_state, :].max())
        
            else:
                Q_value_table[current_state, action] = 0 + (Gamma * Q_value_table[next_state, :].max())

            current_state = next_state
    return Q_value_table


# In[4]:


def Move(Action, cur_state, size_of_grid, environment_table):
    if ( (environment_table[cur_state, Action] != -1) & (environment_table[cur_state, Action] != -2) ):
    
        if (Action==0):
            next_state = cur_state - 1
        elif (Action==1):
            next_state = cur_state + 1
        elif (Action==2):
            next_state = cur_state - size_of_grid[1]
        elif (Action==3):
            next_state = cur_state + size_of_grid[1]
    else:
        next_state = cur_state
    
    return next_state


# In[5]:


def FindAction(state, Q_table):
    return np.argmax(Q_table[state,:])


# In[6]:


def FindPath(Goal, state, size_of_grid, environment_table):   
    path = []
    path.append(state)
    Q_table = LearnTable(Goal, size_of_grid, environment_table)
    while (state!= Goal):
        action = FindAction(state, Q_table)
        
        if (action==0):
            next_state = state - 1
        elif (action==1):
            next_state = state + 1
        elif (action==2):
            next_state = state - size_of_grid[1]
        elif (action==3):
            next_state = state + size_of_grid[1]       
        
        state = next_state
        path.append(state)       
    return path


# In[7]:


path = FindPath(2, 0, [2,2], env)
path


# In[8]:


env_new = np.array([[-2, -1, -2,  0], #0
                    [ 0,  0, -2,  0], #1
                    [ 0,  0, -2,  0], #2
                    [ 0, -2, -2,  0], #3
                    [-2,  0,  0,  0], #4
                    [ 0,  0,  0,  0], #5
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


# In[9]:


def PathScaler(path_small, size_of_small, size_new, environment_new):
    print "func start"
    path_new_grid = []
    new_current_state = path_small[0]
    path_new_grid.append(new_current_state)
    
    for i in range(len(path_small)-1):
        step_change = path_small[i+1] - path_small[i]
        
        if (step_change == -1):
            action = 0
            next_state_new = new_current_state - int(size_new[1]/size_of_small[1])           
        elif (step_change == 1):
            action = 1
            next_state_new = new_current_state + int(size_new[1]/size_of_small[1])           
        elif (step_change == -size_of_small[1]):
            action = 2
            next_state_new = new_current_state - (int(size_new[0]/size_of_small[0]) * size_new[1])           
        elif (step_change == size_of_small[1]):
            action = 3
            next_state_new = new_current_state + (int(size_new[0]/size_of_small[0]) * size_new[1])       
            
        while(new_current_state != next_state_new):
            next_step = Move(action, new_current_state, size_new, environment_new)
            
            if (next_step==new_current_state):
                if (action == 0):
                    next_step = new_current_state - 1
                elif (action == 1):
                    next_step = new_current_state + 1
                elif (action == 2):
                    next_step = new_current_state - size_new[1]
                elif (action == 3):
                    next_step = new_current_state + size_new[1]
                
                temp_path = FindPath(next_step, new_current_state, size_new, environment_new)
                path_new_grid = path_new_grid + temp_path[1:]
                new_current_state = next_step
            else:
                new_current_state = next_step
                path_new_grid.append(new_current_state)
                
    return path_new_grid      


# In[10]:


PathScaler(path, [2,2], [4,4], env_new)

