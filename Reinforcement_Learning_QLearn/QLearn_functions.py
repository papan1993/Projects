
# coding: utf-8

# In[1]:


import numpy as np
import random


# In[2]:


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


# In[3]:


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


# In[4]:


def FindAction(state, Q_table):
    return np.argmax(Q_table[state,:])


# In[5]:


def FindPath(Goal, state, size_of_grid, environment_table):   
    path = []
    path.append(state)
    Q_table = LearnTable(Goal, size_of_grid, environment_table)
    while (state!= Goal):
        action = FindAction(state, Q_table)
        state = Move(action, state, size_of_grid, environment_table)
        path.append(state)       
    return path


# In[6]:


def PathScaler(path_small, size_of_small, size_new):
    scaled_path = []
    new_current_state = path_small[0]
    scaled_path.append(new_current_state)
    
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
            if (action == 0):
                new_current_state = new_current_state - 1
            elif (action == 1):
                new_current_state = new_current_state + 1
            elif (action == 2):
                new_current_state = new_current_state - size_new[1]
            elif (action == 3):
                new_current_state = new_current_state + size_new[1]
            
            scaled_path.append(new_current_state)
                
    return scaled_path


# In[7]:


def PathMirrorVertical(path, size_of_grid):
    path_vertical_mirror = []
    for i in range(len(path)):
        multiplication_factor = int(path[i]/size_of_grid[1]) + 1
        state_vertical_mirror = (2 * multiplication_factor * size_of_grid[1]) - path[i] - size_of_grid[1] - 1
        path_vertical_mirror.append(state_vertical_mirror)
    return path_vertical_mirror


# In[8]:


def PathMirrorHorizontal(path, size_of_grid):
    path_horizontal_mirror = []
    for i in range(len(path)):        
        multiplication_factor = int(path[i]/size_of_grid[1])
        state_horizontal_mirror = ( (size_of_grid[0]-1) * size_of_grid[1] ) + path[i] - (2 * (multiplication_factor) * size_of_grid[1])         
        path_horizontal_mirror.append(state_horizontal_mirror)
    return path_horizontal_mirror


# In[ ]:


def PathMirrorDiagonal(path, size_of_grid):
    path_horizontal_mirror = PathMirrorHorizontal(path, size_of_grid)
    path_diagonal_mirror = PathMirrorVertical(path_horizontal_mirror, size_of_grid)
    return path_diagonal_mirror


# In[9]:


def FinalPath(path_temp, size_of_grid, environment):
    path_final = []
    new_current_state = path_temp[0]
    path_final.append(new_current_state)
    
    for i in range(len(path_temp)-1):
        step_change = path_temp[i+1] - path_temp[i]
        
        if (step_change == -1):
            action = 0
            next_state_new = new_current_state - 1
            
        elif (step_change == 1):
            action = 1
            next_state_new = new_current_state + 1 
            
        elif (step_change == -size_of_grid[1]):
            action = 2
            next_state_new = new_current_state - int(size_of_grid[1])  
            
        elif (step_change == size_of_grid[1]):
            action = 3
            next_state_new = new_current_state + int(size_of_grid[1])             
            
        while(new_current_state != next_state_new):
            next_step = Move(action, new_current_state, size_of_grid, environment)
            
            if (next_step==new_current_state):
                
                if (action == 0):
                    next_step = new_current_state - 1
                    
                elif (action == 1):
                    next_step = new_current_state + 1
                    
                elif (action == 2):
                    next_step = new_current_state - size_of_grid[1]
                    
                elif (action == 3):
                    next_step = new_current_state + size_of_grid[1]                    
                    
                temp_path = FindPath(next_step, new_current_state, size_of_grid, environment)
                path_final = path_final + temp_path[1:]
                new_current_state = next_step
                
            else:
                new_current_state = next_step
                path_final.append(new_current_state)
                
    return path_final

