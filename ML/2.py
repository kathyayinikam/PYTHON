from scipy import stats
import numpy
speed=[99,86,88,111,103,87,94,94,94,78,77,85,86]
x=numpy.mean(speed)
y=numpy.median(speed)
z=stats.mode(speed)
a=numpy.std(speed)
var=numpy.var(speed)
print(x)
print(y)
print(z)
print("Standard deviation=",a)
print("Variance=",var)
