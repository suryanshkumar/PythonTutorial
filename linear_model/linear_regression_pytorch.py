#Author: Suryansh Kumar, Australian National University

#In this example, we will perform linear regression using pytorch
#We will perform this task using three basic building block

#Step1: Design the model using class and variables
#Step2: Construct loss and choice of optimizer
#Step3: Train the model using 4 basic sub-rules
#	3.1 forward pass
#   3.2 compute loss
#	3.3 backward pass
#	3.4 update the parameters

#import the library

import torch
import numpy as np
from torch.autograd import Variable

#Step1: Design the model (here one input and one output linear model)
x_data = Variable(torch.Tensor([[2.0], [3.0], [4.0], [5.0]]), requires_grad= False)
y_data = Variable(torch.Tensor([[4.0], [6.0], [8.0], [10.0]]), requires_grad= False)

class Model(torch.nn.Module):
    #initialize the class
    def __init__(self):
        super(Model, self).__init__()
        #one 1 input and 1 output Model
        self.linear = torch.nn.Linear(1, 1)

    def forward(self, input):
        y_pred = self.linear(input)
        return y_pred

# instantiate the Model
model = Model()

#Step2 : Construct the loss and choose the optimizer
#here we choose the mean square error as loss and stochastic gradient descent as the optimizer
lossFunc  = torch.nn.MSELoss(size_average = False)
optimizer = torch.optim.SGD(model.parameters(), lr = 0.01) #pass the model parameters, and lr (the learning rate)


#Step3: Training the model 1. forward pass 2. compute loss 3. backward, 4. update

for epoch in range(1000):
    #1. forward_pass
    y_pred = model(x_data)

    #2. compute loss
    loss = lossFunc(y_pred, y_data)

    #3. backward pass
    optimizer.zero_grad() #reset the grad
    loss.backward()

    #4. update the parameters
    optimizer.step()

    #print the loss over epoch
    print(epoch, loss.data[0])

#print the parameter values
for parameters in model.parameters():
    if parameters.requires_grad:
        print(parameters.data[0])
