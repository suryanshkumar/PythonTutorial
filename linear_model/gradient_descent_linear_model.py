#Author: Suryansh Kumar, Australian National University

#Example to find optimal w using gradient descent algorithm
#I am using the linear model example to make it coherent and easy to follow.


#import the necessary library
import numpy as np
import matplotlib.pyplot as plt

#set the input data
x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]

#function to make a prediction
def prediction(x, w):
    return np.dot(w, x)

#function to calculate the loss
def loss(x, y, w):
    y_predict = prediction(x, w)
    error = np.dot(y-y_predict, y-y_predict)
    return error

#function to estimate the gradient w.r.t to w. i.e argmin_w (x*w-y)^2
def gradient(x, y, w):
    grad = 2*np.dot((np.dot(w, x)-y), np.transpose(x))
    return grad

#estimate the error for different values of slope (w) and store it in the list
w_set = []
e_set = []

#leaning rate
eta = 0.01

#total number of sample
N = np.size(x_data)

#to find the optimal w, start with some guess on w say 1.0
w = 1.0


for iter in range(100):
    er = loss(x_data, y_data, w)
    er = er/N
    gr = gradient(x_data, y_data, w)
    w = w-eta*gr
    if(er<1e-12):
        break
    w_set.append(w)
    e_set.append(er)

print("optimal w = ", w, "loss=", er, "number of iteration = ",iter)

#plot the convergence curve.
#The red colored star provides an intution on the step length and how step length reduces
#as the algorithm approaches near to the local optimal value (global in case of convex function).
plt.plot(w_set, e_set, 'r-*')
plt.xlabel('w (slope of the line)')
plt.ylabel('Loss function')
plt.title('Convergence Curve')
plt.grid()
plt.show()
