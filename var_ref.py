def update_list(a_list):
    a_list[0] = a_list[0] * 2
    a_list[1] += 5
    a_list[2] = 10
    return a_list

our_list = [6, 12, 43214]

our_list = update_list(our_list)
print(our_list)