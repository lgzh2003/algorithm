**remove duplicate character in string** 
method-1: use enumerate(s)             
```
def removeDuplicate(string):
    return ''.join([j for i,j in enumerate(string) if j not in string[:i]])
```                          
Explaination:           
```
>>> for i,j in enumerate(string):
...     print i,j 
0 h
1 e
2 h
3 e
4 h
5 e
6 h
7 e
8 h
9 s
10 d
11 e
12 d
13 w
14 e
15 d
16 e
17 d
18 w
19 e
```           
method-2: use set() however, this method is not in its orginal order                       
```
def removeDuplicate(string):
    return ''.join(set(string))
```            
Explaination:                          
```
>>> set(string)
set(['h', 's', 'e', 'd', 'w'])
```          
             
Java Solution:                           
```
public static void main(String[] args)
  {
    String s = "aabbaabbcdc";
    StringBuilder sb = new StringBuilder();
    boolean[] seen = new boolean[256];
    for(int i = 0 ; i < s.length(); i++){
      if(!seen[(int)s.charAt(i)]){
      	seen[(int)s.charAt(i)] = true;
        sb.append(s.charAt(i));
      }
    }
    System.out.println(sb.toString());
  }
```
          

