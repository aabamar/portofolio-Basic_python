'''
Case:
You are on a marketing team that have to transfer e-money as a gift to your customer.

You noticed that the phone number data is inconsistent & you have to clean it.

This is the valid definition of phone number
- Starts with `62`, e.g. `62xxxxxxxxxxx`
- It must be 11 digit number, excluding `62`

Clean the phone number first. If after cleaning, there is an invalid phone number, 
change the phone number with `'Invalid number'`.
'''
def clean_phone_number(phone_list):
    '''
    Function to clean the phone number

    Parameters
    ----------
    phone_list : list
        The raw sample of phone data

    Returns
    -------
    phone_clean : list
        The clean sample of phone data
    '''
    
    phone_clean = [] #define phone_clean list variable

    for phone_number in phone_list: #code for determine the data had 11 number or not, for filtering invalid number
      if len(phone_number) < 11: #code for define invalid number in the data
        phone_number = 'Invalid Number'
        phone_clean.append('Invalid Number')
      else: #code for clean valid data and insert data into phone_clean list with additional '62'
        phone_number = phone_number.replace(" ", "").replace("-", "").replace("+", "")
        phone_clean.append(int('62' + phone_number[-11:]))

    return phone_clean #return phone_clean variable