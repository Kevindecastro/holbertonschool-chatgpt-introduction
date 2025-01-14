#!/usr/bin/python3
class TicTacToe:
	"""
	A simple implementation of the Tic-Tac-Toe game.
	"""

	def __init__(self):
		"""
		Initialize the Tic-Tac-Toe board and game state.
		"""
		self.board = [[' ' for _ in range(3)] for _ in range(3)]
		self.current_player = 'X'

	def print_board(self):
		"""
		Display the current state of the board.
		"""
		for row in self.board:
			print("|".join(row))
			print("-" * 5)

	def make_move(self, row, col):
		"""
		Make a move on the board.

		Parameters:
			row (int): Row index (0-2).
			col (int): Column index (0-2).

		Returns:
			bool: True if the move is valid, False otherwise.
		"""
		if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' ':
			self.board[row][col] = self.current_player
			return True
		return False

	def check_winner(self):
		"""
		Check if there's a winner.

		Returns:
			str: The winning player ('X' or 'O') or None if no winner yet.
		"""
		for row in self.board:
			if row[0] == row[1] == row[2] != ' ':
				return row[0]
		for col in range(3):
			if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
				return self.board[0][col]
		if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
			return self.board[0][0]
		if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
			return self.board[0][2]
		return None

	def switch_player(self):
		"""
		Switch to the other player.
		"""
		self.current_player = 'O' if self.current_player == 'X' else 'X'

	def is_full(self):
		"""
		Check if the board is full.

		Returns:
			bool: True if the board is full, False otherwise.
		"""
		return all(cell != ' ' for row in self.board for cell in row)

	def play(self):
		"""
		Start the game loop.
		"""
		while True:
			self.print_board()
			print(f"Player {self.current_player}'s turn.")
			try:
				row = int(input("Enter row (0-2): "))
				col = int(input("Enter column (0-2): "))
				if not self.make_move(row, col):
					print("Invalid move. Try again.")
					continue
				winner = self.check_winner()
				if winner:
					self.print_board()
					print(f"Player {winner} wins!")
					break
				if self.is_full():
					self.print_board()
					print("It's a draw!")
					break
				self.switch_player()
			except ValueError:
				print("Invalid input. Please enter numbers between 0 and 2.")


if __name__ == "__main__":
	game = TicTacToe()
	game.play()
