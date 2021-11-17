import random
import time

def generate_list(list) :
    for i in range(0, 1000000) :
        list.append(random.randrange(0, 100))

def binary_search(a, x) :
    start = 0
    end = len(a) - 1

    while start <= end :                #탐색할 범위가 남아 있는 동안 반복
        mid = (start + end) // 2        #탐색 범위의 중간 위치
        if x == a[mid] :                #발견
            return mid
        elif x > a[mid] :               #찾는 값이 더 크면 오른쪽으로 범위
            start = mid + 1
        else :                          #찾는 값이 중간값보다 작으면 왼쪽으로 범위
            end = mid - 1
        return -1                       #찾지 못했을 때

def linear_search(a, x) :
    alist = []
    n = len(a)
    for i in range(0, n) :
        if x == a[i] :
            return i
    return -1
    
v = []
generate_list(v)
v.sort()

start = time.time()
i1 = linear_search(v, 36)
i2 = linear_search(v, 50)
print(v[i1])
print(v[i2])
print("순차탐색 : ", time.time()-start) #현재 시간 - 시작 시간

start = time.time()
i1 = binary_search(v, 36)
i2 = binary_search(v, 50)
print(v[i1])
print(v[i2])
print("이진탐색 : ", time.time()-start) #현재 시간 - 시작 시간