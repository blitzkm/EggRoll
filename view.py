class EggRollView:
	def show_invalid_move(self, move:str) -> None:
		print("Oh no! You'll hit a wall, invalid move!")

	def show_win(self) -> None:
		print("You win! All egg are safe in the nests.")

	def show_lose(self) -> None:
		print("You're Cooked! Your egg hit a frying pan, you lose.")

	def show_save_game(self, player_name: str) -> None:
		print(f'Hello {player_name}! Would you like to save your game? (y/n)')

	def show_restart_level(self, player_name: str, current_level: int) -> None:
		print(f'Hello {player_name}! Would you like to restart level {current_level}? (y/n)')

	def show_attempts_left(self, attempts_left: int) -> None:
		print(f'{attempts_left} attempts left')

	def show_title(self) -> None:
		print("\033[95m" + "=" * 30)
		print("      🎯 E G G R O L L 🎯")
		print("=" * 30 + "\033[0m\n")

	def clear_screen(self) -> None:
		print("\n" * 100)

	def get_player_input(self) -> str:
		return input()


view = EggRollView()  # Create an instance
view.show_title()