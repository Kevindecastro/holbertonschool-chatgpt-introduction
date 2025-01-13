#!/usr/bin/python3
import sys

def factorial(n):
	"""Calculates the factorial of a given number."""
	result = 1
	while n > 1:
		result *= n
		n -= 1
	return result

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: ./factorial.py <number>")
		sys.exit(1)
	else:
		try:
			n = int(sys.argv[1])
			print(factorial(n))
		except ValueError:
			print("Please provide a valid integer.")
			sys.exit(1)
