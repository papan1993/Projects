
# coding: utf-8

# In[1]:


import resource


# In[2]:


#Memory usage (in bytes) before running program
resource.getrusage(resource.RUSAGE_SELF).ru_maxrss


# In[4]:


import numpy
import matplotlib.pyplot as plt
import pandas
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error

import time


# In[5]:


#Reading data
dataframe = pandas.read_csv('RNN_data.csv', usecols=[1], engine='python')
dataset = dataframe.values
dataset = dataset.astype('float32')


# In[6]:


#Normalize the data
scaler = MinMaxScaler(feature_range=(0, 1))
dataset = scaler.fit_transform(dataset)


# In[7]:


#Train, Test set Split
train_size = int(len(dataset) * 0.7)
test_size = len(dataset) - train_size
train, test = dataset[0:train_size,:], dataset[train_size:len(dataset),:]
print(len(train), len(test))


# In[8]:


#Function to generate time series data matrix from given data
def create_dataset(dataset, look_back=1):
    dataX, dataY = [], []
    for i in range(len(dataset)-look_back-1):
        a = dataset[i:(i+look_back), 0]
        dataX.append(a)
        dataY.append(dataset[i + look_back, 0])
    return numpy.array(dataX), numpy.array(dataY)


# In[9]:


#reshape into X=t and Y=t+1 using create_dataset function defined above
look_back = 2
trainX, trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test, look_back)


# In[10]:


#LSTM Sequential model takes input in form of [samples, time steps, features]
#so reshape input to [samples, time steps, features]
trainX = numpy.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
testX = numpy.reshape(testX, (testX.shape[0], 1, testX.shape[1]))


# In[11]:


time_start = time.clock()
#Sequential Model from Keras library used
model = Sequential()

#add LSTM layer and a regular densely-connected NN layer
model.add(LSTM(25, input_shape=(1, look_back)))
model.add(Dense(1))

#Compile, set optimizer to adam and then fit the training data
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(trainX, trainY, epochs=200, batch_size=1, verbose=2)


# In[12]:


#Predicting for test set & train set and calculating loss 
trainPredict = model.predict(trainX)
testPredict = model.predict(testX)

#inverting predictions before calculating error so that performance is reported in the same units as the original data
#reverse of normalizing
trainPredict = scaler.inverse_transform(trainPredict)
trainY = scaler.inverse_transform([trainY])
testPredict = scaler.inverse_transform(testPredict)
testY = scaler.inverse_transform([testY])

#calculating root mean squared error
trainScore = math.sqrt(mean_squared_error(trainY[0], trainPredict[:,0]))
print('Train Score: %.2f RMSE' % (trainScore))
testScore = math.sqrt(mean_squared_error(testY[0], testPredict[:,0]))
print('Test Score: %.2f RMSE' % (testScore))


# In[13]:


#time taken by the whole process
time_elapsed = (time.clock() - time_start)
time_elapsed


# In[17]:


#Shifting axis for plotting
trainPredictPlot = numpy.empty_like(dataset)
trainPredictPlot[:, :] = numpy.nan
trainPredictPlot[0:len(trainPredict), :] = trainPredict

testPredictPlot = numpy.empty_like(dataset)
testPredictPlot[:, :] = numpy.nan
testPredictPlot[len(trainPredict)+(look_back)+1:len(dataset)-1-(look_back), :] = testPredict

#Plotting baseline and predictions
plt.plot(scaler.inverse_transform(dataset))
plt.plot(trainPredictPlot)
plt.plot(testPredictPlot)
plt.show()


# In[14]:


#Memory usage (in bytes) after running program
resource.getrusage(resource.RUSAGE_SELF).ru_maxrss


# In[15]:


min(trainPredict)


# In[16]:


max(trainPredict)

