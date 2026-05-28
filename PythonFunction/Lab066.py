numbers = [1, 2, 3]


# Collecion of Items

def do_something(arpit_list):
    arpit_list.append(100)
    arpit_list[0] = 123
    return arpit_list

def shanti():
    print("dasda")

l = do_something(arpit_list=numbers)
print(l)