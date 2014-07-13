#deep reverse:


def is_list(p):
    return isinstance(p, list)



def deep_reverse(p):
     result = []
     if is_list(p):
         
         for i in range(len(p) - 1, -1, -1):
             result.append(deep_reverse(p[i]))
         return result
     else:
         return p
