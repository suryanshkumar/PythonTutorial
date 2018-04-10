#Author: Suryansh Kumar, Australian National University
#To understand dataloader in more elementary way

import torch
import torch.nn.functional as F
from torchvision import datasets, transforms
from torch.autograd import Variable

##Load the data and divide into batches
##set the training batch size
batch_size = 64

#MNIST Dataset
train_dataset = datasets.MNIST(root='./mnist_data/',
                               train=True,
                               transform=transforms.ToTensor(),
                               download=True)

test_dataset = datasets.MNIST(root='./mnist_data/',
                              train=False,
                              transform=transforms.ToTensor())

# Data Loader
train_loader = torch.utils.data.DataLoader(dataset=train_dataset,
                                           batch_size=batch_size,
                                           shuffle=True)

test_loader = torch.utils.data.DataLoader(dataset=test_dataset,
                                          batch_size=batch_size,
                                          shuffle=False)

#now load the dataset
for batch_idx, (data, target) in enumerate(train_loader):
    data, target = Variable(data), Variable(target)
    #the first item is the batch number, the second is the size of the batch, third is the size of the target
    #batch_idx an integer
    #data is of the size [batch_size, channel, image_rows, image_cols]. In the mnist data its [64, 1, 28, 28]
    #the target is a vector of size equals to the size of the batch i.e., for each image what is the correct value
    #print(batch_idx, data.size(), target.size())

#Check the batch one by one
first_batch = next(iter(train_loader))
print(len(first_batch))     #the length is 2 (data, target)
print(len(first_batch[0]))  #the length is 64 as it contains 64 images each of size 1x28x28

first_batch_data = first_batch[0] #get the data for the first batch
print(first_batch_data[0]) #this is of the size 1x28x28

#if you want to convert this 28x28 data to a column vector
first_batch_data_vector = first_batch_data[0].view(784, 1)
print(first_batch_data_vector)

#if you want to convert this 28x28 data to a row vector
first_batch_data_vector = first_batch_data[0].view(1, 784)
print(first_batch_data_vector)
