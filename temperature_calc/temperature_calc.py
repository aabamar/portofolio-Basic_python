# giving input value for temp, from temp unit & to temp unit
temp = 20
from_unit = 'celcius'
to_unit = 'Fahrenheit'

# convert 'from_unit' & 'to_unit' to lowercase
from_unit = from_unit.lower()
to_unit = to_unit.lower()

# check & validate value for 'from_unit' & 'to_unit' are kelvin, celcius & fahreinheit
if (from_unit == 'kelvin' or from_unit == 'celcius' or from_unit == 'fahrenheit') and (to_unit == 'kelvin' or to_unit == 'celcius' or to_unit == 'fahrenheit'):

# convert temp from celcius unit
  if from_unit == 'celcius':
    if to_unit == 'fahrenheit':
      convert_temp = (temp * 9/5) + 32
    elif to_unit == 'kelvin':
      convert_temp = temp + 273
    elif to_unit == 'celcius':
      convert_temp = temp
    else:
      pass

# convert temp from fahrenheit unit
  if from_unit == 'fahrenheit':
    temporary_temp = (temp-32) * 5/9 # temp convert to celcius
    if to_unit == 'celcius':
      convert_temp = temporary_temp
    elif to_unit == 'kelvin':
      convert_temp = temporary_temp + 273
    elif to_unit == 'fahrenheit':
      convert_temp = temp
    else:
      pass

# convert temp from kelvin unit
  if from_unit == 'kelvin':
    temporary_temp = temp - 273 # temp convert to celcius
    if to_unit == 'celcius':
      convert_temp = temporary_temp
    elif to_unit == 'fahrenheit':
      convert_temp = (temporary_temp * 9/5) + 32
    elif to_unit == 'kelvin':
      convert_temp = temp
    else:
      pass

  print(f'{temp} {from_unit} is equal to {int(convert_temp)} {to_unit}') # print output value

else:
  print('''error *wrong temp unit value*''') # show error for worng temp unit value