#!/usr/bin/python3
import random
import os


def clear_screen():
	"""
	Clear the terminal screen.
	"""
	os.system('cls' if os.name == 'nt' else 'clear')


class Minesweeper:
	"""
	A Minesweeper game implementation.
	"""

	def __init__(self, width=10, height=10, mines=10):
		"""
		Initialize the Minesweeper board.

		Parameters:
			width (int): Width of the board.
			height (int): Height of the board.
			mines (int): Number of mines on the board.
		"""
		self.width = width
		self.height = height
		self.mines = set(random.sample(range(width * height), mines))
		self.field = [[' ' for _ in range(width)] for _ in range(height)]
		self.revealed = [[False for _ in range(width)] for _ in range(height)]

	def print_board(self, reveal=False):
		"""
		Print the current state of the board.

		Parameters:
			reveal (bool): If True, show all mines.
		"""
		clear_screen()
		print('  ' + ' '.join(str(i) for i in range(self.width)))
		for y in range(self.height):
				print(f"{y} ", end="")
				for x in range(self.width):
					if reveal or self.revealed[y][x]:
						if (y * self.width + x) in self.mines:
							print('*', end=' ')
						else:
							count = self.count_mines_nearby(x, y)
							print(count if count > 0 else ' ', end=' ')
					else:
						print('.', end=' ')
				print()

	def count_mines_nearby(self, x, y):
		"""
		Count mines around a given cell.

		Parameters:
			x (int): X-coordinate of the cell.
			y (int): Y-coordinate of the cell.

		Returns:
			int: Number of mines around the cell.
		"""
		count = 0
		for dx in [-1, 0, 1]:
			for dy in [-1, 0, 1]:
				nx, ny = x + dx, y + dy
				if 0 <= nx < self.width and 0 <= ny < self.height:
					if (ny * self.width + nx) in self.mines:
						count += 1
		return count

	def reveal(self, x, y):
		"""
		Reveal a cell. If the cell has no neighboring mines, reveal its neighbors.

		Parameters:
			x (int): X-coordinate of the cell.
			y (int): Y-coordinate of the cell.

		Returns:
			bool: False if the cell contains a mine, True otherwise.
		"""
		if (y * self.width + x) in self.mines:
			return False
		self.revealed[y][x] = True
		if self.count_mines_nearby(x, y) == 0:
			for dx in [-1, 0, 1]:
				for dy in [-1, 0, 1]:
					nx, ny = x + dx, y + dy
					if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
						self.reveal(nx, ny)
		return True

	def is_won(self):
		"""
		Check if the player has won the game.

		Returns:
			bool: True if all non-mine cells are revealed, False otherwise.
		"""
		for y in range(self.height):
			for x in range(self.width):
				if not self.revealed[y][x] and (y * self.width + x) not in self.mines:
					return False
		return True

	def play(self):
		"""
		Start the game loop.
		"""
		while True:
			self.print_board()
			if self.is_won():
				print("Congratulations! You've won the game.")
				break
			try:
				x = int(input("Enter x coordinate: "))
				y = int(input("Enter y coordinate: "))
				if not self.reveal(x, y):
					self.print_board(reveal=True)
					print("Game Over! You hit a mine.")
				break
			except ValueError:
				print("Invalid input. Please enter numbers only.")


if __name__ == "__main__":
	game = Minesweeper()
	game.play()
