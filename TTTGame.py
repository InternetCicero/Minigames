#Libaries
from tkinter import ttk
import tkinter

'''


ttk.Style().configure("TButton", padding=6, relief="flat",
   background="#ccc")
   '''


class App(tkinter.Tk):
	def __init__(self):
		super().__init__()

		self.field = []
		self.fieldlist= []

		self.player = True

		self.title("Tic Tac Toe Game")
		self.geometry("500x300")
		self.maxsize(750, 550)
		self.resizable(True, True)

		self.style = ttk.Style()
		self.style.configure(
			"TButton",
			padding=10,
			font=('Helvetica', 12),
			background='#3498db',  
			foreground='#ffffff',  	
			borderwidth=2,
			focuscolor='#2980b9',  
			highlightthickness=2,
		)

	def CreateGame(self):
		titel = ttk.Label(text="Tic Tac Toe Game")
		titel.grid(row=0, column=3)

		#Create a 3x3 grid of buttons
		for r in range(3):
			for c in range(3):
				btn = ttk.Button(self, text="", style="TButton", command=lambda row=r, col=c: self.ChangeValue(row, col))
				btn.grid(row=r+2, column=c+2, padx=5, pady=5, columnspan=1)

				self.field.append(btn)
				self.fieldlist.append("")

		
	def ChangeValue(self, row, col):
		button_index = row * 3 + col
		button = self.field[button_index]

		self.symbol = "X" if self.player else "O"
		self.player = not self.player

		if button.cget('text') == "":
			button.configure(text=self.symbol)
			self.fieldlist[button_index] = self.symbol


		if self.CheckWinner() == "w":
			mes = ttk.Label(text=f"{self.symbol} has won the game")
			mes.grid(row=10, column=3)
			for i in self.field:
				i.state(["disabled"])
		elif self.CheckWinner() == "d":
			print("draw")
			mes = ttk.Label(text=f"Its a draw!")
			mes.grid(row=10, column=3)
			for i in self.field:
				i.state(["disabled"])

		
		

			


	def CheckWinner(self):
		draw = 0
		winlines = [[0, 1, 2],[3, 4, 5],[6, 7 ,8],[0, 3, 6],[1, 4, 7],[2, 5, 8], [0, 4, 8], [2, 4, 6]]

		for line in winlines:
			if self.fieldlist[line[0]] == self.symbol and self.fieldlist[line[1]] == self.symbol and self.fieldlist[line[2]] == self.symbol:
				return "w"

			elif "" not in self.fieldlist:
				draw += 1

		if draw == 8:
			return "d"








if __name__ == "__main__":
	app = App()
	app.CreateGame()
	app.mainloop()
