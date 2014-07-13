#Longest Repetition:

def longest_repetition(p):
    current_count = 0
    previous_count = 0
    element_track = None
    current_element = None
    
    for i in p:
          
        if current_element == i:
            current_count = current_count + 1
            if current_count > previous_count:
                previous_count = current_count
                element_track = current_element
 
        else:
            if current_count > previous_count:
                previous_count = current_count
                element_track = current_element
            if previous_count == 0:
                element_track = p[0]
            current_count = 0
            current_element = i
            
            
    return element_track 
                
            
