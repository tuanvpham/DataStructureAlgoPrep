# Some notes for Python

- Variables, Names, and Objects
	- everything is booleans, integers, floats, strings
	- an object: clear plastic box that contains a piece of data
	- immutable object: a closed box with a clear window (can see value, but can't change it)
	- mutable object: an open box, but can't change its type
	- variables: names (a reference to a thing rather than the thing itself - sticky note)
	- assingment does not copy a value; it just attaches a name to the object that contains data

- Slice
	- [:] extracts entire sequence from start to end
	- [start:] from start offset to the end
	- [:end] from beginning to the end offset minus 1
	- [start:end] from start offset to the end offset minus 1
	- [start:end:step] from start offset to the end minus 1, skipping by step

- Lists and Tuples
	- elements can be of different types - any Python object
	- Tuples: immutable
	- List: mutable
		- add item to the end: append()
		- combine lists: extend() or +=
		- add item by offset: insert(index, new_item)
		- delete item
			- by offset: del list[index] (del string[1])
			- by value: list.remove(value)
		- get item and delete: pop(), pop(index)
		- test for a value with in: 'test' in list

- = versus copy()
	- assign a list to more than one variable, changing in one place also changes it in others (sticky note)
	``` 
		a = [1,2,3]
		b = a
	```
	- copy(), list(), slice: copy values of a list to an independent, fresh list
	``` 
		b = a.copy()
		c = list(a)
		d = a[:]
	```
	- b, c, d are copies of: they are new objects with their own values, no connection to original list a. Changing a does not affect b, c, and d

- Useful functions
	- dir(object): list of attributes of methods of any object
	- help(ClassName): list of all information about class (inheritance, attributes, methods)
	- isinstance(instance_name, ClassName): check if an instance is from a class
	- issubclasS(SubclassName, ClassName): check if a class is subclass of another class