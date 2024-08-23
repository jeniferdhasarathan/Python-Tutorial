#DICTIONARY:

#Dictionary is a collection of key and value pair.
#keys and values are separated by colon.
#keys and value pairs are separated by comma(,).
#it is an ordered data type.
#it does not support indexing and slicing.
#Duplicate keys are allowed but duplicate values are not allowed.
#Keys must be immutable data type.But values can be any python data type.
#Dictionary   is a mutable data type.
#Boundaries of dictionary is curly bracket{}.
# Default value of dictionary is empty curly bracket{}.
# To access the value ,we need to use keys.
# 
# SYNTAX:
#        {key:value,key:value} 

#ex:
#dic={'a':1,'b':2,'c':3}
#dic['a']
#o/p=> 1

#ACESSING AND MODIFICATION OF DICTIONARY:
#
#To access the value:
#dic[key]

#dic[key] - Raises rises key error if key is not present.

#dic[key]=value - Update the value if key present else, it will add key and value pair.

#dic={'a'=1,'b'=2}
#dic[a]
#o/p= 1

#DICTIONARY METHODS:
#1.keys()
#2.values()
#3.items()

#1.KEYS():
#It is used to return list of keys present in a dictionary.
#It won't accept any arguments.
#Return type of keys is dict_keys().
# 
# syntax:
#   dic.keys()

#ex:dic={'a':1,'b':2,'c':3}
# dic.keys()
# o/p=(['a','b','c']}

# 2.VALUES():
#It is used to return the list of values present in a dictionary.
#it won't accept any arguments. 
#  return type is dict_values().

#syntax:
#dic.values()

#ex:
#dic={'a':1,'b':2,'c':3}
# dic.values()
#o/p=([1,2,3])

#ITEMS():
#It is used to return a tuple of key and values present in a dictionary.
#It won't accept any arguments.
#return type of items() is dict_items().

##syntax:
#dic.items()

#ex:
#dic={'a':1,'b':2,'c':3}
#dic.items()
#o/p=>([('a',1),('b',2),('c',3)])

#GET():
#It is used to get the values of a specified key.
#It return the value,which is present in a specified key else,it return NONE.
#get method accept two arguments.
#1.keys
#2.default value
#If the key is present ,it returns the value ,else it return default value.

#syntax:
#dic.get(key,[default_value])

#ex:
#dic={'a':1,'b':2,'c':3}
#dic.get('c')
#o/p=> 3

#UPDATE():
#It is used to update the specified key,value to a new value ,if the key is present.
#If key is not present ,it eill add at last.
#It accept only dictionary as an input.

#syntax:
#dic.update({iterable})

#ex:
#dic={'a':1,'b':2,'c':3}
#dic.update({'a':111})
# o/p=> {'a':111,'b':2}
# 
# TO REMOVE AN ELEMET FROM A DICTIONARY:
# 
# 1.POP()
# 2.POPITEM() 
# 3.CLEAR() 

#1.POP():

#It is used to remove key anad value pair from a dictionary.
#It return the value,which got removed.
#It rises key error,if the specified key is not present in the dictionary.

#syntax:
#dic.pop(key)

#ex:
#dic={'a':1,'b':2,'c':3}
#dic.pop('a')
#dic
#{'b':2,'c':3}

#POP ITEM():

#It is used to remove the last key and value pair present in a dictionary.
#it returns tuple(key,value pair).
#it won't accept any argument.

#syntax:
#dic.popitem()

#ex:
#dic={'a':1,'b':2,'c':3}
#dic.popitem()
#('c',3)

#3.CLEAR():
#It is used to empty the dictionary.
#It won't accept any arguments.

##syntax:
#dic.clear()

#ex:
#dic={'a':1,'b':2,'c':3}
#dic.clear()
#o/p=> {}

#SET DEFAULT():
#It is a method ,which is used dto add a key with a default value as none.
#it accepts two arguments.
#1.key
#2.value

#It eturn the value which are passing to specific key.
#If the key is exists,it won't update the key instead it return the original value of the key.

##syntax:
#dic.set(key,[value])

#ex:
#dic={'a':1,'b':2}
#dic.setdefault('c')
#o/p=>{'a':1.'b':2,'c':NONE}

#FROM KEYS()
#It is used to create a dictionary using a collection datat type.
#It creates a dictionary of keys as an elements present in a collection,and defaultly it assign none as a value.

#syntax:
#dic.fromkeys(values)

#ex:
#list=['pubg','ludo','carrom','free fire']
#fromkeys(list)
#o/p=>{'pubg':NONE,'ludo':NONE,'carrom':NONE,'free fire':NONE}


