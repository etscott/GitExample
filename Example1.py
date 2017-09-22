import numpy as np

def listSqrt(x):
    return map(np.sqrt,x)

if __name__ == '__main__':
    print 'Hello World'
    li = range(5)
    print listSqrt(li)

