'''
- Given lists of `user_id`, `promo_A_status`, `promo_B_status`
- this program calculate how many user get a double promo (promo A and B) and find which `user_id` get double promo (promo A and B)
'''
# Note: You can write your input manually
user_id = [11, 21, 34, 49, 51]
promo_A_status = [1, 1, 0, 1, 0]
promo_B_status = [0, 0, 0, 0, 1]

num = 0 # while index variable
double_promo_user = [] # empty list for user with double promo

# function to check user with double promo
while num < len(user_id):
  if promo_A_status[num] == 1 and promo_B_status[num] == 1:
    double_promo_user.append(user_id[num])
  num += 1

# show total of user with double promo
print(f"Number of user with double promo: {len(double_promo_user)}")
# show the user with double promo
print(f"user_id with double promo: {double_promo_user}")