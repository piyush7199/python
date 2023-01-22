def mis(n):
    res = []
    count = 1
    j = 1
    while(j*count<=n):
        res.append(j*count)
        count = j*count
        j += 1

    return res

# mis(10)