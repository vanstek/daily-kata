def nb_year(p0, percent, aug, p):
    n = 0
    percent = 1 + percent/100    
    while p0 < p: 
        p0 = p0 * percent + aug
        n += 1
    return n
