from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
import random as rd
data = np.loadtxt('train_MNIST.csv', dtype = str, delimiter = ',')

y = np.asarray(data[1:, 0:1], dtype='float')
X = np.asarray(data[1:,1:], dtype='float')

def add_ones(x):
 	a, b = np.shape(x)
	c = np.ones((a , 1))   
	return np.hstack((c, x))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.9)

def img(row, data):
	image = np.zeros((28,28))
	for i in range(0,28):
		for j in range(0,28):
			pix = 28*i+j
			image[i,j] = data[row, pix]
	plt.imshow(image, cmap = 'gray')
	plt.show()
	print data[row,0]

def create_weights(data):
	a, b = np.shape(data)
	weights = np.random.rand(b,1)
	return weights

weights = create_weights(X_train)

def predict(data_point, weights):
	b = np.dot(data_point, weights)
	a = b>0
	return a*1

def one_number(labels, number):
	return (labels == number)*1

def update(weights, data_point, labels, alpha=.1):
	predicted = predict(data_point, weights)
	weight_temp = np.zeros(np.shape(weights))
	weight_temp[:,0] = alpha*(labels-predicted)*data_point
	return weight_temp+weights

def train_perceptron(data, labels, weights, alpha = .001, iterations = 10):
	for j in range(0, iterations):
		for i in range(0, len(data)):
			weights = update(weights, data[i], labels[i], alpha)
	return weights

def test_perceptron_f(data, labels, weights):
    a,b = np.shape(data)
    predicted = predict(data, weights)
    correct = (predicted==labels)*1
    true_pos = np.sum((labels==1)*(correct))
    true_neg = np.sum((labels==0)*(correct))
    tp_p = true_pos/float(np.sum(labels))
    print np.sum(labels)
    tn_p = true_neg/float(a- np.sum(labels))
    return true_pos, true_neg, tp_p, tn_p, a

def all_numbers(data,labels):
	c,d = np.shape(data)
	w = create_weights(data)
	weights = []
	for i in range(0, 10):
		z = one_number(labels, i)
		a = train_perceptron(data, z, w, .001, 4)
		weights.append(a[:,0])
	return np.asarray(weights)

def one_all(data, weights):
	a = np.dot(data,np.transpose(weights))
	b = len(np.shape(data))
	if b == 1:
		return np.argmax(a)
	return np.argmax(a, axis=1)

def test_all(data, labels, weights):
	a, b = np.shape(labels)
	predicted = one_all(data, weights)
	correct = predicted == labels[:,0]
	accuracy = np.sum(correct)/float(a)
	return accuracy


####################################################################

import matplotlib.pyplot as plt

width = 0.3

p1 = plt.bar((1,1.7), (a,b), width, color = 'red')
p1 = plt.bar((1.3,2), (e, f), width, color = 'blue')
plt.ylabel('Number')
plt.title('Testing Since Perceptron')
plt.xticks((1,1.3, 1.7, 2), ('True Pos','Total Pos','True Neg', 'Total Neg'))
# plt.yticks(np.arange(0, 81, 10))
# plt.legend((p1[0], p2[0]), ('Men', 'Women'))

plt.show()

### Tuning

import matplotlib.pyplot as plt
lbls = one_number(y_train, 2)
lbls_t = one_number(y_test, 2)

alpha = []
t = .000007
for i in range(0,1):
    alpha.append(t)
    t = t/10.0
True_pos = []
True_neg = []
w = create_weights(X_train)
for a in alpha:
    weights = w
    print a
    temp_p = []
    temp_n = []
    for j in range(0,200):
        for k in range(0, len(X_train)):
            weights = update(weights, X_train[k], lbls[k], a)
        f,b,c,d,e,g = test_perceptron_f(X_test, lbls_t, weights)
        temp_p.append(c)
        temp_n.append(d)
    True_pos.append(temp_p)
    True_neg.append(temp_n)
    print temp_p

TP = np.asarray(True_pos)
TN = np.asarray(True_neg)

a,b = np.shape(TP)
print a, b


x = xrange(0, b)
a = 6
# plt.plot(x, TP[0,:])
plt.plot(x, TP[0,:])
plt.show()
print alpha[0]


def all_numbers(data,labels):
	c,d = np.shape(data)
	w = create_weights(data)
	weights = []
	for i in range(0,  len(np.unique(labels))):
		print i
		z = one_number(labels, i)
		a = train_perceptron(data, z, w, .000007, 200)
		weights.append(a[:,0])
	return np.asarray(weights)
In [75]:
w = all_numbers(X_train, y_train)

print test_all(X_test, y_test, w)



