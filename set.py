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