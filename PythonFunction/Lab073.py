# my_list = [True, "Arpit", 12.34, 90]
# my_list.sort()
# print(my_list)

squares = [1, 4, 9, 16, 25]

if not False:
    print("Not Empty")
else:
    print("Empty")


my_list = [1, 2, 3, 4, 5]
# temp_list = []
# for i in list:
#     temp_list.append(i * 2)
#
# print(temp_list)

# def double_item(num):
#     return num**2

# lambda num:num**2

# Map()
# 1. Takes Each item from the list
# 2. execute the function on it.
# 3. Return same number of elements ( list)

double_list = list(map(lambda num: num ** 2, my_list))
print(double_list)