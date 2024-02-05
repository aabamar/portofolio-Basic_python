'''
case:

Write a Class that can summarize the given data

- Named the class with `Data`
- Initialize the object with no input
- `Data` has several attributes:
  - `data` --> return the input data
  - `size` --> return the size of the input data
- `Data` has several methods:
  - `read_data(data)` --> to read the input data
  - `find_total()` --> return the total sum of the input data
  - `find_average()` --> return the average of the input data
'''
class Data:

    '''
    class of given data

    parameters
    ----------
    data = given data
    size = length of data

    method
    ----------

    read_data = input given data to class
    find_total = calculate total sum of data
    find_average = calculate average of data


    '''
    def read_data(self, data): #define read_data method
      self.data = data
      self.size = len(data)

    def find_total(self): #define find_total method
      total = sum(self.data)
      return total

    def find_average(self): #define find_average method
      average = sum(self.data)/self.size
      return average

    pass

'Example'

data = [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

try:
    data_obj = Data()
    data_obj.read_data(data)

    print(data_obj.data)
    print(data_obj.size)
    print(data_obj.find_total())
    print(data_obj.find_average())
except Exception as e:
    print('There is something wrong')