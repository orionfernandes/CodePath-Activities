import time

# Create a list with 100000 items using the range() method
start = time.time()
mylist = list(range(100000))
end = time.time()
print('Time:', end-start)

# Create a dictionary with 100000 items using the range() method
start = time.time()
mydict = {}
for i in range(100000):
     mydict[i] = i
end =time.time()
print('Time:', end-start)

# Access the element at key 10000
print("\n Access the element at key 10000")
start = time.time() # Start time = 0

# TODO: ADD FUNCTION CALL BELOW
def print_key_100000():
  print(mylist[-1])
print_key_100000()
end = time.time() #Snapsnot of time after script runs
print("Task 1 Runtime: ", end-start) #Subtract the difference

# Add a new key-value pair to the dictionary
print("\n Add a new key-value pair to the dictionary")
start = time.time() # Start time = 0
mydict[0] = [0]
end = time.time() #Snapsnot of time after script runs
print('Time:',end-start)
      
# Increment the value at key 10 by 1
print("\n Increment the value at key 10 by 1")
start = time.time() #Start time = 0
mydict[10] += 1 #Increment the value at key 10 by 1
end = time.time() #Snapsnot of time after script runs
print('Time:',end-start)

# Delete key 10000
print("\n Delete key 10000")
start = time.time()
del mydict[10000]
end = time.time() 
print('Time:',end-start)

# Check if the key 10 is in the dictionary
print("\n Check if the key 10 is in the dictionary")
start = time.time()
if 10 in mydict:
  print('true')
end = time.time()
print('Time:', end-start)

# Check if the key -10 is in the dictionary
print("\n Check if the key -10 is in the dictionary")
start = time.time()
if (-10) in mydict:
  print(True)
else:
  print(False)
end = time.time()
print('Time:', end-start)

# Pop the first item off of the list
print("\n Pop the first item off of the list")
start = time.time()
mylist.pop(0)
end = time.time()
print('Time:', end-start)

# Pop the last item off of the list
print("\n Pop the last item off of the list")
start = time.time()
mylist.pop(-1)
end = time.time()
print('Time:', end-start)
