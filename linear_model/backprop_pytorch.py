#Suryansh Kumar, Australian National University
#Example to find optimal w using backpropagation using computational graph way
#The only change is instead of using gradient function, we will use inbuild library to perform
#backpropagation using computational graph
#I am using pytorch library to achieve this.

#import the necessary library
import numpy as np
import torch
import matplotlib.pyplot as plt
from torch.autograd import Variable

#set the input data
x_data = Variable(torch.Tensor([1.0, 2.0, 3.0]), requires_grad= False)
y_data = Variable(torch.Tensor([2.0, 4.0, 6.0]), requires_grad= False)

#make w as a torch Variable (Important)
w = Variable(torch.Tensor([1.0]), requires_grad = True)


#function to make a prediction
def prediction(x):
    return w*x

#function to calculate the loss
def loss(x, y):
    y_predict = prediction(x)
    error = torch.dot(y-y_predict, y-y_predict)
    return error

#leaning rate
eta = 0.01

#total number of sample
N = np.size(x_data)

w_set = []
e_set = []

for iter in range(100):
    #for x, y in zip(x_data, y_data):
    er = loss(x_data, y_data)
    #automatically performs backpropagation and store the gradient in w.grad.data
    er.backward()
    #update the weight
    w.data = w.data - eta*w.grad.data
    #after weight update make grad as zero
    w.grad.data.zero_()
    #sum of Error
    mse_er = np.array(er.data)

    e_set.append(mse_er)
    w_set.append(w.data)

    if(mse_er<1e-10):
        break

#print the optimal values
print("optimal w = ", w.data, "loss=", er.data, "number of iteration = ",iter)
plt.plot(w_set, e_set, 'r-*')
plt.xlabel('w (slope of the line)')
plt.ylabel('Loss function')
plt.title('Convergence Curve')
plt.grid()
plt.show()
