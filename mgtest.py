# The command "nosetests mgtest.py" gives the following error for
# Python ver 2.7.10, NumPy ver 1.11.0.dev0+772c80b, and nosetests ver 1.3.4:
#    TypeError: meshgrid() got an unexpected keyword argument 'indexing'
#
import numpy as np
#
def test():
    x1 = np.array([1.,2.,3.])
    x2 = np.array([4.,5.])
    xmat = np.meshgrid(x1,x2,indexing='ij')
