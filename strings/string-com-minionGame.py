def minion_game(string):
    # your code goes here
    st = 0
    ca = 0
    n = len(string)
    for i in range(n):
        if string[i] in 'AEIOUaeiou':
            ca+=(n-i)
        else:
            st+=(n-i)
    if ca>st:
        print 'KEVIN',ca
    elif st>ca:
        print 'Stuart',st
    else:
        print 'Draw'

#https://www.hackerrank.com/challenges/the-minion-game
