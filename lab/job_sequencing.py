def JobScheduling(arr, t):
    a = len(arr)
    for i in range(a):
        for j in range(a - 1 - i):
            if arr[j][2] < arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    res = [False] * t
    job = ['-1'] * t
    for i in range(len(arr)):
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
            if res[j] is False:
                res[j] = True
                job[j] = arr[i][0]
                break
    print(job)
jobs = int((input("Total Number of jobs- ")))
arr = []
for i in range(0, jobs):
    l = []
    l = list(map(str, input().split(",")))
    for j in range(1, len(l)):
        l[j] = int(l[j])
    arr.append(l)
print("Max profit sequence of jobs- ")
JobScheduling(arr, 3)