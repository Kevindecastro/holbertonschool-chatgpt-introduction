#!/usr/bin/python3
class Checkbook:
	"""
	A simple checkbook implementation to track balances and transactions.
	"""

	def __init__(self, initial_balance=0.0):
		"""
		Initialize the checkbook with an initial balance.

		Parameters:
			initial_balance (float): The starting balance of the checkbook.
		"""
		if initial_balance < 0:
			raise ValueError("Initial balance cannot be negative.")
		self.balance = initial_balance
		self.transactions = []

	def deposit(self, amount):
		"""
		Add money to the balance.

		Parameters:
			amount (float): The amount to deposit.
		"""
		if amount <= 0:
			raise ValueError("Deposit amount must be positive.")
		self.balance += amount
		self.transactions.append(f"Deposit: +${amount:.2f}")

	def withdraw(self, amount):
		"""
		Subtract money from the balance.

		Parameters:
			amount (float): The amount to withdraw.
		"""
		if amount <= 0:
			raise ValueError("Withdrawal amount must be positive.")
		if amount > self.balance:
			raise ValueError("Insufficient funds.")
		self.balance -= amount
		self.transactions.append(f"Withdrawal: -${amount:.2f}")

	def show_balance(self):
		"""
		Display the current balance.
		"""
		print(f"Current Balance: ${self.balance:.2f}")

	def show_transactions(self):
		"""
		Display all transactions.
		"""
		print("Transactions:")
		for transaction in self.transactions:
			print(transaction)


if __name__ == "__main__":
	checkbook = Checkbook(100.0)  # Starting with an initial balance of $100
	while True:
		print("\nCheckbook Menu")
		print("1. Show Balance")
		print("2. Deposit")
		print("3. Withdraw")
		print("4. Show Transactions")
		print("5. Exit")
		try:
			choice = int(input("Enter your choice: "))
			if choice == 1:
				checkbook.show_balance()
			elif choice == 2:
				amount = float(input("Enter deposit amount: "))
				checkbook.deposit(amount)
			elif choice == 3:
				amount = float(input("Enter withdrawal amount: "))
				checkbook.withdraw(amount)
			elif choice == 4:
				checkbook.show_transactions()
			elif choice == 5:
				print("Goodbye!")
				break
			else:
				print("Invalid choice. Please select a valid option.")
		except ValueError as e:
			print(f"Error: {e}")
