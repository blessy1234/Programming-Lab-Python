Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> dict={}
>>> dict['one']="Hello All"
>>> dict['two']="Stay Safe"
>>> dict['three']="Stay Healthy"
>>> print
<built-in function print>
>>> print(dict)
{'one': 'Hello All', 'two': 'Stay Safe', 'three': 'Stay Healthy'}
>>> dict2={'name=':'Prajitha','age'=20,'programme'=:'MCA'}
KeyboardInterrupt
>>>  dict2={'name=':'Prajitha','age'=20,'programme'=:'MCA'}
 
SyntaxError: unexpected indent
>>>  dict2={'name=':'Prajitha','age':20,'programme':'MCA'}
 
SyntaxError: unexpected indent
>>> dict2={'name=':'Prajitha','age':20,'programme':'MCA'}
>>> print(dict2)
{'name=': 'Prajitha', 'age': 20, 'programme': 'MCA'}
>>> print(dict['one'])
Hello All
>>> print(dict.keys())
dict_keys(['one', 'two', 'three'])
>>> print(dict.values())
dict_values(['Hello All', 'Stay Safe', 'Stay Healthy'])
>>> print(dict.items())
dict_items([('one', 'Hello All'), ('two', 'Stay Safe'), ('three', 'Stay Healthy')])
>>> dict.update(dict2)
>>> print(dict)
{'one': 'Hello All', 'two': 'Stay Safe', 'three': 'Stay Healthy', 'name=': 'Prajitha', 'age': 20, 'programme': 'MCA'}
>>> 