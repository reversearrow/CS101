# Program to check symettry


lists = [[1, 2, 3],
         [2, 3, 4],
        [3, 4, 1]]

lists2 = [["cat", "dog", "fish"],
                ["dog", "dog", "fish"],
                ["fish", "fish", "cat"]]

def symmetric(lists):
   i,j = 0,0
   while i < len(lists) and j < len(lists):
       #print lists[i][j], lists [j][i]
       if length_checker(lists) == False:
           return False

       if lists[i][j] == lists[j][i]:
           j += 1
       else:
           return False
       if j > len(lists) - 1:
           j = 0
           i = i + 1
   return True
           
       
       
def length_checker(lists):
    for i in lists:
        if len(i) != len(lists):
            return False
        
    return Truedef length_checker(lists):
    for i in lists:
        if len(i) != len(lists):
            return False
        
    return True
