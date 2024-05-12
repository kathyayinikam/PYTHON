#scatter plot
import numpy
import matplotlib.pyplot as plt
x=numpy.random.uniform(0.0,5.0,100)
y=numpy.random.uniform(1.0,20.0,100)
#plt.scatter(x,y)
#plt.show()
a=numpy.random.normal(5.0,1.0,1000)
b=numpy.random.normal(10.0,2.0,1000)
plt.scatter(a,b)# points concentrated near 5 and 10
plt.show()
