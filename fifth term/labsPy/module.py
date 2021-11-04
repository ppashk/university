def task01():
    s = "do bist do"
    p = "do"
    result = 0
    find = s.find(p)
    while find != -1:
        result += find
        print(result)
        result += 1
        s = s[find + 1:]
        find = s.find(p)

task01()
