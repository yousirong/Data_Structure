
import time
'''
def isPrime1(n):
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i += 1
    return True

def isPrime2(n):
    for i in range(2,n):
        if n%i == 0:
            return False

    return True
'''

n = int(input())  # 9999991, 99999989, 1410066367
# algorithm 2: O(root(n)) time algorithm

start = time.time()
prime = True
i = 2
while i*i <= n:           # 수행횟수 root(n) 이하
    if n%i == 0:
        prime = False
        break
    i += 1

if prime:
    print("Prime")
else:
    print("Not prime")

finish = time.time()
print(finish - start)

# algorithm 1: O(n) time algorithm
start = time.time()
prime = True
for i in range(2,n):         # 수행횟수 n -2번 이하
    if n%i == 0:
        prime = False
        break

if prime:
    print("Prime")
else:
    print("Not prime")

finish = time.time()

print(finish - start)



