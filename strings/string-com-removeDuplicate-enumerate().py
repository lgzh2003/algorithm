def merge_the_tools(string, k):
    # your code goes here
    times = len(string)/k
    l = []
    for i in range(times):
        s = string[i*k:(i+1)*k]
        print ''.join([j for i,j in enumerate(s) if j not in s[:i]])
#https://www.hackerrank.com/challenges/merge-the-tools?h_r=next-challenge&h_v=zen
