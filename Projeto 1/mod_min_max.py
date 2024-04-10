def mod_min_max(P):
    return [mod_min(P), mod_max(P)]

def mod_max(P):
    div = abs(P[0])
    P[0] = 0
    for element in P:
        element = abs(element)
    return 1 + (max(P)/div)

def mod_min(P):
    div = abs(P[len(P)-1])
    P[len(P)-1] = 0
    for element in P:
        element = abs(element)
    return (1 / (1 + ((max(P))/div)))

# caso de teste dos slides
# print (mod_min_max([1, -12, 19, -12]))
