##string in python
     
###Build in functions         
       
- str.index(x)index of the first occurrence of x in s           	 
- str.count(x)total number of occurrences of x in s              
- str.capitalize() Return a copy of the string with its **first character capitalized and the rest lowercased**.                
- str.find(sub[, start[, end]]) Return the lowest index in the string where substring sub is found within the slice s[start:end].Return **-1 if sub is not found.**          
- str.rfind(sub[, start[, end]]) Return the highest index in the string where substring sub is found. Return -1 on failure.
- str.rindex(sub[, start[, end]]) Like rfind() but raises ValueError when the substring sub is not found.                      
- str.isalnum() Return true if all characters in the string are **alphanumeric(alpha+number)** and there is at least one character, false otherwise.                     
```
>>> '34%231'.isalnum()
False
>>> '34a231'.isalnum()
True
```          
- str.isalpha() Return true if all characters in the string are **alphabetic** and there is at least one character, false otherwise.                  
- str.isdigit() Return true if all characters in the string are **digits** and there is at least one character, false otherwise.            
- str.islower() Return true if all cased characters in the string are **lowercase** and there is at least one cased character, false otherwise.          
- str.isupper() Return true if all cased characters [4] in the string are **uppercase** and there is at least one cased character, false otherwise.                
- str.isspace() Return true if there are **only whitespace characters** in the string and there is at least one character, false otherwise.          
- str.istitle() Return true if the string is a **titlecased('Hello World')** string and there is at least one character, Return false otherwise.          
- str.join(iterable) Return a string which is the concatenation of the strings in the iterable iterable. The separator between elements is the string providing this method.                 
```
>>> l = ['max','Lili','Kobe']
>>> ','.join(x for x in l)
'max,Lili,Kobe'
```                      
- str.lower() Return a copy of the string with **all the cased characters converted to lowercase**.           
- str.upper() Return a copy of the string with **all the cased characters converted to uppercase**.             
- str.replace(old, new[, count]) Return a copy of the string with all occurrences of substring old replaced by new. If the optional argument count is given, only the first count occurrences are replaced.                                    
```
'maxismax'.replace('max','kebi')
'kebiiskebi'
>>> 'maxismax'.replace('max','kebi',1)
'kebiismax'
>>> 'maxismax'.replace('max','kebi',2)
'kebiiskebi'
```           
- str.split([sep[, maxsplit]]) Return a list of the words in the string, using sep as the delimiter string. If maxsplit is given, at most maxsplit splits are done (thus, the list will have at most maxsplit+1 elements).             
- str.splitlines([keepends]) Return a list of the lines in the string, breaking at line boundaries. This method uses the universal newlines approach to splitting lines. Line breaks are not included in the resulting list unless keepends is given and true.                                                      
```
>>> 'str\nmax\nhehe'.split('\n')
['str', 'max', 'hehe']
>>> 'str\nmax\nhehe'.splitlines()
['str', 'max', 'hehe']
```           
- str.startswith(prefix[, start[, end]]) Return True if string starts with the prefix, otherwise return False.             
```
>>> 'maxishere'.startswith('max')
True
>>> 'maxishere'.startswith('Max')
False
```          
- str.swapcase() Return a copy of the string with uppercase characters converted to lowercase and vice versa.                
- str.title() Return a titlecased version of the string where words start with an uppercase character and the remaining characters are lowercase.           
```
>>> 'max is here always'.title()
'Max Is Here Always'
>>> 'max 1here is 2always'.title()
'Max 1Here Is 2Always'
```                    
                    
###Cool method    
####str.translate(table[, deletechars])
Return a copy of the string where all characters occurring in the optional argument deletechars are removed, and the remaining characters have been mapped through the given translation table, which must be a string of length 256. You can use the **maketrans() helper function in the string module** to create a translation table. For string objects, set the table argument to None for translations that only delete characters:            
**example 1: swap characters**                                           
```
from string import maketrans   # Required to call maketrans function.

intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)

str = "this is string example....wow!!!";
print str.translate(trantab)
```              
**example 2: delete characters(str.translate(None,'aeiou'))**                                           
```
>>> 'I am so happy to see U'.translate(None,'aeiou')
'I m s hppy t s U'

```               
        
             

   
      


             




