# Dynamic Programming 
- taking a recursive algorithm and finding the overlapping subproblems. Then we can cache those results for future recursive callls
- avoid making redundant method calls
- store the answers to all mecessary method calls in memory and simply look these up as necessary

## Fibonacci 
```python
def fib(n):
	if n < 2: return n
	else: return fib(n-1) + fib(n-2)

def fib_dynamic(n):
	fib_array = [0,1]
	while len(fib_array) < n+1: fib_array.append(0)

	if n <= 1: return n
	else:
		if fib_array[n-1] == 0: fib_array[n-1] = fib_dynamic(n-1)
		if fib_array[n-2] == 0: fib_array[n-2] = fib_dynamic(n-2)
		fib_array[n] = fib_array[n-2] + fib_array[n-1]

	return fib_array[n]

def fib_dynamic_fancy(n):
	fib_first = 0
	fib_second = 1
	i = 2

	while i < n+1:
		fib_second = fib_first + fib_second
		fib_first = fib_second - fib_first
		i+=1
	
	return fib_second
```