def split_list_in_half(any_list):
    half = len(any_list)//2
    return any_list[:half], any_list[half:]

values = [1,2,3,4,5,6,7,8]
one, two = split_list_in_half(values)

print(one) # [1, 2, 3, 4]

print(two) # [5, 6, 7, 8]