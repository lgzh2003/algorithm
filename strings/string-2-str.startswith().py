def count_substring(string, sub_string):
    return len([i for i in range(len(string)) if string[i:].startswith(sub_string)])
#https://www.hackerrank.com/challenges/find-a-string?h_r=next-challenge&h_v=zen
