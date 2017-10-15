###
### template of code for Problem 4 of Problem Set 2, Fall 2008
###

bestSoFar = 0
flag = False
                    # variable that keeps track of largest number
                  # of McNuggets that cannot be bought in exact quantity
packages = (6,9,20)   # variable that contains package sizes
a = 0
b = 0
c = 0
for n in range(1, 150):
    # only search for solutions up to size 150
    ## complete code here to find largest size that cannot be bought
    ## when done, your answer should be bound to bestSoFar
    for a in range(0,25):
        for b in range(0,22) :
            for c in range(0,8) :  ##exhaustive enumeration to test all valid combination which satisfy the condition.
                if (6*a + 9*b + 20*c) == n :   ##nested loop flag checks wether any combiantion fullfill the condition
                    flag = True
    if flag == False :                ## if any number which cant be satisfy by any value of abc then bestsofar record that number
        bestSoFar = n
    flag = False
                
if n == 149:               ##atlast trying all in range 1-150 largest bestsofar printed here.
    print('Largest number of McNuggets that cannot be bought in exact quantity:'+ str(bestSoFar))
                
    

    
