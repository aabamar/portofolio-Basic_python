'''
case:
You are in a research team. Your product team asked you to help their research agenda, i.e. performing a Focus Group Discussion (FGD).

The product team need to distribute the user equally to each group. 
Please help the product team.

Your tasked is to divide $n$ people as equal as possible to $k$ groups.
'''
def distribute_user(n, k):
    '''
    Function to distribute n user equally to k class

    Parameters
    ----------
    n : int
        The number of people to distribute

    k : int
        The number of group

    Returns
    -------
    group_size : list
        The list of group size (must be integer) and shape of (k)
    '''

    group_size = [] #define group_size list variable
    num = 0 #define while parameter

    '''
    fair_group variable containing the amount of people with fair amount between each group
    e.g: if the total of people = 17 and the total of group = 3 then, the fair amount between each group is 5 with 2 remaining people is not included yet

    remaining_group variable containing the remaining amount of people after the amount of people with fair amount between each group has been distributed
    '''

    fair_group = n // k
    remaining_group = n % k

    while num < k: #code for distribute amount of people to each group with fair amount of people
      group_size.append(fair_group)

      num += 1

    num = 0 #define while parameter

    while num < remaining_group: #code for add remaining people to the group
      group_size[num] += 1

      num += 1

    return group_size
