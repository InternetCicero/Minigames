from random import *

D = ["Rock","Paper","Scissors"]
Score = 0

def func():

	W_P = input("Type in your move: ")

	if W_P in D:
		rand(W_P)
		print(Score)
	else:
		print("NotValid!")
		func()

	
	#print(Score)
	playAgain = input("Do you want to play again? Y/N ")

	if playAgain == "Y":
		func()
	else: quit()


def rand(W_P):

	global Score
	z = randint(0, 2)

	W_PC = D[z]


	if W_PC == W_P:
		print(f"Its a Tie! The computer chose {W_PC} ")
	elif W_PC == "Rock" and W_P == "Paper" or W_PC == "Paper" and W_P == "Scissors" or W_PC == "Scissors" and W_P == "Rock":
		print(f"You Win! The computer chose {W_PC}")
		Score = Score + 1
	else:
		print(f"You Lost! The computer chose {W_PC}")


def main():
	func()


if __name__ == "__main__":

	main()





