word = "cab"
lst = [ ["c","a","b","z","c"],
        ["r","a","r","y","a"],
        ["b","w","o","w","b"],
        ["a","x","d","a","e"],
        ["c","o","b","a","c"] ]


def wordfinder(word, lst):
    a = ""
    b = ""
    c = ""
    d = ""
    e = []

# forming major string by joining all letters of rows

    e = (a.join(lst[0])+b.join(lst[1])+c.join(lst[2])+c.join(lst[3])+d.join(lst[4]))

    f = e[::-1]

    g = []

    h = ""

    print(e)
    print(f)
    
# Variable Initialization

    count = 0

    ptr1 = 0
    ptr2 = len(word)
    
    ptr3 = 0
    ptr4 = len(word)

    ptr5 = 0
    ptr6 = len(word)
    
    ptr7 = 0
    ptr8 = len(word)

# row operations

    for i in range(len(e)):
        if e[ptr1:ptr2] == word:
            count +=1
        ptr1+=1
        ptr2+=1

    for j in range(len(f)):
        if f[ptr3:ptr4] == word:
            count +=1
        ptr3+=1
        ptr4+=1

# column operations

    for col in range(len(lst[0])):
        for row in range(len(lst)):
            g.append(lst[row][col])
            
    h = h.join(g)       # converting list to string
    
    print(h)
    print(g)

    for k in range(len(h)):
        if h[ptr5:ptr6] == word:
            count +=1
        ptr5 +=1
        ptr6 +=1
        
    r = h[::-1]         # reversing string
    
    for l in range(len(r)):
        if r[ptr7:ptr8] == word:
            count += 1
        ptr7 +=1
        ptr8 +=1
        
        
    print("\nNumber of occurences : ", count)


wordfinder(word, lst)
