n = 0
print ("Pattern A")
for x in range (0,11):
    n = n + 1
    for a in range (0, n-1):
        print ('*', end = '')
    print()
print ('')
print ("Pattern B")
for b in range (0,11):
    n = n - 1
    for d in range (0, n+1):
        print ('*', end = '')
    print()
print ('')
print ("Pattern C")
for e in range (11,0,-1):
    n = n + 1
    for f in range (0, n+1):
        print ('*', end = '')
    print()
print ('')
print ("Pattern D")
for g in range (11,0,-1):
    n = n - 1
    for h in range (0, n-1):
        print ('*', end = '')
    print()