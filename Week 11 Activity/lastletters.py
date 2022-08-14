word = "apple"
l = []

def lastletters(word):
  for i in word:
    l.append(i)

  return (l[-1]+" "+l[-2])
  

print(lastletters(word))
