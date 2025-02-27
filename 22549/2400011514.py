def main():
    s = input()
    dic = {}
    for l in "abcdefghijklmnopqrstuvwxyz":
        dic[l] = 0
    for n, c in enumerate(s):
        n += 1
        if dic[c] > 0:
            dic[c] = -1
        elif dic[c] == 0:
            dic[c] = n
    min = 100001
    c = 'A'
    for l in "abcdefghijklmnopqrstuvwxyz":
        if dic[l] > 0 and dic[l] < min:
            min = dic[l]
            c = l
    if (c != 'A'):
        print(dic[c] - 1)
    else:
        print(-1)


if __name__ == "__main__":
    main()