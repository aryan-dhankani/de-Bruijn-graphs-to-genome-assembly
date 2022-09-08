from enum import unique
import sys, os

f = open ("cyclicseq.txt", "r")
f1 = f.read()
listm = f1.split('\n')
f.close()


print ("List of  k+1 mers  ", listm)

#print unique two-mers or k mers 

k = len (listm[0]) - 1
print("length of every unique kmer is :" , k)


i=0
kmers = []
while i<len(listm):
    #getting all (non-unique) k mers from k+1 mers
    kmers.append(listm[i][0:k])
    kmers.append(listm[i][k-1: k+1])
    i = i+1

print(kmers)

#picking out unique kmers
unique_kmers = [*set(kmers)]
print("list of unique kmers :" , unique_kmers)


#making matrix of k-mers with additional ACTG they need to make required k+1mer

rows = 4
columns = len(unique_kmers)

arr = [ [ None for y in range( 4 ) ] for x in range( len(unique_kmers) ) ]

actg = ['A' , 'C' , 'T' , 'G']

for i in range(0 , len(unique_kmers)):
    for j in range (0 , 4):
        item = unique_kmers[i] + actg[j]
        if item in listm:
            item2 = unique_kmers[i][1:] + actg[j]
            arr[i][j] = unique_kmers.index(item2)
        else :
            arr[i][j] = -1

#Our Required Matrix :
print (arr)

numu = set()

sumasfloat = len(unique_kmers)*(len(unique_kmers) -1 )/2

for i in range(len(arr)) :
    for j in range(4) :
        if(arr[i][j] == -1) :
            continue
        else :
            numu.add(arr[i][j])

for val in numu :
    sumasfloat -= val

print("index to start with : " , int(sumasfloat))

# start is index to start our traversal from

start = int(sumasfloat)

ans = ""
temp = ""
ans += unique_kmers[start]

cunt = 0
m = 0
addidx = 0
flag = True
storage = []
while(flag) :
    storage = []
    temp = ""
    while(m < 4) :
        if(arr[start][m] != -1) :
                x = arr[start][m]
                arr[start][m] = -1
                storage.append(x)
                start = x
                temp += unique_kmers[start][-1]
                m = 0
        else :
                m +=1 
    
    print(temp , storage) 
               
    if len(ans) == k :
        ans = ans + temp
    else :   
        cunt = len(storage)*4
        
        for i in range(len(storage)) :
            for j in range(4) : 
                      
                if arr[storage[i]][j] != -1 :
                    ans = ans[0:2+addidx] + temp +  ans[2+addidx:]
                    addidx = i
                    start = storage[i]
                    
                else :
                    cunt -= 1
        if(cunt == 0) :
            flag = False
    print("flagloop end")
    
print(ans , storage)