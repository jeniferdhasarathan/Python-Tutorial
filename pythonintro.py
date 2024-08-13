#PYTHON:

#HIGH LEVEL LANGUAGE:
#The language which can be understandable by humans are called high level language.

#LOW LEVEL LANGUAGE:
#The language which can be understandable by machines is known as low lwvel language.

#WHAT IS PYTHON?
#Python ia general purpose,high level programming language which was introduced by GUIDO VAN ROSSUM in 1990,
# but released in the year 1991-feb-20.

#Features:
#easy syntax
#user friendly
#general purpose language
#high level language.
#platform independent.
#Automatic garbage collector.
#It supports oops.
#Pyhton is DYNAMICALLY TYPED LANGUAGE.
#Python supports DYNAMIC MEMORY ALLOCATION.
#Python is interpreter programming language.

#IDENTIFIER:
# Identifier is user defined name which is given for an object(class,function,variables etc.)

#RULES OF IDENTIFIER:
# RULE 1: Identifier should start with alphabets or numbers.
# RULE 2: Identifier can have the numbers but it shouldn't start with numbers.
# RULE 3: No other special characters are allowed except underscore(_).
# RULE 4: Identifier can have unlimited length but according to the convention(pep-8),the maximum number of characters is 79 characters but we go
#upto 32 characters.
#RULE 5:Keywords can't be used as an identifier name.

#KEYWORDS:
#Keywords are pre-defined words which are having some specific meaning or specific task.
#In python,we have 35 keywords.
#But it will varies from 32-36 keywords based on version.

#We can use the keyword in 2 ways.
#1.By taking the help(). eg.help('keywords')
#  list of keywords are:False,True,None,and,if,else,elif etc. 
#2.Importing the keywords.
#  1.import keyword
#    keyword.kwlist

#  2.From keyword import kwlist
#   kwlist
#ex:False.True,None etc.

#VARIABLE:
#Variable is a named memory location which is used to store the data, and it can be changed during execution.
#ex: a=10

#Variables always declare with LOWERCASE LETTERS.
# If we declare variable with UPPERCASE CHARACTERS,it will become CONSTANT VARIABLE.


#GARBAGE COLLECTION:
# Whenever the reference count of an object become 0, garbage collector will remove the dereferenced variable from the memory.

#id()
# It is an in-built function which returns object address.
#SYNTAX:
#    id('variable_name')

#DATA TYPES:
#Data types are used to specify what type of data are storing inside a variable.
#Data types are 2 types,
#           1.Individual / single value data type.
#           2.Collection / container data type.

#1.Individual data type:
#      All the datas are store in a single memory block is called individual data type.

#2.Collection data type:
#      All  datas are stored in a sequence of memory is called collection data type.

# 1.Individual data type:
#      All the datas are store in a single memory block is called individual data type.
#     
#There are 4 types of individual data type:
#       1.Integer
#       2.Float
#       3.Boolean 
#       4.Complex
#
#All idividual data types are immutable.
#We can't use length function for the individual data type.
 
#1.INTEGER:
#If we store the number,without having decimal values or floating values we call it as an integer.
#Default value of integer is 0.
#ex:a=2
#type(a)
#op=<class 'int'>

#SOME BASIC OPERATORS IN INTEGER ARE:
#+,-,*,/,**,//

#2.FLOAT:
#Any number which is declared by using floating values or decimal values,we need to use float data type.
#The dafault value of float is 0.0
#ex:b=1.2
#type(b)
#o/p=<class 'float'>

#3.BOOLEAN:
#It is used to store either TRUE or FALSE.
#Default value of boolean is FALSE.
#Internal value of TRUE is 1.
#Internal value of FALSE is 0.

#ex:c=True
#type(c)
#o/p=<class 'Bool'>

#4.COMPLEX:
#It is a combination of real and imaginary number.
#The dafault value of j is root(-1).
#The dafault value of complex is oj.

#ex:c=2+3j
#type(c)
#o/p=<class 'complex'>

#2.COLLECTION DATAT TYPE:
#In collection data types,we store the data in the 'Sequence of memeory'.
#For the collection data type, we can use len() function.

#There are 5 types of collection data type:
#1.String
#2.List
#3.Tuple
#4.Set
#5.Dictionary

#1.STRING:
#String is a "collection of elements or Characters".
# Anything which is enclosed in single quote(' '),double quotes(" "),triple quotes("' "') and triple double quotes("""""") abd also these are boundaries of string.
#String is an immutable data type.
#Default value of string is empty single quotes(' ').
#ex:c='jesus'
#type(c)
#o/p=<class 'str'>

#INDEXING:
# It is the process of 'extracting individual character' from a collection.
# SYNTAX:
# collection_name[index]
# ex:'PROGRAMMING'  
# S[0]='P'
# S[1]='R'
# S[2]='O'

#SLICING:
#It is the process of extracting 'multiple characters at a time or simultaneously is known as slicing.

