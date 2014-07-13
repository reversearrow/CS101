#Spreading Udaciousness

#Model to teach everyone in the world how to program

#Inputs :
#1. Convince a number
#2. Spread
#3.


def hexes_to_udaciousness(n, spread, target):
 
   
    if n >= target:
      return 0
 
    else:
      return 1 + hexes_to_udaciousness(n+(n*spread),spread,target)
