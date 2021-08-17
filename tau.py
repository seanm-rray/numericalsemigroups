def main():
    f=open("C:\\Users\\14842\Desktop\\tau.txt","w") # open the file
    f.write("x\ty\tz\n") # write header row
    n = 50 #set length 
    i = 0
    a = 1
    b = i
    c = int(i*(i-1)/2) # i choose 2
    gens = [] #generator list
    temp = []
    tau = []
    nuni = []
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
        print("checking x =",x)
        for y in range(n+1):
            for z in range(n+1): 
                for [a, b, c] in gens: 
                    if x >= a and y >= b and z >= c and T[x-a][y-b][z-c]:
                        T[x][y][z]=True
                        temp.append([x, y, z])
                        break
    
    
    
    for x in temp:
        if ("("+str(x[1])+","+str(x[2])+")") in nuni:
            continue
        else:
            tau.append([x[0],x[1],x[2]])
            f.write(str(x[0]) + "\t" + str(x[1]) + "\t" + str(x[2]) + "\n")
            nuni.append("("+str(x[1])+","+str(x[2])+")")
    
    
    print(tau)


main()