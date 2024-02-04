'''
- NIK is not some random numbers. You can extract information from the NIK.
  - The first six digits are a province, regency, and district code
  - The next six digits are the date of birth; DD-MM-YY, respectively
    - For men, the date of birth ranged between 01-31
    - For women, the date of birth is added with 40, hence ranged between 41-71.
  - The last 4 digits are a serial number of NIK issuance.


- Given **two** NIK, your tasks are
  1. Extract the date of birth of each NIK
  2. Extract their gender.
  3. Extract whether they have similar gender.
  4. Extract whether they have similar month of birth.
'''


nik_1 = 1571011709860003
nik_2 = 2404075109910009


nik_1_str = str(nik_1)
nik_2_str = str(nik_2)

if int(nik_1_str[6:8]) < 40:
  nik_1_gender = 'Male'
  nik_1_dob = f'{nik_1_str[6:8]}-{nik_1_str[8:10]}-{nik_1_str[10:12]}'
else:
  nik_1_gender = 'Female'
  nik_1_str.replace(nik_1_str[6:8], str((int(nik_1_str[6:8])) - 40))
  nik_1_dob = f'{nik_1_str[6:8]}-{nik_1_str[8:10]}-{nik_1_str[10:12]}'

if int(nik_2_str[6:8]) < 40:
  nik_2_gender = 'Male'
  nik_2_dob = f'{nik_2_str[6:8]}-{nik_2_str[8:10]}-{nik_2_str[10:12]}'
else:
  nik_2_gender = 'Female'
  nik_2_day = int(nik_2_str[6:8]) - 40
  nik_2_dob = f'{nik_2_day}-{nik_2_str[8:10]}-{nik_2_str[10:12]}'

print(f'Date of Birth \n- NIK 1 : {nik_1_dob} \n- NIK 2 : {nik_2_dob}\n')
print(f'Gender \n- NIK 1 : {nik_1_gender}\n- NIK 2 : {nik_2_gender}\n')

print('Do they have similar gender?')
if nik_1_gender == nik_2_gender:
  print('Yes\n')
else:
  print('No\n')

month = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

print('Do they have similar month of birth?')
if nik_1_str[8:10] == nik_2_str[8:10]:
  month_nik = int(nik_1_str[8:10]) - 1
  print(f'Yes, it is on {month[month_nik]}')
else:
  print('No\n')