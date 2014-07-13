#Remove Tags

       

def line_together(p):
    string = ""
    for i in p:
        if i != " ":
            string = string + i

    return string
            
def remove_new_line(p):
    p = line_together(p)
    while "\n" in p:
        start_pos = p.find("\n")
        p = p[:start_pos] + p[start_pos + 1:]

    return p
    
def remove_tags(p):
      p = remove_new_line(p)

      end_pos = p.find(">")
      start_pos = p.find("<",end_pos)
      if start_pos == -1:
              return None, 0
      string = p[end_pos + 1 :start_pos]
      return string,start_pos         
    
          

 


def remove_all_tags(p):
    string = ""
    while True:
        element,start_pos = remove_tags(p)

        if element == None:
            break
        if not element:
           p = p[start_pos:]

        if element:
            string = string + " " + element
            p = p[start_pos:]

    return string.split()
            
