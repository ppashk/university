def task01():
    s = 'Hello, user!'
    half_len = len(s) // 2
    if len(s) % 2 == 1:
        half_len += 1
    new_s = s[half_len:len(s)] + s[0:half_len]
    print(new_s)
def task02():
    s = 'Hello user'
    arr = s.split()
    new_s = arr[1] + ' ' + arr[0]
    print(new_s)
def task03():
    s = 'Hello, fuckn\' user!'
    res = s.find('f')
    r_res = s.rfind('f')
    if res != -1:
        print(res)
        if res != r_res:
            print(r_res)
def task04():
    s = 'Hello, fuckn\' user!'
    arr = list(s)
    res = s.find('f')
    arr.pop(res)
    s = "".join(arr)
    sec_res = s.find('f')
    if res == -1:
        print(-2)
    elif sec_res == -1:
        print(-1)
    else:
        print(sec_res)
def task05():
    s = 'Say hello healey'
    arr = s.split('h')
    s = arr[0] + arr[len(arr) - 1]
    print(s)
def task06():
    s = 'Say hello healey'
    arr = s.split('h')
    arr[1] = arr[1][::-1]
    arr[0] += 'h'
    arr[2] = 'h' + arr[2]
    s = ''.join(arr)
    print(s)
def task07():
    s = '1 plus 1 is two'
    s = s.replace('1', 'one')
    print(s)
def task08():
    s = 'ty @ ja @ ty @ ja @ ty @ ja @'
    s = s.replace('@', '')
    print(s)
def task09():
    s = 'Say hello healey hemming'
    find = s.find('h')
    rfind = s.rfind('h')
    s = s.replace('h', 'H')
    s = s[:find] + 'h' + s[find + 1:rfind] + 'h' + s[rfind + 1:]
    print(s)
def task10():
    s = 'Hello user'
    t = ''
    for i in range(len(s)):
        if i % 3 != 0:
            t = t + s[i]
    print(t)
def task11():
    f_input = open('resources/lab07_task11_a_dict.txt', 'r')
    f_output = open('resources/lab07_task11_b_dict.txt', 'w')
    a_dict = dict()
    b_dict = dict()
    s = f_input.read().split('\n')
    for item in s:
        key = item.split(" ")[0]
        value = item.split(" ")[1:]
        a_dict[key] = value
    for key, value in a_dict.items():
        for item in value:
            b_dict[item] = key
    for key, value in b_dict.items():
        f_output.write('{} {}\n'.format(key, value))
task01()
task02()
task03()
task04()
task05()
task06()
task07()
task08()
task09()
task10()
task11()
