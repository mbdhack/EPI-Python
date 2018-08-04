# Implement your function below.
def is_one_away(s1, s2):
    if s1 ==s2:
        return True
    elif abs(len(s1)-len(s2))!= 1 and len(s1)!=len(s2):
        return False
    else:
        if len(s1) == len(s2):
            i=0
            while i<len(s1):
                if s1[i]!=s2[i]:
                    s3= s1[:i]+s2[i] if i==len(s1)-1 else s1[:i]+s2[i]+s1[i+1:]
                    return s3==s2
                i+=1
        else:
            l_s = s1 if len(s1)>len(s2) else s2
            s_s = s1 if len(s1)<len(s2) else s2
            i=0
            while i<len(s_s):
                if s_s[i]!=l_s[i]:
                    return s_s == l_s[:i]+l_s[i+1:]
                i+=1
            return True
    return False

# NOTE: The following input values will be used for testing your solution.
print(is_one_away("abcde", "abcd") ) # should return True
print(is_one_away("abde", "abcde"))  # should return True
print(is_one_away("a", "a"))  # should return True
print(is_one_away("abcdef", "abqdef"))  # should return True
print(is_one_away("abcdef", "abccef"))  # should return True
print(is_one_away("abcdef", "abcde"))  # should return True
print(is_one_away("aaa", "abc"))  # should return False
print(is_one_away("abcde", "abc"))  # should return False
print(is_one_away("abc", "abcde"))  # should return False
print(is_one_away("abc", "bcc"))  # should return False
