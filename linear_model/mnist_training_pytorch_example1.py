#Author: Suryansh Kumar, Australian National University
#Training neural network with 4 hidden layer on mnist dataset

import torch
from torchvision import datasets, transforms
from torch.autograd import Variable

#Step1: Design the model using class and variables
#Step2: Construct loss and choice of optimizer
#Step3: Train the model using 4 basic sub-rules
#	3.1 forward pass
#   3.2 compute loss
#	3.3 backward pass
#	3.4 update the parameters

##Load the data and divide into batches
# set the training batch size
batch_size = 64

# MNIST Dataset
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

## Step1: Design the neural network model with 1 input, 4 hidden layer, 1 output
## The input is 784 (28x28)
## First hidden layer  (520x320) -input to output
## Second hidden layer (320x240) -input to output
## Third hidden layer  (240x120) -input to output
## Forth hidden layer  (120x10)  -input to output
## The output is 10x1 vector

class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        #create linear layer model with four hidden layers
        self.l1 = torch.nn.Linear(784, 520)
        self.l2 = torch.nn.Linear(520, 320)
        self.l3 = torch.nn.Linear(320, 240)
        self.l4 = torch.nn.Linear(240, 120)
        self.l5 = torch.nn.Linear(120, 10)
    def forward(self, input):
        input = input.view(-1, 784) #make it a vector 28x28
        input = torch.nn.functional.relu(self.l1(input))
        input = torch.nn.functional.relu(self.l2(input))
        input = torch.nn.functional.relu(self.l3(input))
        input = torch.nn.functional.relu(self.l4(input))
        return self.l5(input)

model = Model()

## Step2 : Construct the loss and choose the optimizer
lossFunc = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01, momentum=0.5)


#Step3: Training the model 1. forward pass 2. compute loss 3. backward, 4. update

def training(epoch):
    model.train() #set the module in the training mode
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = Variable(data), Variable(target)
        #1. forward pass
        output = model(data)
        #2. compute loss
        loss = lossFunc(output, target)
        #3. backward pass
        optimizer.zero_grad()
        loss.backward()
        #4. update the parameters
        optimizer.step()
        #estimate the train error
        if batch_idx % 10 == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                100. * batch_idx / len(train_loader), loss.data[0]))

#this part is inspired from the materials available online (pytorch)
def test():
    model.eval()
    test_loss = 0
    correct = 0
    for data, target in test_loader:
        data, target = Variable(data, volatile=True), Variable(target)
        output = model(data)
        # sum up batch loss
        test_loss += lossFunc(output, target).data[0]
        # get the index of the max
        pred = output.data.max(1, keepdim=True)[1]
        correct += pred.eq(target.data.view_as(pred)).cpu().sum()

    test_loss /= len(test_loader.dataset)
    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        test_loss, correct, len(test_loader.dataset),
        100.* correct / len(test_loader.dataset)))

#train the model for 10 epoch
for epoch in range(1, 10):
    training(epoch)
#test the model
test()
