names = {"Alice": "Bob", "Charlie": "Charlie", "Jane": "King"}
samename =[]
word_dict = {}

def same_name(names):
  
  for name in names:
    if names[name] == name:
      samename.append(name)
      print("Owners with same name: ", name)
    



same_name(names)
