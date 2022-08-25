def fib(n):
	""" Compute the nth Fibonacci number, for n >= 2."""
	pred, curr = 0, 1	# Fibonacci numbers 1st and 2nd term
	k = 2				# Which Fib number is curr?
	while k < n:
		pred, curr = curr, pred + curr
		k = k + 1
	return  curr

result = fib(8)