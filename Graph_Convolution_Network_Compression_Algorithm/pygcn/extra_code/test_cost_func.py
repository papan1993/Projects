import numpy as np

def computeCost(X,y,theta):
    tobesummed = np.power(((X @ theta.T)-y),2)
    return np.sum(tobesummed)/(2 * len(X))

def gradientDescent(X,y,theta,iters,alpha):
    cost = np.zeros(iters)
    for i in range(iters):
        theta = theta - (alpha/len(X)) * np.sum(X * (X @ theta.T - y), axis=0)
        cost[i] = computeCost(X, y, theta)

    return theta,cost


#loss_train = loss_train.detach().numpy()
#acc_train = acc_train.numpy()

loss_train_data = [0.100, 3, 5, 3, 2, 12, 6]
acc_diff_data = [0.1000, 4, 2, 2, 1, 1, 3]

#set hyper parameters
alpha = 0.01
iters = 10
theta = 1e-5
theta = np.zeros(len(loss_train_data))

#globals()
g, cost = gradientDescent(loss_train_data, acc_diff_data, theta, iters, alpha)
#print(g)

finalCost = computeCost(loss_train_data, acc_diff_data, g)
print("final_cost----", finalCost)


import math

x = 1.923

decimal_pos = 2
tune_factor_1 = 0.65
tune_factor_2 = 2
val = (1 - tune_factor_1) - x
if val < 0:
    val = 0
max_v = 1
min_v = 0
b = 8
a = 1
new_val = (((b-a)*(val - min_v))/(max_v - min_v))+a
new_val = math.ceil(new_val)
if new_val < tune_factor_2:
    decimal_pos = 2
else:
    decimal_pos = new_val
