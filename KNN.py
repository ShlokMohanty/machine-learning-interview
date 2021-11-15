import numpy as np 
import matplotlib.pyplot as plt 
data = np.load("/datasets/mnist_train_small.npy") //storing a numpy array into a file 
data 

/* array([[5,0,0,........,0,0,0],
          [7,0,0,......,0,0,0],
          [9,0,0,......,0,0,0],
          .....,
          [2,0,0.......,0,0,0],
          [9,0,0,.......,0,0,0],
          [5,0,0,........,0,0,0]], dtype=unit8)
*/
 //flattening of the image 
 x = data[:, 1:]
 y = data[:, 0]
 x.shape, y.shape
 plt.imshow(x[0].reshape(28,28), cmap=gray)
