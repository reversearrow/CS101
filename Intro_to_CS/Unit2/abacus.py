#Abaci for 0

def input_check(n):
    n = str(n)
    if len(n) != 10 and len(n) < 10 :
      return  "0" * (10 - len(n)) + n
    else:
        return n
    
    


def print_abaci(n):
    n = input_check(n)
    
    for i in range(0,10):    
        string = "|00000*****"
        j = int(n[i])
        if j != 0:
            print string[:(11-j)] + "   " + string[-j:] + string[0]
        else:
            print string[:(11-j)] + "   " + string[0]            
 
