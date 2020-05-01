with open("input.txt", "r", encoding="utf8") as file:
    n = int(file.readline())
    Set_num = set(range(1, n + 1))
    new = set()
    for line in file:
        if "YES" in line:
            Set_num &= new
        elif "NO" in line:
            Set_num -= new
        elif "HELP" not in line:
            new = set(map(int, line.split()))
print(' '.join(map(str, sorted(Set_num))))
