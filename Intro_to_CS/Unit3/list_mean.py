# Getting the mean of the list

def list_mean(lists):
    divider = len(lists)
    divider = float(divider)
    total = 0

    if lists == []:
        return None
    
    for i in lists:
        total = total + i
    return total/divider
