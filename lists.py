Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> garage = ['toyota', 'honda', 'izuzu']
>>> garage.append('suzuki')
>>> print (garage)
['toyota', 'honda', 'izuzu', 'suzuki']
>>> print(garage[2])
izuzu
>>> garage.remove('honda')
>>> print (garage)
['toyota', 'izuzu', 'suzuki']
>>> garage.insert(1,'benz')
>>> print (garage)
['toyota', 'benz', 'izuzu', 'suzuki']
>>> del garage[2]
>>> print (garage)
['toyota', 'benz', 'suzuki']
>>> print (garage[-1])
suzuki
>>> print (garage[-2])
benz
>>> print (mycar)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print (mycar)
NameError: name 'mycar' is not defined
>>> mycar = garage.pop(-1)
>>> print (mycar)
suzuki
>>> garage.append('suzuki')
>>> print garage
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(garage)?
>>> print (garage)
['toyota', 'benz', 'suzuki']
>>> garage[1] = 'tesla'
>>> print (garage)
['toyota', 'tesla', 'suzuki']
>>> print (len(garage))
3
>>> users = ['z','r','t','b','n','p']
>>> users.sort()
>>> print (users)
['b', 'n', 'p', 'r', 't', 'z']
>>> users.sort(reverse=Tr)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    users.sort(reverse=Tr)
NameError: name 'Tr' is not defined
>>> users.sort(reverse=True)
>>> users
['z', 't', 'r', 'p', 'n', 'b']
>>> print(sorted(users))
['b', 'n', 'p', 'r', 't', 'z']
>>> print (users)
['z', 't', 'r', 'p', 'n', 'b']
>>> users = ['z','r','t','b','n','p']
>>> users.reverse()
>>> print (users)
['p', 'n', 'b', 't', 'r', 'z']
>>> for u in users:
	print (u)

	
p
n
b
t
r
z
>>> for u in users:
	users.sorted(reverse=True)
	print (u)

	
Traceback (most recent call last):
  File "<pyshell#36>", line 2, in <module>
    users.sorted(reverse=True)
AttributeError: 'list' object has no attribute 'sorted'
>>> for u in users:
	users.(sorted(users))
	print (u)
	
SyntaxError: invalid syntax
>>> for u in users:
	print (sorted(users))

	
['b', 'n', 'p', 'r', 't', 'z']
['b', 'n', 'p', 'r', 't', 'z']
['b', 'n', 'p', 'r', 't', 'z']
['b', 'n', 'p', 'r', 't', 'z']
['b', 'n', 'p', 'r', 't', 'z']
['b', 'n', 'p', 'r', 't', 'z']
>>> for u in users:
	print ('hello',u)
	print ('hello'+u)

	
hello p
hellop
hello n
hellon
hello b
hellob
hello t
hellot
hello r
hellor
hello z
helloz
>>> 
============================= RESTART: D:\UncleEngineerPython\EP.1\Test1.py ============================
