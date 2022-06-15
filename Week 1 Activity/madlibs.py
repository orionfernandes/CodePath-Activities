# Run using Shell -> python3 madlibs.py


try:
    name = str(input("Input Name: "))
    noun = str(input("Input Noun: "))
    adjective = str(input("Input Adjective: "))
    verb = str(input("Input Verb: "))

    vowel = 'aeiou'

    if noun in vowel:
        print(f"Nice to meet you {name}. There's an {noun} right behind you ! It looks rather {adjective}. I think it wants to {verb}.")
    else:
         print(f"Nice to meet you {name}. There's a {noun} right behind you ! It looks rather {adjective}. I think it wants to {verb}.")
except:
    pass

