def first_palindrome(words):
    for i in range(len(words)):
        if words[i] in "0123456789":
            continue
        elif words[i][::-1] == words[i]:
            return words[i]
            break
        else:
            continue
        
    return("")
    i +=1
