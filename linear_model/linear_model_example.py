#Author: Suryansh Kumar
#Example to linearly model 2D dataset (x(input), y(output)).

#import the necessary library
import numpy as np
import matplotlib.pyplot as plt

#set the input data
x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]

#function to make a prediction
def prediction(x, w):
    return x*w

#function to calculate the loss
def loss(x, y, w):
    y_predict = prediction(x, w)
    error = (y-y_predict)*(y-y_predict)
    return error

#estimate the error for different values of slope (w) and store it in the list
w_set = []
e_set = []
N = np.size(x_data)

#loop through the different values of w's
for w in np.arange(-1.0, 5, 0.1):
    mse_iter = 0.0
    for x, y in zip(x_data, y_data):
        mse_iter = mse_iter + loss(x, y, w)
    e_set.append(mse_iter/N)
    w_set.append(w)

#plot the error curve.
plt.plot(w_set, e_set, 'r-')
plt.xlabel('w (slope of line)')
plt.ylabel('mean square error')
plt.title('Mean Squared Error Curve')
plt.grid()
plt.show()
