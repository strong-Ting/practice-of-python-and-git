import math
def estimate_pi():
    k=0
    now_k = 1
    sum_k = 0
    factor = (2*math.sqrt(2)) / 9801
    while abs(now_k) > (1e-15):
        num = fac(4*k)*(1103+26390*k) 
        den = (fac(k)**4)*(396**(4*k))
        now_k = num /den
        now_k = now_k * factor
        sum_k = sum_k + now_k
        k = k+1
        
    return 1/sum_k,now_k ,k

def fac(num):
    if num == 0:
        return 1
    else:
        n = 0
        ans =1
        while num > 0 :
            n = n +1 
            num = num -1
            ans = ans * n   
        return ans 


print(estimate_pi())
print(math.pi)
#if 1/estimate_pi() == math.pi :
 #   print("the same")
#else:
 #   print("no")
