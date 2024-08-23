#SET:
# Set is a  collection of homogeneous and heterogeneous type of data.
# Boundaries of set is {}.
# Set is a unordered data type.
# Set doesn't support indexing and slicing.
# Set doesn't allow duplicates.
# Set is a mutable data type,but elements present inside the set must be immutable.
# Default value of set is SET().

#Ex:
# s={1,10.2,True,2+3j,'hello'}
#s
#{True,1,2+3j,'hello'}

#s={True,1,2+3j,'hello',False,0}
#s
#o/p={False,True,(2+3j),'hello'}

#Set methods:
#1.UNION
#2.INTERSECTION
#3.DIFFERENCE
#4.SYMMETRIC_DIFFERENCE
  
#UPDATE METHOD IS COMMON FOR ALL METHODS.

#1.UNION:

#It is used to combine values present in base set and iterable.
#SYNTAX:
#baseset.union(iterable)

#Ex:
#s1={1,2,3,4}
#s2={3,4,5,6}
#s1.union(s2)
#o/p={1,2,3,4,5,6}


#UPDATE:
#It is used to update the base set,with the values present in base set and iterable.
#SYNTAX:
#Baseset.Update(iterable)

#ex:
#s1={1,2,3,4,5}
#s2={'hello'}
#o/p={1,2,3,4,5.'o','l','h','e'}   



#2.INTERSECTION:
#It is used to return the common elements present in base set and iterable.
#The return type of intersection is SET.
#f there is no common elements are present,it returns DEFAULT VALUE OF SET().

#SYNTAX:
#baseset.intersection(iterable)

#ex:
#s={1,2,3,4}
#s1={3,4,5,6}
#s.intersection(s1)
# o/p={3,4} 

#INTERSECTION_UPDATE:
#It is used to update the base set with the common elements present in base set and iterables.

#SYNTAX:
#baseset.intersection_updatae(iterable)

#ex:
#s={1,2,3,4}
#s1={3,4,5,6}
#s.intersection(s1)
#o/p={3,4}

#3.DIFFERENCE:
#It is used to return uniqye elements preseent in base set.

#SYNTAX:
#baseset.difference(iterable)

#ex:
#s1={1,2,3,4}
#s2={3,4,5,6}
#s1.difference(s2)
#o/p={1,2}

#DIFFERENCE_UPDATE:
#It is used to update the base set with the unique values,present in base set.

#SYNTAX:
#ex:
#s1={1,2,3,4}
#s2={3,4,5,6}
#s1.difference_update(s2)
#s1
#o/p={'hello'}


#4.SYMMETRIC_DIFFERENCE:
#It is used to return the unique value present in base set and iterables.

#SYNTAX:
#baseset.symmetric_difference(s2)

#ex:
#s1={1,2,3,4}
#s2={3,4,5,6}
#s1.symmetric_difference(s2)
#o/p={1,2,5,6}

#SYMMETRIC_DIFFERENCE_UPDATE:
#It is used to update the base set with the unique values,present in base set and iterables.

#SYNTAX:
#baseset.symmetric_difference_update(iterable)

#ex:
#s1={'h','e','hello','l','o'}
#s1.symmetric_difference_update('hello2')
#s1
#o/p={'2','hello'}

#TO ADD AN ELEMENT INTO THE SET:
#1.ADD()
#2.UPDATE()

#1.ADD():
#Add() will add the element randomly.
#It accepts on;y immutable data type.
#It throws type error, if any mutable data type are passed.

#syntax:
#set.add(element)

#ex:
#s={11,22,33,44}
#s.add(55)
#o/p=> {11,22,33,44,55}

#UPDATE():
#It si used to add the element random to a set.
#It will unpack the element and dd to a set.
#It accepts iterable.

#ex:
#s={1,2,3,4}
#s.update('hello')
#o/p=> {1,2,3,4,'h','e','l','l','o'}


#TO REMOVE AN ELEMENTS FROM THE SET:
#1.remove()
#2.Discard()
#3.pop()
#4.clear()

#1.REMOVE():
#It is used to remove the specified element from the set.
#It rises key error,if the specified element is not present in the set.

#SYNTAX:
#set.remove(element)

#ex:
#s={1,2,3,'hello',20}
#print(s)
#{1,2,3,'hello',20}

#DISCARD():
#It is used to remove the specified element from the set.
#It won't throws any error,if the specified element is not present in a specified set.

#SYNTAX:
#set.discard(element)

#ex:
##s={1,2,3,4,5,6}
#s.discard(2)
#o/p=> {1,3,4,5,6}


#POP():
#it is used to remove the specified element from a set.
#it won't accept any arguments.
#it rises error if the set is empty.

#SYNTAX:
#set.pop()

#ex:
#s={1,2,3,4,5,6}
#set.pop()
#o/p=> 1

#CLEAR():

#It is used to remove all the elements from a set.
#It won't accept any arguments.

#syntax:
#set.clear()

#ex:
#s={1,2,3,4,5,6}
#s.clear()


#IS SUPERSET():

#It returns true,if all the values of iterable are present in base set.
#Else it returns false.

#syntax:
#base set.issuperset(iterable)

#ex:
#s={1,2,3,4,5,6}
#s.issuperset(s1)
#o/p=> True

#IS SUBSET():

#it returns true,if all the values of base set are present in a iterable.
#else it returns false.

#SYNtax:
#base set.issubset(iterable)

#ex:
#s={1,2,3}
#s1={2,3,4,5,6,7,1}
#s.issubset(s1)
#True

#IS DISJOINT():
#it returna true ,if base set and iterable contains different elements.

#SYNtax:
#base set.isdisjoint()

#ex:
#s={1,2,3,4}
#s1={5,6,7,8}
#s.isdisjoint(s1)
#True
















































