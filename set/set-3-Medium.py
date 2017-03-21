# Enter your code here. Read input from STDIN. Print output to STDOUT
length = map(int,raw_input().split())
l1 = map(int,raw_input().split())
setA = set(map(int,raw_input().split()))
setB = set(map(int,raw_input().split()))
print len([x for x in l1 if x in setA])-len([x for x in l1 if x in setB])
#https://www.hackerrank.com/challenges/no-idea
