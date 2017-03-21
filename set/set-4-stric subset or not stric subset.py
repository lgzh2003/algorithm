setA = set(map(int, raw_input().split()))
N = int(input())
for i in range(N):
    set1 = set(map(int, raw_input().split()))
    if set1 & setA != set1 or set1 & setA == setA:
        print False
        exit()
print True;
#https://www.hackerrank.com/challenges/py-check-strict-superset
