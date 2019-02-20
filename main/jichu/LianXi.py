from typing import Set

my_set={1,2,3,4}
set1 ={4,5,6,7,1}
set2={4,5,6,7,78,9,"java"}
print (my_set.union(set1))
print (set2.difference(set1))
print (set1.difference(set2))
print (set2.symmetric_difference(set1))
print (set1.intersection(set2))
set2.discard(7)
print (set2)
set2.discard("jav")
print (set2)
set2.remove(78)
print (set2)
b="java"+" "+"python"
a="love"
print (b)





#第2题

a=2.918
b=int(a)
print(b)

#第3题
a:int=18;
print(bin(a))
#第4题
a='Python is popular'
b=a.replace('Python','java')
assert isinstance(b, object)
print(b)

#第5题
a={1,2,3,4,5,6,7,10,8,}
for m in a:
   if m%2==0:
     print(m)



