import time
def bs(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
def ss(f):
    n = len(f)
    for i in range(n):
        b = i
        for j in range(i + 1, n):
            if f[j] < f[b]:
                b = j
        f[i], f[b] = f[b], f[i]
def mt(sf, d):
    st = time.time()
    sf(d)
    et = time.time()
    return et - st
size = int(input("Enter the number of elements: "))
rl = []
print("Enter the elements:")
for _ in range(size):
    rl.append(int(input()))
bl = rl[:]
sl = rl[:]
tb = mt(bs, bl)
ts = mt(ss, sl)
print(f"Bubble Sort Time: {tb:.3f} sec")
print(f"Selection Sort Time: {ts:.3f} sec")
print("Sorted List using Bubble Sort:", bl)
print("Sorted List using Selection Sort:", sl)