#Shift_N_Letters

def shift_n_letter(letter,n):
      return chr(97+(ord(letter)-97+n)%26)

    
def rotate(name,n):
    output = ""
    for i in name:
        if ord(i) != 32:
            i = shift_n_letter(i,n)
            output = output + i
        else:
            output = output + " "
    return output
