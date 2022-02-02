import numpy as np #numpy object instance
import matplotlib.pyplot as plt #for plotting


#linspace is a function that generates evenly split N numbers within the first 2 numbers you provide (first, last, N)
numline_x = np.linspace(0,2*np.pi,1000)
numline_y = np.sin(numline_x)
print(numline_x)
print("Y")
print(numline_y)
plt.plot(numline_x,numline_y)
plt.show()