import numpy as np

def init2DArray(rows, cols, val=0):
    return [[val for j in range(cols)] for i in range(rows)]
