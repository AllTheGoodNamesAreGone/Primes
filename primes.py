#This is a program to print prime numbers
#Designed by AnirudhCB
import math

in2 = raw_input("Press 1 to check if a number is prime, and press 2 to print primes")


def checkprm(b,prm):
             
    if b%prm ==0:
        return True
    
    else:
        return False
    
    
if in2 =="1":
        x1 = input("Enter the number to check for prime (Above 3)")
        x = int(x1)
        
        h1 = x/2
        math.ceil(h1)
        h1 = int(h1)
        for l in range(h1,2,-1):
            chk = checkprm(x,l)
            
            if chk==True:
                print("Not prime")
                res = False
                break
            else:
                res = True
            
if res ==True:
    print("Is prime")
    
def checkprime2(bx,by):
    if bx%by == 0:
        return True
    else:
        return False
    
    
if in2=="2":
    sz = input("Enter the number until which you want primes to be printed")
    s = int(sz)
    for d in range (2,s):    
        d2 = int(d/2)
        d2 = int(math.ceil(d2))
        
        for l2 in range(d2,1,-1):
            checkprime2(d,l2)
            
            if checkprime2(d,l2) == True:
                break
        if checkprm(d,l2) == False:
                print(d)
                
            
            
        
        
        
        
        
        