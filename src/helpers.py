import numpy as np
import numpy.ma as ma

#This file contains various functions that provide functionalities useable in the event tasks

##Functions for input formatting--------------------------------------------------------------
#

def string_to_field(string_in, height, width, index_first=0, index_last=None):
    if not index_last: index_last=len(string_in)
    text=string_in[index_first:index_last].ljust(height*width, '0')
    arr=np.asarray([char for char in text])
    return arr.reshape(height,width)

def get_list_of_neighbours(TwoDArray):
    neigh=[]
    padded=np.pad(TwoDArray,1,constant_values='.')
    for i in range(len(TwoDArray)):
        for j in range(len(TwoDArray[0])):
            area=padded[i:i+3,j:j+3]
            neigh.append(area.flatten())
    return neigh


#Filter for certain inputs
def create_mask_for_values(arr_in, values_to_keep):
    print(arr_in)
    for i in values_to_keep:
        arr_in=arr_in.replace(i,'~')
    for i in arr_in:
        if not i =='~':
            arr_in=arr_in.replace(i,'1')
    arr_in=arr_in.replace('~','0')
    return arr_in

def get_masked_array(data, mask):
    return ma.masked_array(data, mask)

#---------------------------------------------------------------------------------------------

if __name__ == "__main__":
    #print(get_masked_array(np.array([1, 2, 3, -1, 5]), [0,1,0,0,0]))
    #inarr =np.char.array([1,2,3,'.',8,'.'])
    #print(create_mask_for_values(inarr,['1','.']))
    print(get_list_of_neighbours([[1,2,3],['.',8,'.']]))