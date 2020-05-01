List = list(map(int, input().split()))
Set = set()
for i in List:
    if i in Set:
        print("YES")
    else:
        print("NO")
        Set.add(i)
