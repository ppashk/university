def task01():
    fib01 = 0
    fib02 = 1
    i = 1
    k = 5
    n = 20
    while i <= n:
        fib_sum = fib02 + fib01
        fib01 = fib02
        fib02 = fib_sum
        if i >= k:
            print(fib_sum)
        i = i + 1

def task02():
    i = 0
    n = 20
    while i <= n:
        if i % 2 == 0:
            print(i)
        i = i + 1
    print('\n')
    i = -1
    n = -21
    while i >= n:
        if i % 3 == 0:
            print(i)
        i = i - 1

def example():
    print("Solve 4*100 - 54")
    res = input("Input your answer\n")
    if res.isdigit() and int(res) == 346:
        print("Correct")
    else:
        print("Wrong")

def unlimited_example():
    print("Solve 4*100 - 54")
    res = input("Input your answer\n")
    if res.isdigit():
        while res != 346:
            print("Try again")
            res = input("Input your answer\n")
            if res.isdigit():
                res = int(res)
        print("Correct")

task01()
print('\n')
task02()
print('\n')
example()
print('\n')
unlimited_example()
