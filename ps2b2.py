###
### template of code for Problem 4 of Problem Set 2, Fall 2008
###

bestSoFar = 0
flag = False
                    # variable that keeps track of largest number
                  # of McNuggets that cannot be bought in exact quantity
packages = (10,20,30)   # variable that contains package sizes
a = 0
b = 0
c = 0
for n in range(0, 200):
    # only search for solutions up to size 150
    ## complete code here to find largest size that cannot be bought
    ## when done, your answer should be bound to bestSoFar
    for a in range(0,200):
        for b in range(0,200) :
            for c in range(0,200) :
                if (packages[0]*a + packages[1]*b + packages[2]*c) == n :
                    flag = True
                if flag == True :   ##so many break used for immediately exiting after finding correct combination so that loop rapidly exit for next n 
                    break
            if flag == True :
                break
        if flag == True :
            break            
    if flag == False :    ## stores the n which has no solution.
        bestSoFar = n
    flag = False    ## reset to default false for next iteration.
    print("Given package sizes "+ str(packages[0]) + ", " + str(packages[1]) + ", and " + str(packages[2]) + ", the largest number of McNuggets that cannot be bought in exact quantity is:" + str(bestSoFar))
                
    

    
