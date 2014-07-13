#Frequency Analysis
 
def freq_analysis(message):
    
    output = []
    string = "abcdefghijklmnopqrstuvwxyz"
    for i in string:
        count = message.count(i)
        output.append((count/1.0)/len(message))
    return output
        
        
            
