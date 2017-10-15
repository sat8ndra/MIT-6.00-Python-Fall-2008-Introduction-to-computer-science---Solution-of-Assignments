from string import *

def countSubStringMatch(target,key):
    count = 0
    for i in range(int(len(target))):     ## find the key word in length of the target by incrementing one by one and matching
        if target[i:len(key)+ i] == key :
            count = count + 1
    return count


def countSubStringMatchRecursive(target,key,count = 0):   ## this is same in this recursive way the problem is solved in every
                                                    ## recursion the target string is reduces by first one letter and at last
    if len(target) < 1 : return count          ## if target string reduces to 0 size then count is returned
    if target[:len(key)] == key :
        #print(target)
        return countSubStringMatchRecursive(target[1:],key,count + 1)   ## when target is matched the count increment and target statement reduces by one
    return countSubStringMatchRecursive(target[1:],key,count)  ## if target is not matched then count remain same and target statement reduce one
    
def subStringMatchExact(target,key) :
    count = 0
    result = ()
    for i in range(int(len(target))):    ## serial wise statement compares and at last tuple of number where statement matches return
        if target[i:len(key)+ i] == key :
            result = result + (i,)
            count = count + 1
    return result

def constrainedMatchPair(firstMatch,secondMatch,length):
    





            



