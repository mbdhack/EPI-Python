def num_add_up(num_list,k):
    seen = {}
    for num in num_list:
        seen[num] = 1
        if k-num in seen and k-num != num:
            return True
    return False

print (num_add_up( [10, 15, 3, 7,2,10,17],20))
        