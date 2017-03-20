if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    arr.sort()
    arr.reverse()
    maxNum = max(arr)
    for x in arr:
        if x!=maxNum:
            print x
            break
#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list?h_r=next-challenge&h_v=zen
