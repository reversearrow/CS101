# Sudoku

#Length Checker:


p = [[1,2,3,4],
             [2,3,1,1],
             [3,1,4,2],
             [4,4,4,3]]

def length_checker(lists):
    for i in lists:
        if len(i) != len(lists):
            return False
        
    return True

def value_checker(lists):
    for i in lists:
        for j in i:
            if j > len(lists):
                return False
            if type(1) != type(j):
                return False
    return True

def row_checker(lists):
    new_list = []
    for i in lists:
        for j in i:
            if j not in new_list:
                new_list.append(j)
            else:
                return False
        new_list = []
        
    return True


def column_checker(lists):
    new_list = []
    count = 0
    while True:
        for i in lists:
            j = i[count]
            if j not in new_list:
                new_list.append(j)
            else:
                print new_list
                return False
        count += 1
        new_list = []
        if count > len(lists) - 1:
            break
    return True

def sudoku(lists):
    if length_checker(lists) and value_checker(lists) and row_checker(lists) and column_checker(lists):
        return True
    else:
        return False
