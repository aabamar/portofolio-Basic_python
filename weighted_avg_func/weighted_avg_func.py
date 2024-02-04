'''
Given a list of number (`data`) and list of weight (`w`), we want to find its weighted average.

To calculate the weighted average, using formula

weighted average = W1 * data 1 + W2 * data 2 +....+ Wn * data n
'''
def calc_weighted_avg(data, w):
    '''
    Function to calculate the weighted average of a list

    Parameters
    ----------
    data : list
        The sample data

    w : list
        The sample weights

    Returns
    -------
    avg : float
        The weighted average
    '''

    num = 0 #define while parameter
    avg = 0 #define weighted data average
    while num < len(data): #code for calculate average data weighted
      avg += (data[num] * w[num])
      num += 1

    return avg #return average value