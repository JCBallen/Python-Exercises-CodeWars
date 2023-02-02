def solution(array_a, array_b):
    ans=[]
    for idx,i in enumerate(array_a):
        ans.append(abs(array_a[idx]-array_b[idx])**2)
    prom=sum(ans)/len(ans)
        
    return prom
    
    
    
a1 = [1,2,3]
a2 = [4,5,6] 
solution(a1, a2)
