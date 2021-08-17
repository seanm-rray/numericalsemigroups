def main():
    f=open("C:\\Users\\14842\Desktop\\xyz.txt","w") # open the file
    f.write("x\ty\tz\n") # write header row
    n = 100 #set length 
    i = 0
    a = 1
    b = i
    c = int(i*(i-1)/2) # i choose 2
    gens = [] #generator list
    T=[[[False for k in range(n+1)] for j in range(n+1)] for i in range(n+1)]
    T[0][0][0] = True
    

    
    while c <= n: #fill generator list
        gens.append([a, b, c])
        f.write(str(a) + "\t" + str(b) + "\t" + str(c) + "\n") # write header row
        T[a][b][c] = True
        i = i + 1
        b = i
        c = int(i*(i-1)/2) # i choose 2
    
    for x in range(n+1): 
        for y in range(n+1): 
            for z in range(n+1): 
                for [a, b, c] in gens: 
                    if x >= a and y >= b and z >= c and T[x-a][y-b][z-c]:
                        T[x][y][z]=True
                        f.write(str(x) + "\t" + str(y) + "\t" + str(z) + "\n")
                        print(x,y,z)
                        break

    print(gens)
    print(T)
main()
                        
 
 

 
    
        



