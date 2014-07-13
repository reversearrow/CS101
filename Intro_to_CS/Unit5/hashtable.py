# HashTable Program



def make_hashtable(bucket):
    index = []
    for i in range(0 , bucket):
        index.append([])
    return index
        

def hash_string(string,bucket):
    num = 0
    if bucket <= 0:
        return None
    for i in string:
        num = num + ord(i)
        bucket_num = num%bucket
        
    return bucket_num

def hashtable_get_bucket(hashtable,keyword):
    len_of_htable = len(hashtable)
    keyword_occurance = hash_string(keyword,len_of_htable)
    return hashtable[keyword_occurance]



def hashtable_add(htable,key,value):
    get_bucket = hashtable_get_bucket(htable,key)
    get_bucket.append([key,value])
    return htable


def hashtable_lookup(htable,key):
    entry,bucket = hashtable_helper(htable,key)
    if entry:
        return entry[1]
    else:
        return None

def hashtable_update(htable,key,value):
    entry,bucket = hashtable_helper(htable,key)
    if entry:
        entry[1] = value
    else:
        bucket.append([key,value])
    
        
 
def hashtable_update_old(htable,key,value):
    bucket = hashtable_get_bucket(htable, key)
    for entry in bucket:
        if entry[0] == key:
            entry[1] = value
            return
    bucket.append([key, value])
    
def hashtable_helper(htable,key):
       bucket = hashtable_get_bucket(htable, key)
       for entry in bucket:
            if entry[0] == key:
                return entry,bucket
        
       return None, bucket
       
       
       
    
hashtable = make_hashtable(1000)
print hashtable_get_bucket(hashtable,"Udacity")


table = [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]],
[['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]

