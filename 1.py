a = list(map(int, input().split()))
b = list(map(int, input().split()))
ab = (((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2)) ** 0.5
if a[0] < b[0] and a[1] < b[1]:
    if ab > (a[2] ** 2 + a[3] ** 2) ** 0.5:
        print("YES")
    else:
        print("NO")
elif b[0] < a[0] and b[1] < a[1]:
    if ab > (b[2] ** 2 + b[3] ** 2) ** 0.5:
        print("YES")
    else:
        print("NO")
elif a[0] == b[0]:
    if a[3] >= ab:
        print("YES")
    else:
        print("NO")
elif a[1] == b[1]:


