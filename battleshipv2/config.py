
class Config:

	def __init__(self):

		#GAME CONFIG
		self.title = "Battleship"
		self.row = 5
		self.column = 5


		#WINDOW CONFIG
		base = 100
		ratio = 5
		self.side = base * ratio
		self.screen = f"{self.side}x{self.side}+500+500"

		#IMG PATH
		self.init_img = "img/click_here.jpg"
		self.final_img = "img/try_again.jpg"
		self.win_img = "img/good_job.jpg"