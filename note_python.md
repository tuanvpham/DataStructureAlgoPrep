# Some notes for Python

## Useful Resources
https://www.pythoncentral.io/category/python-tips-tricks-hacks-idioms/

## Data Structure
### Stacks and Queues
- Stack
 - Last In First Out (LIFO)
 - Use [] (List)
 - Add item to the top (end) of the list: append(item)
 - Pop out item at the end: pop()
- Queue
 - First In First Out (FIFO)
 - Use *collections.deque*
 - Add item at the top (end): append(item)
 - Pop out item at the beginning: popleft()
```python
    stack = ['Tuan', 'Viet']
    stack.append('Pham')
    stack.pop()

    from collections import deque
    queue = deque(['Tuan', 'Viet'])
    queue.append('Pham')
    queue.popleft()
 ```



### Variables, Names, and Objects
- everything is booleans, integers, floats, strings
- an object: clear plastic box that contains a piece of data
- immutable object: a closed box with a clear window (can see value, but can't change it)
- mutable object: an open box, but can't change its type
- variables: names (a reference to a thing rather than the thing itself - sticky note)
- assingment does not copy a value; it just attaches a name to the object that contains data
- False: False (boolean), None (null), 0, 0.0, '', [], (), {}, set()

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

### Comprehension
- List Comprehension
    - [ expression for item in iterable ]
    - [ expression for item in iterable if condition ]
- Dict Comprehenstion
    - { key_expression:value_expression for expression in iterable }
- Set Comprehension
    - { expression for expression in iterable }
```python
    # List Comprehension
    number_list = [number for number in range(1,6)]
    number_list_expression = [number-1 for number in range(1,6)]
    a_list = [number for number in range(1,6) if number % 2 ==0]
    rows = range(1,4)
    cols = range(1,3)
    cells = [(row, col) for row in rows for col in cols]

    # Dict Comprehention: create a dict of frequences of each letter in a word
    word = 'letters'
    letter_counts = { letter: word.count(letter) for letter in word}

    # Set Comprehension
    a_set = { number for number in range(1,6) if number % 3 == 1}
```

### Function
- postional arguments
- keyword arguments

---
## Effective Python

### Assignment = versus copy()
- assign a list to more than one variable, changing in one place also changes it in others (sticky note)
```python
    a = [1,2,3]
    b = a
```
- copy(), list(), slice: copy values of a list to an independent, fresh list
```python 
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

### How to slice sequences
- simplest uses: list, str, and bytes and any Python class has `__getitem__` and `__setitem__`
- `somelist[start:end]`, start is inclusive and end is exclusive
- slicing from the start: leave out zero index `a[:5]`
- slicing to the end: `a[5:]`
- negative numbers for doing offset relative to the end of list `a[-3:-1]`
- sliced list won't affect original list
- assignment:
```python
    print('Before ', a)
    a[2:7] = [99, 22, 14]
    print('After ', a)
    >>>
    Before ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    After ['a', 'b', 99, 22, 14, 'h']
```
- assign a slice with no start or end indexes: replace its entire contents with a copy of what's referenced (instead of allocating a new list)
- assigning to a list slice will replace that range in the original sequence with what's referenced even if their lenghts are different
```python
    b = a
    print('Before ', a)
    a[:] = [101, 102, 103]
    print('After ', b)
    >>>
    Before ['a', 'b', 99, 22, 14, 'h']
    After [101, 102, 103]
```

### Shorthand for Swapping Two Variables
- use tuples
```python
    a = 7
    b = 10
    a, b =  b, a
```

### Special Notes
- Avoid using start, end, step in a single step
    - if using stride, making it a positive value and omit start and end indexes
    - consider do 2 assignments: one to slice, another to stride (make steps)
- Use List Comprehenstions instead of map, filter, and lambda
- List Comprehension with more than 2 expressions are difficult to read (should be avoided)


### Useful Things
- dir(object): list of attributes of methods of any object
- help(ClassName): list of all information about class (inheritance, attributes, methods)
- isinstance(instance_name, ClassName): check if an instance is from a class
- issubclass(SubclassName, ClassName): check if a class is subclass of another class
- Dictionary:
    - dict['key']: this returns an error if value cannot be found
    - use dict.get(key, 'default'): returns 'default' if value cannot be found
- Continue lines with \
- Ierating over multiple sequences in parallel: zip()
```python
    for day, fruit in zip(days, fruits):
        print(day, fruit)
```