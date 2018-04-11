#Author: Suryansh Kumar, Australian National University
#Rythm of making dataloader in in pytorch

import torch
import csv
import numpy as np
from torch.autograd import Variable
from torch.utils.data import Dataset, DataLoader

class csvDataset(Dataset):
    #arrange your dataset in __init__ such as reading and setting the variable
    def __init__(self):
        #1. read the file
        data = np.loadtxt("./csvData/yourfilename.csv", delimiter=',', dtype=np.float32)

        #2. separate the input and output
        rows = data.shape[0]
        cols = data.shape[1]

        #transform and assign the values
        self.input_data = torch.from_numpy(data[:, 0:-1])
        self.output_label = torch.from_numpy(data[:, [-1]]) #-1 means the right most column
        self.len = rows
    #return the value based on the index
    def __getitem__(self, index):
        return self.input_data[index], self.output_label[index]

    #return the total number of sample
    def __len__(self):
        return self.len

#instantiate the class
dataset = csvDataset()

#use the pytorch dataloader
train_loader = DataLoader(dataset=dataset, batch_size=32, shuffle=True)

#read the data from the train loader
for epoch in range(1):
    for i, data in enumerate(train_loader, 0):
        # get the inputs
        inputs, labels = data

        # wrap them in Variable
        inputs, labels = Variable(inputs), Variable(labels)

        # Run your training process
        print(epoch, i, "inputs", inputs.data, "labels", labels.data)
