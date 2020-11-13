
# coding: utf-8

# In[1]:


import numpy as np
import random


# In[2]:


from QLearn_functions import FindPath
from QLearn_functions import PathScaler
from QLearn_functions import PathMirrorVertical
from QLearn_functions import PathMirrorHorizontal
from QLearn_functions import PathMirrorDiagonal
from QLearn_functions import FinalPath


# In[3]:


#column 0 = left
#column 1 = right
#column 2 = up
#column 3 = down
# --------------- L   R   U   D --------------- #
env = np.array([[-2,  0, -2, -1], #0
                [ 0, -2, -2,  0], #1
                [-2,  0,  0, -2], #2
                [ 0, -2,  0, -2]]).astype("float32")
#environment table


# In[4]:


#column 0 = left
#column 1 = right
#column 2 = up
#column 3 = down
# ------------------- L   R   U   D -------------- #
env_new = np.array([[-2, -1, -2,  0], #0
                    [ 0,  0, -2,  0], #1
                    [ 0,  0, -2,  0], #2
                    [ 0, -2, -2,  0], #3
                    [-2,  0,  0, -1], #4
                    [ 0,  0,  0, -1], #5
                    [ 0,  0,  0,  0], #6
                    [ 0, -2,  0,  0], #7 
                    [-2,  0,  0,  0], #8
                    [ 0,  0,  0,  0], #9
                    [ 0,  0,  0,  0], #10
                    [ 0, -2,  0,  0], #11
                    [-2,  0,  0, -2], #12
                    [ 0,  0, -1, -2], #13
                    [ 0,  0,  0, -2], #14
                    [ 0, -2,  0, -2]]).astype("float32")


# In[5]:


small_path = FindPath(2, 0, [2,2], env) #FindPath(Goal, state, size_of_grid, environment_table)
print "Path of Small Grid ",small_path


# In[6]:


diagonal_mirror_small_path = PathMirrorDiagonal(small_path, [2,2])  #PathMirrorDiagonal(path, size_of_grid)
print "Diagonal Mirror small path ", diagonal_mirror_small_path


# In[7]:


path_scalled = PathScaler(small_path, [2,2], [4,4])  #PathScaler(path_small, size_of_small, size_new)
print "Predicted Scalled Path of Small Grid ", path_scalled


# In[8]:


final_path_scalled = FinalPath(path_scalled, [4,4], env_new) #FinalPath(path_temp, size_of_grid, environment)
print "Actual Path of Predicted scalled ", final_path_scalled


# In[9]:


################# VERTICAL MIRROR #################


# In[10]:


path_mirrored_vertical = PathMirrorVertical(path_scalled, [4,4])  #PathMirrorVertical(path, size_of_grid)
print "Mirror Of Predicted scalled path ", path_mirrored_vertical


# In[11]:


path_mirrored_vertical_scalled = PathMirrorVertical(final_path_scalled, [4,4]) #PathMirrorVertical(path, size_of_grid)
print "Mirror of Actual Scalled Path ", path_mirrored_vertical_scalled


# In[12]:


final_path_mirrored_vertical = FinalPath(path_mirrored_vertical, [4,4], env_new)  #FinalPath(path_temp, size_of_grid, environment)
print "Actual of Mirror of Predicted scalled ", final_path_mirrored_vertical


# In[13]:


final_path_mirrored_vertical_scalled = FinalPath(path_mirrored_vertical_scalled, [4,4], env_new) #FinalPath(path_temp, size_of_grid, environment)
print "Actual of 'Mirror of actual of Predicted scalled' ", final_path_mirrored_vertical_scalled


# In[14]:


################# HORIZONTAL MIRROR #################


# In[15]:


path_mirrored_horizontal = PathMirrorHorizontal(path_scalled, [4,4])  #PathMirrorVertical(path, size_of_grid)
print "Mirror Of Predicted scalled path ", path_mirrored_horizontal


# In[16]:


path_mirrored_horizontal_scalled = PathMirrorHorizontal(final_path_scalled, [4,4]) #PathMirrorVertical(path, size_of_grid)
print "Mirror of Actual Scalled Path ", path_mirrored_horizontal_scalled


# In[17]:


final_path_mirrored_horizontal = FinalPath(path_mirrored_horizontal, [4,4], env_new)  #FinalPath(path_temp, size_of_grid, environment)
print "Actual of Mirror of Predicted scalled ", final_path_mirrored_horizontal


# In[18]:


final_path_mirrored_horizontal_scalled = FinalPath(path_mirrored_horizontal_scalled, [4,4], env_new) #FinalPath(path_temp, size_of_grid, environment)
print "Actual of 'Mirror of actual of Predicted scalled' ", final_path_mirrored_horizontal_scalled


# In[19]:


################# DIAGONAL MIRROR #################


# In[20]:


diagonal_mirror_Predicted_Scalled = PathMirrorDiagonal(path_scalled, [4,4])   #PathMirrorDiagonal(path, size_of_grid)
print "Diagonal Mirror Predicted Scalled ", diagonal_mirror_Predicted_Scalled


# In[21]:


diagonal_mirror_actual_Scalled = PathMirrorDiagonal(final_path_scalled, [4,4])   #PathMirrorDiagonal(path, size_of_grid)
print "Diagonal Mirror actual Scalled ", diagonal_mirror_actual_Scalled


# In[22]:


final_path_diagonal_mirror = FinalPath(diagonal_mirror_actual_Scalled, [4,4], env_new) #FinalPath(path_temp, size_of_grid, environment)
print "Actual Path of 'Diagonal Mirror actual' ", final_path_diagonal_mirror

