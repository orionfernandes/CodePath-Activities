l = []

a = ""

dictionary = {"hello": "hola", "world": "mundo", "si": "yes", "por favor": "please"}

while a != "exit":
  a = input("Enter words to add to list - type 'exit' to stop: ")
  l.append(a)
  if a == "exit":
    del l[-1]

def translate(l, dictionary):
  for i in range(len(l)):
    print(l[i], "=", dictionary.get(l[i]))

translate(l, dictionary)