#syntax:
# COLLECTION_NAME(START INDEX:END INDEX:STEP VALUE)

#Here,start index is optional,if we are start from 0.
# End index is optional,if we ends at length.
# Step value is optional,if we want to extract characters after every step.
# 
# NOTE: IN SLICING, END INDEX IS EXCLUSIVE,WON'T BE CONSIDER.
# 
# ex:  a='morning'
# print([0:2:1])
# o/p= 


#STRING METHODS:
#1.  UPPER()
#2.  LOWER()
#3.  SWAPCASE()
#4.  CAPITALIZE()
#5.  TITLE()
#6.  INDEX()
#7.  rINDEX()
#8.  FIND()
#9.  rFIND()
#10. COUNT()
#11. REPLACE()
#12. SPLIT()
#13. rSPLIT()
#14. JOIN()
#15. STRIP()
#16. rSTRIP()
#17. lSTRIP()
#18. STARTSWITH()
#19. ENDSWITH()
#20. ISUPPER()
#21. ISLOWER()
#22. ISALPHA()
#23. ISDIGIT()
#24. ISALNUM()
#25. ISSPACE()
#26. ISIDENTIFIER()

#1.UPPER():
#It is a string method ,which accepts string as an input and convert that string into uppercase characters.
#Return type of upper is String.
#It won't accept any arguments.

#SYNTAX:
# string.upper()

#ex:  a='hello'
#s.upper()
#o/p='HELLO'

#2.LOWER():
#It is a string method, which accept string as an input and convert the string into lowercase characters.
#It returns string.
#It won't accept any arguments.

#SYNTAX:
#string.lower()

#ex: a='JESUS'
#a.lower()
#o/p= 'jesus'

#3.SWAPCASE():
#It is a string method ,which accept string as an input and convert all the uppercase character into lowercase and lowercase character into uppercase.
#It returns string.
#It won't accept any arguments.

#SYNTAX:
#string.swapcase()

#ex: c='JesUS'
#c.swapcase()
#o/p='jESus'

#4.CAPITALIZE():
#It is a string method, which converts first letter of a string into uppercase and remaining letters into lowercase.
#It returns string.
#It won't accepts any arguments.

#SYNTAX:
#string.capitalize()

#ex: a='love is blind'
#a.capitalize()
#o/p:'Love is blind'

#5.TITLE():
#It is a string method ,which accepts string and return the string by converting first letter of every word into uppercase and remaining lwtter into lowercase.
# It returns string.
#It won't accept any arguments.

# SYNTAX:
#  string.title()
# 
# ex: a='hello everyone here'
# a.title()
#o/p='Hello Everyone Here'
#  

#6.INDEX():
#It is a string method, is used to find first occured specified element from the left side.
# The return type of index is 'INTEGER'.
# It accepts 3 arguments.
# 1.element or substring.
# 2.start index
# 3.end index
# 
# By default start index is 0 and end index is length of the collection.
# It  rises VALUE ERROR,if the specified element is not present in the collection.

# SYNTAX:
# string.index(substring,[SI,EI]).........[] indicates the optional.
 
# ex:
# a='jenifer'
# a.index('e',0,5)
#o/p=1
 
 
#7.rINDEX():
# It is a string method,which is used to find the position of a first occured specified element from the right side.
# It returns 'INTEGER'.

# It accepts 3 arguments.
# 1.element or substring.
# 2.start index
# 3.end index  

#SYNTAX:
#string.Rindex(substring,[SI,EI]).........[] indicates the optional.

#EX: a='jenifer'
#a.rindex('e')
#o/p=2


#8.FIND()

# It is a string method,which is used to find the position of a first occured specified element from the LEFT side.
#  It returns 'INTEGER'.
# It accepts 3 arguments.
# 1.element or substring.
# 2.start index
# 3.end index  

#SYNTAX:
#string.FIND(substring,[SI,EI]).........[] indicates the optional.


#ex: a='jenifer'
#a.find('n')
#o/p=2


#9.rFIND():

#It is a string method,which is used to find the position of a first occured specified element from the RIGHT side.
#  It returns 'INTEGER'.
# It accepts 3 arguments.
# 1.element or substring.
# 2.start index
# 3.end index  

##SYNTAX:
#string.rFIND(substring,[SI,EI]).........[] indicates the optional.

#ex: a='APPLE'
#a.rfind('P')
#o/p=2

#10.COUNT():
#It is used to find how many times the specified substring is repeated.

#  It returns 'INTEGER'.
# It accepts 3 arguments.
# 1.element or substring.
# 2.start index
# 3.end index  

#Substring is mandatory but start index and end index are optional.
#If the specified element is not present it returns 0.

#SYNTAX:
#string.count(substring,[SI,EI])........[] indicates the optional.
#ex:
#a='jennifer'
#a.count('n')
#o/p=2

#11.REPLACE():

#It is used to replace the old string with new string.
#it accepts 3 arguments.
#'old_string'
#new_string'
#count

#SYNTAX:
#string.replace('old_string,new_string,[count])

