def sum(a, b, c):
    return a + b + c
print(sum(1, 2 ,3))
def input_num():
    num = input('Input num\n')
    if num.isdigit():
        print(f'U enter {num}')
    else:
        print('That`s not num')
def print_num():
    print('Here u can input num')
    input_num()
print_num()
