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


#INSERT:

#It is used to add the element in specific index.
#if the specified index is not present,it will add the element at last.
#it accets two arguments:
 #1.index or position
 #2.value or object.

#syntax:
# list.insert(imdex,value)

#example:
# lst=[1,2,3,4,5]
# lst.insert(2,22)
# o/p=[1,2,22,3,4,5]
 
#TO REMOVE ELEMENT FROM LIST:
#      1.REMOVE()
#      2.POP()
#      3.CLEAR()

#1.REMOVE:
#   It is used to remove the first occured specified element from the list.
#   It rises value error,if the specified element is not present in the list.
#   It rises type eror if no argument is given.
#   It returns NONE.

#syntax:
#    list.remove(value)

#lst=[1,2,3,4,5]
#lst.remove(4)
#o/p=[1,2,3,5]

#pop:
#It is used to remove the element based on index.
#It returns the element which is removed.
#It rises index error ,ifv the specified index is not present in the list.
#It rises index error,if the given list is empty.
#By default,pop will remove last element.
#It accepts only one arguments.

#syntax:
# list.pop(index/position)

#EXAMPLE:
#lst=[1,2,3,4,5]
#lst.pop(3)
#o/p=[1,2,4,5]

#CLEAR:

#It is used to remove all the elements from a list.
#It won't accept any arguments.
#Boundaries of list will present but the values will get removed.

#syntax:
# list.clear()

#EXAMPLE:
# lst=[1,2,3,4,5]
# lst.remove()
#o/p=none