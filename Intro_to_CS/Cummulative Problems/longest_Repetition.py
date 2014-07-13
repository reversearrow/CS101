#Longest Repetition

def keywithmaxval(d):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]

def is_list(p):
    return isinstance(p, list)


def longest_repetition(p):
    current_count = 1
    previous_count = 1
    dic = {}
    if p == []:
        return None
    
    for i in range(0, (len(p)-2)):
        current = p[i]
        upcoming = p[i+1]
        if current == upcoming:
                
                current_count = current_count + 1
                if current_count > previous_count:
                        if is_list(current):
                            current = str(current)
                            dic[current] = current
                        else:
                            dic[current] = current_count
            
        else:
            previous_count = current_count
            current_count = 1
    if dic == {}:
        return p[0]
    else:
        return keywithmaxval(dic),dic
                   
                                
