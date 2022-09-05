import sys , os
if not os.path.exists("input.txt"):
    print("Input File not Found")
    sys.exit(0)
else :
    f1 = open("input.txt", "r")
    list1 = list(f1.read().split())
    f1.close()
    
    print(list1)
    k = len(list1[0]) - 1 
    while k>0 :
        i = 0
        while i < len(list1) :
            j = 0
            while j < len(list1) :
                if i == j :
                    j += 1
                elif list1[i][-k:]==list1[j][0:k] :
                    list1[i] = list1[i]+list1[j][k:]
                    del list1[j]
                    i -= 1
                    break
                else :
                    j +=1 
            i += 1
        k -= 1        
            
                
    print(list1)
    ans = ''.join(list1)
    print(ans)
               

