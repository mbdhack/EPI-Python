from test_framework import generic_test


def multiply(num1, num2):
    sign = -1 if (num1[0]<0) ^(num2[0]<0) else 1 #set te sign that the result will have
    num1[0],num2[0] = abs(num1[0]),abs(num2[0]) #remove the sign to be able to do multiplication 

    result = [0] * (len(num1)+len(num2)) #create the result array and set it to zero

    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i+j+1] += num1[i] * num2[j] # multiply 
            result[i+j] += result[i+j+1] //10 # get the carry
            result[i+j+1] %= 10 #keep remainder
    
    #stip leading zero if any
    result = strip_leading_zero(result)

    return [sign * result[0]] + result[1:]

def strip_leading_zero(result):
    final =[]
    if result[0] != 0:
        return result
    else:
        num_has_started= False
        for num in result:
            if num !=0 or num_has_started:
                final.append(num)
                num_has_started = True
    if final:
        return final
    return [0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_multiply.py",
                                       'int_as_array_multiply.tsv', multiply))
