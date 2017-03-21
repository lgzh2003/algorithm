##set
A set is an **unordered** collection of items. Every element is **unique (no duplicates)** and must be immutable (which cannot be changed).            
             
**How to create or initiate a set?** a = set()                               
```
>>> se = {'a','b',1}
>>> type(a)
<type 'set'>

>>> a = set()
>>> a
set([])
>>> type(a)
<type 'set'>
```                 
            
**How to change a set in Python?**se.add(one element), se.update(a bunch of elements)             
```
>>> se = set()
>>> se.add('a')
>>> se
set(['a'])
>>> se.update(['b','c','d'])
>>> se
set(['a', 'c', 'b', 'd'])
>>> se.update([1,2,3],[4,5,6])
>>> se
set(['a', 1, 'c', 'b', 4, 'd', 6, 2, 3, 5])
```          
        
**How to remove elements from a set?**           
```
se.discard(one element)#if the item does not exist in the set, it remains unchanged
se.remove(one element)#with error message when not find
se.clear()#clear all
```        
          
**Python Set Operations**              
- A**&**B             
- A**|**B           
- A**-**B (Difference of A and B (A-B) is a set of elements that are only in A but not in B.)                                                                 
- A**^**B (Symmetric Difference of A and B is a set of elements in both A and B except those that are common in both.)                               
```
>>> a = {1,2,3,4,5}
>>> b = {3,4,5,6,7}
>>> a&b
set([3, 4, 5])
>>> a|b
set([1, 2, 3, 4, 5, 6, 7])
>>> a-b
set([1, 2])
>>> a^b
set([1, 2, 6, 7])
```           
               
**Built-in Functions with set**                       
Built-in functions like all(), any(), **enumerate()**, len(), max(), min(), sorted(), sum() etc. are commonly used with set to perform different tasks.               
```
>>> a = set()
>>> a.update((1,2,3,4,5,6,7))
>>> a
set([1, 2, 3, 4, 5, 6, 7])
>>> [j for i,j in enumerate(a)]
[1, 2, 3, 4, 5, 6, 7]
```       
         
**Python Frozenset**            
**tuples are immutable lists, frozensets are immutable sets.** Sets being mutable are unhashable, so they can't be used as dictionary keys. On the other hand, frozensets are **hashable** and can be used as keys to a dictionary. Frozensets can be created using the function frozenset()                 
       
                
      
                       
            
      
         
         

