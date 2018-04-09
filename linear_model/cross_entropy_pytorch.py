#Author: Suryansh Kumar, Australian National University

#import the library
import torch
import numpy as np
from torch.autograd import Variable

#torch has inbuild function to calculate cross entropy
#It performs softmax internally
loss = torch.nn.CrossEntropyLoss()


#Given output Y, in this example it symbolizes the sample belongs to class 1
Y = Variable(torch.LongTensor([0]), requires_grad=False)

#predicted output without softmax
Y_hat1 = Variable(torch.Tensor([[3.0, 1.0, 1.5]]))
Y_hat2 = Variable(torch.Tensor([[1.0, 2.0, 0.5]]))


#calculate cross entropy loss due to first prediction
ce_l1 = loss(Y_hat1, Y)

#calculate cross entropy loss due to second prediction
ce_l2 = loss(Y_hat2, Y)

#print the values
print("cross entropy loss due to first prediction = ", ce_l1.data, "\n cross entropy loss due to second prediction = ", ce_l2.data)