#ex: a='hello'
#a.replace('l','a')
#o/p='heaao'

#12.SPLIT():

#It is used to seperate the given string based on the separator.
#Default separator is '_' (space).
#If the specified separator is not prsent it returns the string as it is.
#The return type of split is [list].
 
# SYNTAX:
# string.split('separator',[max_split])
 
# ex: a='hello world'
# a.split()
# o/p=['hello,'world'] 

#13.rSPLIT:
#It is used to seperate the given string based on the separator.
#if we mention maximum split,it will split from right side.
#Default separator is '_' (space).
#If the specified separator is not prsent it returns the string as it is.
#The return type of split is [list].

# SYNTAX:
# string.rsplit('separator',[max_split])

#ex:
#a='hello every one'
#a.rsplit()
#o/p=['hello','every','one']
#s.rsplit(' ',1)=>['hello every','one']


#14.JOIN():
#Join is used to join a string,for each and every element present in a iterable(through which we can traverse).
#Join always accepts 'string' as an input.
#Return type of join is STRING.

#SYNTAX:
# string.join(iterable)

#ex:
#@.join('12345')
#o/p='1@2@3@4'

#STRIP:
#It is used to remove the specified element from leading and tailing.
#Default character is space('_').

#WORKING:
#it starts removing the given character from the leading part until the unmatched character is found.
#Once the unmatch is found ,it will jump into the tailing part and removes the specified character until unmatch is found.
 
#SYNTAX:
# string.strip([character])

#ex:
#s='@@@@hello@@@@'
#s.strip('@')
#o/p=> 'hello'

#lSTRIP:
#It is used to remove the specified element from leading part.
#Default character is space '_'
#
#SYNTAX:
#string.lstrip(['character'])

#ex:
#a='      hello         '
#a.lstrip()
#o/p=>'hello      '


#rSTRIP:
#It is used to remove the specified element from tailing part.
#Default character is space '_'
#
#SYNTAX:
#string.rstrip(['character'])

#ex:
#s='       hello        '
#s.rstrip()
#o/p=> '     hello'
# 
# 
# STARTSWITH:

#It is used to check whether the given string is starting with specified substring.
#It returns BOOLEAN VALUE.
#If the given string starts with specified character,it returns 'TRUE' else it returns 'FALSE'.
#
#SYNTAX:
# string.startswith(sub_string,[SI,EI])

#ex:
#s='hello pyhton'
#s.startswith('h')
#o/p=>TRUE

#ENDSWITH:
#It is used to check whether the given string is ending with specified substring.
#It returns BOOLEAN VALUE.
#If the given string ends with specified character,it returns 'TRUE' else it returns 'FALSE'.
#
#SYNTAX:
# string.endswith(sub_string,[SI,EI])
#
#ex:
#s='hello'
#s.endswith('o')
#o/p=>TRUE

#IS UPPER():
#
#It is used to check whether the given string is containing only UPPER CASE characters.
#It returns BOOLEAN VALUE.
# It returns 'TRUE' ,if the given string is having only uppercase characters.
#It won't accept any arguments.

#SYNTAX:
#string.isupper()

#ex:
#s='HELLO'
#s.upper()
#o/p=> TRUE

#ISLOWER():

#It is used to check whether the given string is containing only LOWER CASE characters.
#It returns BOOLEAN VALUE.
# It returns 'TRUE' ,if the given string is having only lowercase characters.
#It won't accept any arguments.

#SYNTAX:
#string.islower()

#ex:
#s='hello'
#s.islower()
#TRUE

#IS ALPHA():
#It is used to check whether the given string having only alphabets or not.
#It returns BOOLEAN VALUE.
# It returns 'TRUE' ,if the given string is having completely alphabets.
#It won't accept any arguments.

#SYNTAX:
# string.isalpha()

#ex:
#s='jeni'
#s.isalpha()
#o/p=> TRUE


#IS DIGIT():
#It is used to check whether the given string having completely numbers.
#It returns BOOLEAN VALUE.
# It returns 'TRUE' ,if the given string is having completely digits.
#It won't accept any arguments.

#SYNTAX:
#string.isdigit()

#ex:
#a='1234556'
#a.isdigit()
#o/p=> TRUE


#IS ALNUM():

#It is used to check whether the given string having only alphabets,only digits ,combination of alphabets and numbers.
#It returns BOOLEAN VALUE.
# It returns 'TRUE' ,if the given string is having completely digits.
#It won't accept any arguments.

#SYNTAX:
#string.isalnum()

#ex:
#s='hello'
#s.isalnum()
#o/p=> TRUE

#ex:
#s='123232'
#s.isalnum()
#o/p=> TRUE

#EX:
#s='123jeni'
#s.isalnum()
#o/p=> TRUE

#IS SPACE():
#It returns TRUE, if the given string contains only SPACE.

#SYNTAX:
#'_' . isspace()

#ex:
#a=' '
#a.isspace()
#o/p=> TRUE





















