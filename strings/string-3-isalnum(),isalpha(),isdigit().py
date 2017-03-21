if __name__ == '__main__':
    s = raw_input()
    print len([x for x in s if x.isalnum()])>0
    print len([x for x in s if x.isalpha()])>0
    print len([x for x in s if x.isdigit()])>0
    print len([x for x in s if x.islower()])>0
    print len([x for x in s if x.isupper()])>0
#https://www.hackerrank.com/challenges/string-validators?h_r=next-challenge&h_v=zen
