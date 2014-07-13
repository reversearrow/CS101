
#  S(n, k) = k*S(n-1, k) + S(n-1, k-1)

def stirling(n,k):
       if n==k :
              return 1
       if k == 1:
              return 1
       if k > n:
              return 0
       else:
              return k*stirling(n-1,k) + stirling(n-1,k-1)
       
       
# B(n) is the sum of S(n,k) for k =1,2, ... , n.


def bell(n):
    total = 0
    for i in range(1,n+1):
          
          total = total + stirling(n,i)
           
    return total
