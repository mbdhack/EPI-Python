def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    sign = -1 if x<0 else 1
    x=abs(x)
    final_num = list()
    
    while x // 10 > 0:
        final_num.append(x%10)
        x //= 10
    final_num.append(x)
    final_num = ''.join(str(x) for x in final_num)
    print(int(final_num))

reverse(120)