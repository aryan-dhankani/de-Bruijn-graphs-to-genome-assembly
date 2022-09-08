from enum import unique
import sys, os

f = open ("cyclicseq.txt", "r")
f1 = f.read()
listm = f1.split('\n')
f.close()


print ("List of  k+1 mers : ", listm , "\n")

#print unique two-mers or k mers 

k = len (listm[0]) - 1
print("length of every unique kmer is : " , k , "\n")


i=0
kmers = []
while i<len(listm):
    #getting all (non-unique) k mers from k+1 mers
    kmers.append(listm[i][0:k])
    kmers.append(listm[i][k-1: k+1])
    i = i+1


#picking out unique kmers
unique_kmers = [*set(kmers)]
print("list of unique kmers :  " , unique_kmers , "\n")


#making matrix of k-mers with additional ACTG they need to make required k+1mer

rows = 4
columns = len(unique_kmers)

arr = [ [ None for y in range( 4 ) ] for x in range( len(unique_kmers) ) ]

nucleotides = ['A' , 'C' , 'T' , 'G']

for i in range(0 , len(unique_kmers)):
    for j in range (0 , 4):
        item = unique_kmers[i] + nucleotides[j]
        if item in listm:
            item2 = unique_kmers[i][1:] + nucleotides[j]
            arr[i][j] = unique_kmers.index(item2)
        else :
            arr[i][j] = -1

#Our Required Matrix :
print ("Matrix thus formed" ,arr , "\n")

uniq_inds = set()

start_float = len(unique_kmers)*(len(unique_kmers) -1 )/2

for i in range(len(arr)) :
    for j in range(4) :
        if(arr[i][j] == -1) :
            continue
        else :
            uniq_inds.add(arr[i][j])

for val in uniq_inds :
    start_float -= val



# start is index to start our traversal from

start = int(start_float)

ans = ""

ans += unique_kmers[start]
m = 0
add_at = 2
flag = True
storage = []
while(flag) :
    print("index to start with :  " , start)
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
    
    ans = ans[0 : add_at] + temp + ans[add_at :]
    print("ans at this stage :  " , ans , "\n")
    flagtrigger = len(storage)*4
    print("Visited array at this stage : ", storage , "\n") 
    
    
    for i in range(len(storage)):
        for j in range(4) :
            if arr[storage[i]][j] != -1 :
                add_at = i
                start = storage[i]
                break #breaks the loop when finds another path and sets variables for another traversals
            else :
                flagtrigger -= 1 
                
    # When all the values are set to null flagtrigger becomes 0 , thus triggering our flag to be false
    
    m = 0 
    
    if(flagtrigger == 0) : 
        flag = False
    
print("\n" ,"The Shortest substring  :  " , ans , "\n")