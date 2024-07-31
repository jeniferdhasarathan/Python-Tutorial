#LIST:

# It is  collection data type.
# It is a collection of homogeneous and heterogeneous.
# HOMOGENEOUS - SAME DATA TYPE.
# HETEROGENEOUS - DIFFERENT DATA TYPE.
# Boundaries of list are [] square brackets.
# List is a ordered data type.
# List supports indexing and slicing.
# List allows duplicates.
# List is a mutable data type.
# Default value of list is empty square brackets [].

#Example:
#list=[1,2,3,4,5]
#type(list)
#o/p=<class 'list'>


#list=['hi','hello',10+3j,True,10,23]
#list[3]
#o/p = True


#list=[1,2,3,4,5,'hello','hi',True,'monday']
#list[4]
#o/p = 5

#MEMORY MANAGEMENT IN LIST: 

  #In list, the memory management is simple and easy to understand.
  #It stores data in a  sequence of memory or sequence of blocks.
  #The indexing should be start from 0.
  
#MODIFICATION OF LIST:
  
  #syntax:
           #list[index]=value

#EXAMPLE:
#list=[1,2,3,'hello',True,10+2j,4,5,6]
#list[2]=33

#LIST METHODS:
#1.Append()
#2.Extend()
#3.Insert()

#1.Append():
#It is use to add at last.
#Append will accept only one argument.
#We can pass collection and individual data types.

#syntax:
       #list.Append(individual/collection)

#Example:
#list=[1,2,3,4,6]
#list.append(5)
#o/p=[1,2,3,4,6,5]
  

#EXTEND:
#It is used add the element at the last
#It accepts only one arguments.
#It will unpack the given elements and add to the list.
#It will unpack only once.
#It accepts only collection data types as an argument.

#syntax:
    # list.extend(collection)

#Example:
#list=[1,2,3]
#list.extend('hello')
#o/p=[1,2,3,'hello','h','e','l','l','o']   


