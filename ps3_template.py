from string import *

def countSubStringMatch(target,key):
    count = 0
    for i in range(int(len(target))):
        if target[i:len(key)+ i] == key :
            count = count + 1
    return count

def countSubStringMatchRecursive(target,key,count = 0):
    if len(target) < 1 : return count
    if target[:len(key)] == key :
        #print(target)
        return countSubStringMatchRecursive(target[1:],key,count + 1)
    return countSubStringMatchRecursive(target[1:],key,count)

def subStringMatchExact(target,key) :
    count = 0
    result = ()
    for i in range(int(len(target))):
        if target[i:len(key)+ i] == key :
            result = result + (i,)
            count = count + 1
    return result

# this is a code file that you can use as a template for submitting your
# solutions


# these are some example strings for use in testing your code

#  target strings

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

# key strings

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'



### the following procedure you will use in Problem 3


def subStringMatchOneSub(key,target):
    """search for all locations of key in target, with one substitution"""
    allAnswers = ()
    for miss in range(0,len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        print 'breaking key',key,'into',key1,key2
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1,match2,len(key1))
        allAnswers = allAnswers + filtered
        print 'match1',match1
        print 'match2',match2
        print 'possible matches for',key1,key2,'start at',filtered
    return allAnswers
        



    







            



