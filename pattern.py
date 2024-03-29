# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=' ')
    print()

# 1 1 1 1 1 
# 2 2 2 2 
# 3 3 3 
# 4 4 
# 5
n = 5
for i in range(1,n+1):
    for j in range(1, n-i+2):
        print(i, end=' ')
    print()

# 5 5 5 5 5 
# 5 5 5 5 
# 5 5 5 
# 5 5 
# 5
n = 5
for i in range(1, n+1):
    for j in range(1, n-i+2):
        print(n, end=' ')
    print()

# 0 1 2 3 4 5 
# 0 1 2 3 4 
# 0 1 2 3 
# 0 1 2 
# 0 1
n = 5
for i in range(0,n):
    for j in range(0, n-i+1):
        print(j, end=' ')
    print()

# 1 
# 3 3 
# 5 5 5 
# 7 7 7 7 
# 9 9 9 9 9
n = 5
for i in range(1,n+1):
    for j in range(1, i+1):
        print(i*2-1, end=' ')
    print()

# 5 5 5 5 5 
# 4 4 4 4 
# 3 3 3 
# 2 2 
# 1
n = 5
for i in range(n,0,-1):
    for j in range(1, i+1):
        print(i, end=' ')
    print()

# 1 
# 2 1 
# 3 2 1 
# 4 3 2 1 
# 5 4 3 2 1
n = 5
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j, end=' ')
    print()

# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1
n = 5
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j, end=' ')
    print()

# 1
# 3 2
# 6 5 4
# 10 9 8 7