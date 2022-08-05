dicti = []

def unique(my_list):
    for i in my_list:
        if i not in dicti:
            dicti.append(i)
      
    return dicti
