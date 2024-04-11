def mod_min_max(P):
    P = [abs(element) for element in P]
    return [format(mod_min(P), ".5f"), format(mod_max(P), ".5f")]

def mod_max(P):
    Q = P[1:len(P)]
    res = (1 + (max(Q)/P[0]))
    return res

def mod_min(P):
    R = P[0:len(P)-1]
    res = (1 / (1 + ((max(R))/P[len(P)-1])))
    return res
