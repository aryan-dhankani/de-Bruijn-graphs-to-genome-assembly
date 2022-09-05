from enum import unique
import sys, os

f = open ("strings.txt", "r")
f1 = f.read()
listm = f1.split('\n')
f.close()


print (listm)

#print unique two-mers or k mers 

k = len (listm[0]) - 1
print("length of every unique kmer is :" , k)


i=0
kmers = []
while i<len(listm):
    print (listm[i])
    kmers.append(listm[i][0:k])
    kmers.append(listm[i][k-1: k+1])
    i = i+1

print(kmers)

unique_kmers = [*set(kmers)]
print(unique_kmers)


#making matrix of 2-mers with additional ACTG they need to make required 3mer

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


print (arr)

ans = ""

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

ans += unique_kmers[start]

m = 0

while(m < 4) :
    if(arr[start][m] != -1) :
        x = arr[start][m]
        arr[start][m] = -1
        start = x
        ans += unique_kmers[start][-1]
        m = 0
    else :
        m +=1 
    
print(ans)