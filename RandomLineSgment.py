import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations
import itertools
from shapely.geometry import LineString, MultiLineString, MultiPoint, Point, box
import scipy.stats as stats
#points = np.zeros((4,2))
#print points

#points[:,0] = np.random.randint(10,size = 4)
#points[:,1] = np.random.randint(10,size = 4)
#x, y = np.random.random(size=(2,20))

mu, sigma = 0.5, 0.1 # mean and standard deviation
x, y = np.random.normal(mu, sigma, (2,60))
#print points
my_list_x = []
my_list_y = []
for i in range(0, len(x), 2):
    plt.plot(x[i:i+2], y[i:i+2]) 
    #print x[i:i+2] 
    #print y[i:i+2]
    #x_append = 
    my_list_x.append(x[i:i+2])
    x_coordinates= np.hstack(my_list_x)
    #y_append = 
    my_list_y.append (y[i:i+2])
    y_coordinates = np.hstack(my_list_y)  

  
print "X_coordinates", x_coordinates#my_list_x     
print "Y_coordinates", y_coordinates#y_append 
pair_list = np.vstack((x_coordinates, y_coordinates)).T 
print "x,y_coordinates_points\n", pair_list

line_coordinates = []
p = 0
temp = []
for pair in pair_list:
    p+=1
    if p%2==0:
        temp.append (pair)
        line_coordinates.append(temp)
        temp = []
    else:
        temp.append (pair)
        
print "line_coordinates\n", line_coordinates
mlines = MultiLineString(line_coordinates)     
print "MultiLineString\n", mlines   
for line_1, line_2 in combinations([line for line in mlines],2):
    if line_1.intersects(line_2):
        print(line_1.intersection(line_2))   
    


    