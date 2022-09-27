def next_bigger(n):
    s = list(str(n))
    lenght = len(str(n))
    max_n = int("".join(sorted(s, reverse=True)))
    min_n = sorted(s)
    m = n
    print(s, lenght, max_n, min_n)

    """
    for i in range(lenght-2,-1,-1):
        if(s[i] < s[i-1]):
            a = s[i:]
            m= min(filter(lambda x: x>a[0],a))
            a.remove(m)
            a.sort()
            s[i:] = [m] +a
            return int("".join(s))
    """
    while m <= max_n:
        m += 1
        print(m, min_n, max_n)
        if sorted(list(str(m))) == min_n:
            return m
    return -1





print(next_bigger(2017))