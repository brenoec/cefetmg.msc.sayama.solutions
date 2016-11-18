
import matplotlib
matplotlib.use('TkAgg')

from pylab import *
import numpy, pycxsimulator

n = 100
p = 0.6180

def N (val = n):
    global n
    n = int(val)
    return val
    
def P (val = p):
    global p
    p = float(val)
    return val

def initialize():
    global config, nextconfig, n, p

    config = zeros([n, n])
    for x in xrange(n):
        for y in xrange(n):
            config[x, y] = 1 if random() < p else 0

    nextconfig = zeros([n, n])
    
    # initialize tree on fire    
    while(1):
       i = numpy.random.randint(n)
       j = numpy.random.randint(n)
       if (config[i, j] == 1):
           config[i, j] = 2
           break

def observe():
    global config, nextconfig
    cla()
    imshow(config.T, vmin = 0, vmax = 2, cmap = cm.binary, interpolation='none')
    axis('off')

def update():
    global config, nextconfig, n, p
    
    for x in xrange(n):
        for y in xrange(n):
            
            for dx in [-1, 0, 1]:
            
                nx = x + dx
                nx = 0 if nx < 0 else nx
                nx = n - 1 if nx == n else nx
            
                if (config[x, y] == 2 and config[nx, y] == 1):
                    nextconfig[x, y]  = 2
                    nextconfig[nx, y] = 2
                    
            for dy in [-1, 1]:
                
                ny = y + dy
                ny = 0 if ny < 0 else ny
                ny = n - 1 if ny == n else ny
                
                if (config[x, y] == 2 and config[x, ny] == 1):
                    nextconfig[x, y]  = 2                    
                    nextconfig[x, ny] = 2                    
    
    for x in xrange(n):
        for y in xrange(n):
            
            if (nextconfig[x, y] != 2):
                nextconfig[x, y] = config[x, y]
                
    config, nextconfig = nextconfig, config

pycxsimulator.GUI(parameterSetters = [N, P]).start(
    func=[initialize, observe, update])
