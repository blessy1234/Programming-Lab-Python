Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> d={'m1':20,'m2':30}
>>> d1={'name':'Rasika'}
>>> s=d.copy()
>>> print(s)
{'m1': 20, 'm2': 30}
>>> d.update(d1)
>>> print(d)
{'m1': 20, 'm2': 30, 'name': 'Rasika'}
>>> d1['age']=20
>>> print(d1)
{'name': 'Rasika', 'age': 20}
>>> print(sorted(d1.items())
print(sorted(d1.items()))
      
SyntaxError: invalid syntax
>>> print(sorted(d1.items()))
[('age', 20), ('name', 'Rasika')]
>>> print(sorted(d1.keys()))
['age', 'name']
>>> 