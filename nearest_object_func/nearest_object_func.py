'''
Case:
You are developing a web application that recommend good place to stay during holiday sessions.

A feature loved by most of customer is finding the nearest tourism object from a position (could be their hotel).

Given a list of tourism object (`tourism_name`), tourism object coordinates (`tourism_coor`), and customer places coordinates (`current_coor`), 
return the nearest tourism object as a `dict` type.
'''

# Function to find distance between 2 object
def calc_dist(A, B):
    '''
    Function to calculate distance between two objects

    Parameters
    ----------
    A : list
        The coordinates of object A

    B : list
        The coordinates of object B

    Returns
    -------
    dist : float
        The distance between A & B
    '''
    dist = (((A[0] - B[0]) ** 2) + ((A[1] - B[1]) ** 2))**0.5 #code for calculate distance between two objects
    return dist #return dist variable

def find_nearest(current_coor, tourism_coor, tourism_name):
    '''
    Function to find nearest tourism object near current coordinates

    Parameters
    ----------
    current_coor : list
        The guest current coordinate

    tourism_coor : list
        The tourism object coordinates

    toursim_name : list
        The tourism object name

    Returns
    -------
    nearest_object : dict
        The dictionary of nearest tourism object
    '''

    list_dist = [] #define list_dist list variable
    num = 0 #define while parameter

    while num < len(tourism_coor): #code for calculate neaerest tourism object
      list_dist.append(calc_dist(current_coor, tourism_coor[num])) #code for add calculated distance between current coordination with tourism object coordination

      num += 1

    #determine nearest tourism object for current coordination
    nearest_dist = min(list_dist)
    nearest_object = {'object' : tourism_name[list_dist.index(nearest_dist)], 'dist': nearest_dist}

    return nearest_object #return nearest_object variable