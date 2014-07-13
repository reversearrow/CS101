#Memoization

#a cached : Dictionary that maps input to proc their previously computed values
#Proc : Procedure which can be callled by just writing proc(proc_input)


cache = {}

def cached_execution(cache,proc,proc_input):
    proc_str = str(proc).split()[1]
    

    if proc_str in cache:
          
        if proc_input in cache[proc_str]:
            return cache[proc_str][proc_input]
        else:
            cache[proc_str][proc_input] = proc(proc_input)
            return cache[proc_str][proc_input]
    else:
        proc_result = proc(proc_input)
        cache[proc_str] = {proc_input:proc_result}
        return proc_result


def cached_execution_old(cache,proc,proc_input):
    if proc_input not in cache:
        cache[proc_input] = proc(proc_input)
    return cache[proc_input]

def factorial(n):
    print "Running factorial"
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result


print cached_execution(cache, factorial, 50)

print cached_execution(cache, factorial, 50)

print cached_execution(cache, factorial, 40)



def cached_fibo(n):
    if n == 1 or n == 0:
        return n
    else:
        return (cached_execution(cache, cached_fibo, n - 1 )
               + cached_execution(cache,  cached_fibo, n - 2 ))

print cached_execution(cache, cached_fibo,100)
    

