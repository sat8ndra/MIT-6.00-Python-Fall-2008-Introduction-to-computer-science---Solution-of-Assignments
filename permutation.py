from itertools import permutations
hand = {'i': 2, 'q': 2, 'z': 1, 'w': 1, 'h': 1}
##for i in range(0, len(hand)+1):
##        for subset in permutations(stuff, i):
##               print(subset)

points_dict = {'zqw':456}
def pick_best_word(hand, points_dict):
##"""
##Return the highest scoring word from points_dict that can be made with the
##given hand.
##Return '.' if no words can be made with the given hand.
##choose first from points_dict then check it satisfy hand then check second
##"""
    
    best_until = 0
    temp = "."
    word = ""
    for i in range(0, len(hand)+1):
        for subset in permutations(hand, i):
                word = ''.join(subset)
                print word
                if (points_dict.has_key(word) and best_until >= points_dict(word)) :
                    temp = word
                    best_until = points_dict(word)
                    print temp
                    print best_until
        
    return temp
                        
