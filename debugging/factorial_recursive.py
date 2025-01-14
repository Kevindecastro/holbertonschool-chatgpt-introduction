#!/usr/bin/python3
def factorial_recursive(n):
	"""
	Calculate the factorial of a number recursively.

	Parameters:
		n (int): The number to calculate the factorial of.

	Returns:
		int: The factorial of the number.
	"""
	if n < 0:
		raise ValueError("Factorial is not defined for negative numbers.")
	if n == 0 or n == 1:
		return 1
	return n * factorial_recursive(n - 1)


if __name__ == "__main__":
	try:
		num = int(input("Enter a number to calculate its factorial: "))
		print(f"The factorial of {num} is {factorial_recursive(num)}")
	except ValueError as e:
		print(f"Error: {e}")
