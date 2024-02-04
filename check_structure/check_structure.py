'''
Given a 2D list of data, this is a function that returns the number of rows & columns from that list.
'''
def check_structure(data):
    '''
    Function to check the data structures

    Parameters
    ----------
    data : list
        The 2D sample data

    Returns
    --------
    data_shape : list
        The shape of data with format [nrows, ncols]
        nrows = number of rows
        ncols = number of columns
    '''
 
    nrows = len(data) #define nrows as length of matrix row
    ncols = len(data[0]) #define ncols as length of matrix column
    data_shape = [nrows, ncols] #define data_chape variable as row length, column length
    return data_shape #return data_shape value