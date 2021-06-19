import tkinter as tk
import sys
import time

from tkinter import messagebox as msg
from config import Config
from game_stat import Statistic
from ship import Ship
from player import Player
from board import Board

class Window(tk.Tk):

	def __init__(self, Game):
		self.game = Game
		self.config = Game.config

		super().__init__()
		self.title(self.config.title)
		self.geometry(self.config.screen)

		self.create_container()

		self.pages = {}
		self.create_board()
		self.create_login_page()

	def create_container(self):
		self.container = tk.Frame(self, bg="red")
		self.container.pack(fill="both", expand=True)

	def create_board(self):
		self.pages["board"] = Board(self.container, self.game)

	def create_login_page(self):
		self.pages["Play"] = Play(self.container, self)

	def change_page(self):
		self.pages["board"].tkraise()




class Battleship:

	def __init__(self):
		self.config = Config()
		self.ship = Ship(self)
		self.player = Player()
		self.window = Window(self)
		self.stats = Statistic()
		self.play = self.window.pages["Play"]

	def check_location(self):
		if self.ship.location == self.player.location:
			return True
		return False

	def is_button_clicked(self, pos_x, pos_y):
		self.stats.steps+=1
		print(pos_x, pos_y)
		self.window.pages["board"].buttons_board[pos_x][pos_y]["state"] = "disabled"
		self.player.current_location(pos_x, pos_y)
		win = self.check_location()
		self.window.pages["board"].change_photo_button(pos_x, pos_y, win)
		if self.ship.location!= self.player.location:
			self.stats.score-=10
		print(self.stats.score)
		if win:
			print("WIN!")
			confirm = msg.showinfo(f"Congrats {self.play.nameVar.get()}",f"Score : {self.stats.score}\nAttempts : {self.stats.steps}                                ")
			if confirm:
				sys.exit()
		if self.stats.score == 0:
			print("Game Over")
			confirm = msg.showinfo(f"Nice Try {self.play.nameVar.get()}",f"Score : {self.stats.score}\nAttempts : {self.stats.steps}                                ")
			if confirm:
				sys.exit()

	def run(self):
		self.window.mainloop()

class Play(tk.Frame):

	def __init__(self, parent,App):
		self.application = App
		self.settings    = App.config
		self.stats       = Statistic()

		super().__init__(parent)

		self.configure(bg = "red")
		self.grid(row = 0, column= 0, sticky = 'nswe')

		parent.grid_columnconfigure(0, weight = 1)
		parent.grid_rowconfigure(0, weight = 1)

		self.main_frame = tk.Frame(self, height = self.settings.side, width = self.settings.side, bg = 'red')
		self.main_frame.pack(expand = True) 

		self.label_username = tk.Label(self.main_frame, text = "Selamat datang di Game Battleship\nSilahkan isi nickname", bg = 'red', fg = "white", font = ("Arial", 18, "bold"))
		self.label_username.pack(pady = 5)

		self.nameVar = tk.StringVar()
		self.entry_username = tk.Entry(self.main_frame, font = ("Arial", 16, "bold"), textvariable = self.nameVar, justify = 'center')
		self.entry_username.pack(pady = 15)

		self.btn_login = tk.Button(self.main_frame, text='Enter', command=lambda:self.greeting())
		self.btn_login.pack(pady=5)

	def greeting(self):
		self.label_username.config(text="Halo" + " " + self.nameVar.get(), font = ("Arial", 15, "bold"))
		self.peraturan = tk.Label(self.main_frame, text = "Peraturan :\n1. Di game ini terdapat 25 box yang diantaranya terdapat 1 box yang benar\n2. Jika anda menebak pada box yang salah poin anda akan berkurang 10 poin\n3.Kesempatan menebak hanya 10 kali\n4. Klik Play now untuk bermain", bg = 'red', fg = "white", font = ("Arial", 9, "bold"))
		self.peraturan.pack(pady = 5) 
		self.entry_username.destroy()
		self.btn_login.config(text="Play Now", command=lambda:[self.application.change_page()])
		
def main():
	my_battleship = Battleship()
	my_battleship.run()


if __name__ == '__main__':
	main()