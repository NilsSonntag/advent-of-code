import numpy as np

#This file contains various functions that provide functionalities useable in the event tasks

##Functions for input formatting--------------------------------------------------------------
#

def string_to_field(string_in, height, width, index_first=0, index_last=None):
    if not index_last: index_last=len(string_in)
    text=string_in[index_first:index_last].ljust(height*width, '0')
    arr=np.asarray([char for char in text])
    return arr.reshape(height,width)


#---------------------------------------------------------------------------------------------

if __name__ == "__main__":
    print(string_to_field("abcd",2,2))