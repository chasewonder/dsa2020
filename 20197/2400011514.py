def main():
    l = input()
    n, m = map(int, l.split())
    s = min(n, m)
    n = max(n, m)
    m = s
    sum = 0
    while m > 0:
        sum += n // m
        s = n % m
        n = m
        m = s
    print(sum)

if __name__ == "__main__":
    main()