import math
import itertools
def retsemi(A): #returns a numerical semigroup of A
    B = []
    count = 0
    stop = 0
    for i in A:
            if i == True:
                B.append(count)
                count = count + 1
                stop = stop + 1
            else:
                stop = 0
                count = count + 1
    #print (B)
    return B


def retbool(A): #Returns the numerical semigroup in a list of booleans
    B = []
    count = 0
    numer = [0]
    stop = 0

    while stop < A[0]:    
        for i in A:    
            if (count - i) in numer:   
                B.append(True)
                numer.append(count)
                count = count + 1
                stop = stop + 1 
                break

            elif i == A[-1]:
                B.append(False)
                stop = 0
                count = count + 1
    numer.pop(0) #Removes 0    
    #print(B)
    return B

def retgap(B): #Returns the gapset of B, a list of booleans
    gapset = []
    count = 0

    for i in B:
        if i == False:
            gapset.append(count)
            count = count + 1
        else:
            count = count + 1
    
    gapset.pop(0) #Removes 0
    #print(gapset)
    return gapset

def retmin(boo):
    numer = retsemi(boo)
    numer.reverse()
    count = 0
    for i in range(1, len(numer)):
        for j in range(1, len(numer)):
            diff = numer[count]-numer[j]
            if diff in numer:
                del numer[count]
                break
            else:
                if j == (len(numer) - 1):
                    count = count + 1 
    numer.sort()
    return numer
    

def main():
    file = open("C:\\Users\\14842\Desktop\\testfile.txt","w")
    file.write("Gen\tGen\tGen\tGap Set\tGenus\tFrobenius\tMinSet\tEmbedded\n")

    A = ([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    genlist = []
    semilist = []
    for comb in itertools.combinations(A, 3): #Finds all combinations of 3 for generators
        if (math.gcd(comb[0], math.gcd(comb[1], comb[2]))) == 1: #Eliminates all groups besides where gcd = 1
            genlist.append(comb)
            semilist.append(retsemi(comb)) #Returns the numerical semigroup for each set of generators

    for i in genlist:
        file.write(str(i[0]))
        file.write("\t")
        file.write(str(i[1]))
        file.write("\t")
        file.write(str(i[2]))
        file.write("\t")
        file.write(str(retgap(retbool(i))))
        file.write("\t")
        file.write(str(len(retgap(retbool(i)))))
        file.write("\t")
        file.write(str(retgap(retbool(i))[-1]))
        file.write("\t")
        file.write(str(retmin(retbool(i))))
        file.write("\t")
        file.write(str(len(retmin(retbool(i)))))
        file.write("\n")
    file.close 

    

    

main()
    

        
    
        
