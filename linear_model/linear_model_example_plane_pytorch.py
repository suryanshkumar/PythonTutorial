#Author: Suryansh Kumar, Australian National University

#In this example, first we will generate data samples
#These data samples lies on a plane x + 2*y = z;
#The goal is to estimate the parameters (w1, w2) say (1, 2) in this example
#using backpropagation algorithm which makes use of computational graph

#import the necessary library
import numpy as np
import torch
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from torch.autograd import Variable

#set the input data
a = 1.0
b = 2.0
data = Variable(torch.Tensor([np.random.rand(10), np.random.rand(10)]), requires_grad= False)
train = a*data[0, :] + b*data[1, :]

#make w as a torch Variable (Important) initialized as [1, 1]
w = Variable(torch.Tensor([[1.0, 1.0]]), requires_grad = True)

#function to make a prediction
def prediction(x):
    return torch.mm(w, x)

#function to calculate the loss
def loss(x, y):
    y_predict = prediction(x)
    error = torch.dot(y-y_predict, y-y_predict)
    return error

#leaning rate
eta = 0.01

#to store the cost and parameters over iteration
e_set = []
w_set = []

#loop
for iter in range(1000):
    #for x, y in zip(x_data, y_data):
    er = loss(data, train)
    #automatically performs backpropagation and store the gradient in w.grad.data
    er.backward()
    #update the weight
    w.data = w.data - eta*w.grad.data
    #after weight update make grad as zero
    w.grad.data.zero_()
    #sum of Error
    mse_er = np.array(er.data)

    e_set.append(mse_er)
    w_set.append(np.array(w.data))


#print the optimal values
print("optimal w = ", w.data, "loss=", er.data, "number of iteration = ",iter)
