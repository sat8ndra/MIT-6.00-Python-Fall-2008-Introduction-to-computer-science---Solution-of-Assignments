def makeSet(s):
    assert type(s) == str
    res = ''
    for c in s:
        if not c in res:
            res = res + c
        print res
    
    return res
