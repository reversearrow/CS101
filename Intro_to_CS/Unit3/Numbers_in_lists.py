# numbers_in_lists

string = '543987'
def numbers_in_lists(string):
    i = None
    output = []
    test = []
    for j in string:
         if i != None:
             print i,j
             if i >= j:
                 output.append(i)
 
                 test.append(j)
             else:
                 
                 print i + "Hullu"
                 
                 if test not in output:
                         output.append(test)
                 test = [] 

         i = j
         
    return output                   
