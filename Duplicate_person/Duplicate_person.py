'''
The marketing team & sales want to make sure that there is no duplicate person in the data.

Given a list of people ID & its name, find people ID & names that has similar names.
'''

def find_duplicates(people_ID, people_name):
    '''
    Function to find duplicate person

    Parameters
    ----------
    people_ID : List
        list of people ID

    people_name : list
        list of people name

    Returns
    -------
    people_duplicate : list
        List of duplicate people
    '''


    people_duplicate = [] #define people_duplicate variable


    #clean people_name list data
    people_name_space = [name.strip() for name in people_name] #delete space in people_name list of data
    people_name_lower = [name.lower() for name in people_name_space] #convert value in people_name list of data to lowercase

    #code for compare value of data in people_name with other value of data in peole_name
    num_1 = 0 #define while parameter
    while num_1 < len(people_ID):
      num_2 = 0 #define while parameter
      while num_2 < len(people_ID):
        if num_1 != num_2: #code only execute if parameter in first while and second while is different
          if people_name_lower[num_1] == people_name_lower[num_2]:
            people_duplicate.append([people_ID[num_1], people_name[num_1]]) #if the value of compared data is the same, then add the data to people_duplicate list variable
            num_2 = len(people_ID) #change num_2 value for ending while loop
          else:
            num_2 += 1
        else:
          num_2 += 1
      num_1 += 1

    return people_duplicate #return people_duplicate variable