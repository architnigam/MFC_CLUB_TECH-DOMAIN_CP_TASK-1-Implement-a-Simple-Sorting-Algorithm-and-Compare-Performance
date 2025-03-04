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
def iss(c):
    n = len(c)
    for i in range(1, n):
        key = c[i]
        j = i - 1
        while j >= 0 and c[j] > key:
            c[j + 1] = c[j]
            j -= 1
        c[j + 1] = key
def mt(sf, d):
    st = time.perf_counter_ns()
    sf(d)
    et = time.perf_counter_ns()
    return et - st
size = int(input("Enter the number of elements: "))
rl = []
print("Enter the elements:")
for _ in range(size):
    rl.append(int(input()))
bl = rl[:]
sl = rl[:]
il = rl[:]
tb = mt(bs, bl)
ts = mt(ss, sl)
ti = mt(iss, il)
print(f"Bubble Sort Time: {tb:.3f} nanosecs")
print(f"Selection Sort Time: {ts:.3f} nanosecs")
print(f"Insertion Sort Time: {ti:.3f} nanosecs")
print("Sorted List using Bubble Sort:", bl)
print("Sorted List using Selection Sort:", sl)
print("Sorted List using Insertion Sort:", il)
if tb < ts and tb < ti:
    print("On comparing, Bubble Sort is the fastest! 👍")
elif ts < tb and ts < ti:
    print("On comparing, Selection Sort is the fastest! 👍")
else:
    print("On comparing, Insertion Sort is the fastest! 👍")
