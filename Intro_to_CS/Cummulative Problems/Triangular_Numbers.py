#Cummulative Problems


def triangular(p):
    if p == 1:
        return 1
    else:
        return p + triangular(p-1)
    
