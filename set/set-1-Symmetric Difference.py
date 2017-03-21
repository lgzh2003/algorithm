M = int(input()) 
first = set(map(int, raw_input().split()))
N = int(input())  
second = set(map(int, raw_input().split()))
l = sorted(first^second)
for x in l:
    print x
#https://www.hackerrank.com/challenges/symmetric-difference
