#Find and Replace

def make_converter(match, replacement):
        return match,replacement
    

def apply_converter(converter, string):
    match,replacement = converter
    match_check = string.find(match)
    len_of_match = len(match)
    while match_check != -1:
 
        string = string[:match_check] + replacement + string[match_check+len_of_match:]
        match_check = string.find(match)

    return string
    


def converter(string,match,replacement):
    match_check = string.find(match)
    len_of_match = len(match)
    while match_check != -1:
        string = string[:match_check] + replacement + string[match_check+len_of_match:]
        match_check = string.find(match)
    return string
        
