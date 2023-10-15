def main():
    n = 38

    f0 = 0
    f1 = 1
    s = 0

    if n == 0:
        print(0)
        return
    if n == 1:
        print(1)
        return

    for iter in range(2,n+1):
        new_f = f0+f1
        f0 = f1
        f1 = new_f
        print(new_f)

if __name__ == '__main__':
    main()
