# Tuple - Collection of Items

my_list = [1, 2, 3, 4, 5]
print(id(my_list))
my_list[0] = 21  # Mutable
print(my_list)
print(id(my_list))

my_tuple = (1, 2, 3, 4, 5, 5)
# my_tuple[0] = 21 # Immutable
print(my_tuple)



my_list = [1, 4, 5, 7]


def double_item(num):
    return num * 2


# Map()
# Takes each item from list
# execute function on it
# return same no of elements (list)
# return modified list

double_list = list(map(double_item, my_list))
print(double_list)