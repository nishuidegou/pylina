"""
Input -> CONV -> ReLU -> Pool -> Fully Connected Layer

INPUT [32x32x3] will hold the raw pixel values of the image, in this case an image of width 32, height 32, and with three color channels R,G,B.
CONV layer will compute the output of neurons that are connected to local regions in the input, each computing a dot product between their weights and a small region they are connected to in the input volume. This may result in volume such as [32x32x12] if we decided to use 12 filters.
RELU layer will apply an elementwise activation function, such as the max(0,x)max(0,x) thresholding at zero. This leaves the size of the volume unchanged ([32x32x12]).
POOL layer will perform a downsampling operation along the spatial dimensions (width, height), resulting in volume such as [16x16x12].
FC (i.e. fully-connected) layer will compute the class scores, resulting in volume of size [1x1x10], where each of the 10 numbers correspond to a class score, such as among the 10 categories of CIFAR-10. As with ordinary Neural Networks and as the name implies, each neuron in this layer will be connected to all the numbers in the previous volume.


"""
import numpy as np


def net_forward():
    pass



def net_backward():
    pass



class Neuron(object):
  # ...
  def forward(self, inputs):
    """ assume inputs and weights are 1-D numpy arrays and bias is a number """
    cell_body_sum = np.sum(inputs * self.weights) + self.bias
    firing_rate = 1.0 / (1.0 + math.exp(-cell_body_sum)) # sigmoid activation function
    return firing_rate


# # forward-pass of a 3-layer neural network:
# f = lambda x: 1.0/(1.0 + np.exp(-x)) # activation function (use sigmoid)
# x = np.random.randn(3, 1) # random input vector of three numbers (3x1)
# h1 = f(np.dot(W1, x) + b1) # calculate first hidden layer activations (4x1)
# h2 = f(np.dot(W2, h1) + b2) # calculate second hidden layer activations (4x1)
# out = np.dot(W3, h2) + b3 # output neuron (1x1)


