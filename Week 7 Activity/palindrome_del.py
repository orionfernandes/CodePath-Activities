def check_palindrome(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    
    return True

def palindrome_del(s):

    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return check_palindrome(s, i, j - 1) or check_palindrome(s, i + 1, j)
        i += 1
        j -= 1
    return True
        
        
    
    return b
