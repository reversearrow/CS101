# Remove Tags
def remove_tags(string):
    start_pos = string.find("<")
    
    while start_pos != -1:
        end_pos = string.find(">",start_pos)
        string = string[:start_pos] + " " + string[end_pos + 1:]
        print string
        start_pos = string.find("<")
    return string.split()
    
        
    
    
    
