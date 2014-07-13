

seed = "https://www.udacity.com/cs101x/index.html"

index = {}

def get_page(url):

    try:
        import urllib2

        html = urllib2.urlopen(url)
    
        html_str = str(html.read())

        return html_str

    except:

        return ""


def get_next_target(page):
     
    start_pos = page.find("<a href=")

    if start_pos == -1:
        
        return None , 0
    
    start_link = page.find('"',start_pos)
    end_link = page.find('"', start_link + 1)
    link_string = page[start_link+1:end_link]
    return link_string , end_link


def get_all_links(html):
    
     
    links = []
    while True:
        url,end_pos = get_next_target(html)
        if url:
            links.append(url)
            html = html[end_pos:]
        else:
            
            break
    return links
    

def union(a,b):
    test = []
    for i in b:
        if i not in a:
            a.append(i)
        
   
    return a




  

def crawl_web(seed,max_depth = 1000):
    tocrawl = [seed]
    crawled = []
    next_depth = []
    depth = 0
    index = {}
    graph = {}
    while tocrawl and depth <= max_depth:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index,content,page)
            outlinks = get_all_links(content)
            union(next_depth, outlinks)
            graph[page] = outlinks
            crawled.append(page)
        if not tocrawl:
            tocrawl, next_depth = next_depth , []
            depth = depth + 1
        
    return index, graph
    


def add_to_index_old(index,keyword,url):
    counts = 0 
    for i in index:
        if i[0] == keyword:
            for j in i[1]:
                if url == j[0]:
                    return
            i[1].append([url,counts])       
            return            
                
    index.append([keyword,[[url,counts]]])
    

def add_to_index(index,keyword,url):
    if keyword in index:
        index[keyword].append(url)
        return
    else:
        index[keyword] = [url]
            
def lookup(index,keyword):
      if keyword in index:
          return index[keyword]
      else:
          return None


def add_page_to_index(index,content,url):
    content = content.split()
    for i in content:
        
        add_to_index(index,i,url)

    
    
def record_user_click(index,word,url):
    list_of_url = lookup(index,word)
    for i in list_of_url:
        if i[0] == url:
             i[1] = i[1] + 1
                      
    
    
def compute_ranks(graph):
    # Output of the Compute Ranks will be the dictionary which will give each url a score
    
    
