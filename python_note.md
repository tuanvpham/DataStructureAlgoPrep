# Some notes for Python

## Data Structure

### Variables, Names, and Objects
- everything is booleans, integers, floats, strings
- an object: clear plastic box that contains a piece of data
- immutable object: a closed box with a clear window (can see value, but can't change it)
- mutable object: an open box, but can't change its type
- variables: names (a reference to a thing rather than the thing itself - sticky note)
- assingment does not copy a value; it just attaches a name to the object that contains data

### Slice
- [:] extracts entire sequence from start to end
- [start:] from start offset to the end
- [:end] from beginning to the end offset minus 1
- [start:end] from start offset to the end offset minus 1
- [start: end: step] from start offset to the end minus 1, skipping by step

### Lists, Tuples, Dictionary, and Sets
- Lists and Tuples: elements can be of different types (any Python object)
- Sets: like a dict without values
- List: **[] or list()**
    - mutable
    - add item to the end: append()
    - combine lists: extend() or +=
    - add item by offset: insert(index, new_item)
    - delete item
        - by offset: del list[index] (del string[1])
        - by value: list.remove(value)
    - get item and delete: pop(), pop(index)
    - test for a value with in: 'test' in list
- Tuples: **()**
    - immutable
    - ```('a', 'b')``` = ```'a', 'b'``` (readable purpose)
    - assign multiple variables at once (tuple unpacking)
        - `unpacking_test_tuples = ('Dog', 'Cat', 'Bird')`
        - `d, c, b = unpacking_test_tuples`
        - exchange values without using temporary variable
    - use as dict keys, and function arguments
    - convert other things to tuples: tuple(other_things)
    - less space than lists
- Dictionary: **{key: value}**
    - key: immutable - unique (string or tuples only)
    - convert any sequence containing two-item sequences to dict: dict(other_things)
    - add or change an item: test['key_name']
    - combine dict: update()
    - delete an item by key: del test['key_name']
    - test where a key exits: key in test
    - get all keys, values: test.keys(), test.values()
    - get all key-value pairs: test.item()
    - copy: test.copy() (like lists, assignment will reflect all names that refer to dict)
- Sets: **{} or set()**
    - intersection: `&`
    - union: `|` or `union()`
    - difference: `-` or `difference()`

---
## Effective Python

### Assignment = versus copy()
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

### Differences between bytes, str, and unicode
- Python 3
    - bytes: raw 8-bit values
    - str: Unicode characters
    - can't be used together with operators
- Python 2
    - str: raw 8-bit values
    - unicode: Unicode characters
    - can be used together
- convert Unicode characters to binary data: encode
- convert binary data to Unicode: decode

### Useful functions
- dir(object): list of attributes of methods of any object
- help(ClassName): list of all information about class (inheritance, attributes, methods)
- isinstance(instance_name, ClassName): check if an instance is from a class
- issubclass(SubclassName, ClassName): check if a class is subclass of another class