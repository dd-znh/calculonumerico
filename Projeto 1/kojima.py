def kojima(P):
    res = []
    for i in range(len(P)-1):
        res.append((abs(P[i+1]/P[0]))**(1/(i+1)))

    mx1 = (max(res))
    res.remove(max(res))

    mx2 = (max(res))
    res.remove(max(res))
    
    return float(mx1 + mx2)
