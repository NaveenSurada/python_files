import numpy

##var = [1,2,3]
##print(var)
##print(type(var))

##var = numpy.array([1,2,3])
##print(var)
##print(type(var))

##var = numpy.array([[1,2,3],[4,5,6]])
##print(var)
##print(type(var))

##var = numpy.array([1,2,3],ndmin = 2)
##print(var)
##print(type(var))

##data_type = numpy.dtype(numpy.int32)
##print(data_type)

##data_type = numpy.dtype('i4')
##print(data_type)

##data = numpy.array([[2,3,4,8],[5,4,3]])
##print(data.shape)

##data= numpy.array([[2,3,4],[5,4,3]])
##print(data.shape)
##data1= data.reshape(3,2)
##print(data1)
##print(data1.shape)

##data= numpy.array([[2,3,4,5,6],[6,5,5,4,3]])
##print(data.shape)
##data1= data.reshape(5,2)
##print(data1)
##print(data1.shape)

##data= numpy.empty([3,2],dtype= int)
##print(data)

##data= numpy.zeros(5)
##print(data)

##data = numpy.zeros((2,2), dtype = numpy.int32)
##print(data)

##data = numpy.zeros((2,4), dtype = numpy.int32)
##print(data)

#broadcasting

##data = numpy.array([2,3,4,5])
##data1 = numpy.array([10,20,30,40])
##print(data*data1)

##data = numpy.array([[2,3,4,5],[1,2,3,4]])
##data1 = numpy.array([10,20,30,40])
##print(data*data1)

##data = numpy.array([2,3,4,5])
##data1 = numpy.array([10,20,30])   #it will not gonna run
##print(data*data1)

##data = numpy.array([2,3,4,5])
##data1 = numpy.array([10,20,30,40])
##print(data+data1)

##data = numpy.array([2,3,4,5])
##data1 = numpy.array([10,20,30,40])
##print(data-data1)

##data = numpy.array([2,4,3,5])
##data1 = numpy.array([10,20,30,40])
##print(data1/data)

##import pandas
##var=[2,4,6]
##data= pandas.DataFrame(var)
##print(data)
##print(data.sum(axis = 0))
##print(data.drop())

import pandas
var=[2,4,6]
data= pandas.DataFrame(var)
print(data)
print(data.sum(axis =1))
print(data.drop())
