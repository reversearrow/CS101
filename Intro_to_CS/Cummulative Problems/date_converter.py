#Date Converter

english = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 
6:"June", 7:"July", 8:"August", 9:"September",10:"October", 
11:"November", 12:"December"}

swedish = {1:"januari", 2:"februari", 3:"mars", 4:"april", 5:"maj", 
6:"juni", 7:"juli", 8:"augusti", 9:"september",10:"oktober", 
11:"november", 12:"december"}

def date_converter(dictionary,date):
    #Date has 3 parts
    month_1 = date.find("/")
    day_1 =  date.find("/",month_1 + 1)
    month = date[:month_1]
    day = date[month_1+1:day_1]
    year = date[day_1+1:]

    return day + " " + dictionary[int(month)] + " " + year
    
