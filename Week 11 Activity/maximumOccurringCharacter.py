from collections import Counter

def maximumOccurringCharacter(text):
    res = Counter(text)
    res = max(res, key = res.get)
    return (str(res))
