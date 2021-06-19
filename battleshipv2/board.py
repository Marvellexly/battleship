import tkinter as tk
from PIL import Image, ImageTk

class Board(tk.Frame):

	def __init__(self, parent, Game):
		self.game = Game # Battleship - my_battleship
		self.config = Game.config

		#CONFIG FRAME
		super().__init__(parent)
		self.configure(bg="black")
		self.grid(row=0, column=0, sticky="nsew")
		parent.grid_rowconfigure(0, weight=1)
		parent.grid_columnconfigure(0, weight=1)

		self.create_mainframe()
		self.create_board()
		self.show_board()

		#CONFIG BUTTON
		#self.buttonPixel = tk.PhotoImage(width=1, height=1)

		self.create_buttons()
		self.show_buttons()

	def create_mainframe(self):
		self.mainframe = tk.Frame(self, height=self.config.side, width=self.config.side, bg="black")
		self.mainframe.pack(expand=True)

	def create_board(self):
		self.frame_rows = [] #rows [0,1,2,3,4]

		color = 756867
		n_row, n_column = self.config.row, self.config.column
		row_height, row_width = self.config.side//n_row, self.config.side

		for i in range(n_row):
			row_color = f"#{color}"
			frame = tk.Frame(self.mainframe, height=row_height, width=row_width, bg=row_color)
			self.frame_rows.append(frame)
			color += 500

	def show_board(self):
		for every_frame in self.frame_rows:
			every_frame.pack()

	def put_and_resize_photo(self, ori_image, scale):
		n_column = self.config.column
		button_width = self.config.side//n_column-8

		image = Image.open(ori_image)
		image_w, image_h = image.size
		ratio = image_w/button_width
		new_size = (int(image_w//ratio//scale), int(image_h//ratio//scale))
		image = image.resize(new_size)
		return ImageTk.PhotoImage(image)

	def change_photo_button(self, pos_x, pos_y, win):
		if not win:
			self.buttons_board[pos_x][pos_y].configure(image=self.final_img_btn)
		else:
			self.buttons_board[pos_x][pos_y].configure(image=self.win_img_btn)

	def create_buttons(self):
		self.buttons_board = [] #button
		n_row, n_column = self.config.row, self.config.column
		button_height, button_width = self.config.side//n_row-8, self.config.side//n_column-8

		#image
		self.init_img_btn = self.put_and_resize_photo(self.config.init_img, 1)
		self.final_img_btn = self.put_and_resize_photo(self.config.final_img, 1)
		self.win_img_btn = self.put_and_resize_photo(self.config.win_img, 1) 

		for i in range(n_row):
			row = []
			for j in range(n_column):
				button = tk.Button(self.frame_rows[i], image=self.init_img_btn, height=button_height, width=button_width, command=lambda x=i, y=j:self.game.is_button_clicked(x, y)) #, compound="c", text="O", font=("Arial", 36, "bold")
				row.append(button)
			self.buttons_board.append(row)

	def show_buttons(self):
		n_row, n_column = self.config.row, self.config.column
		for i in range(n_row):
			for j in range(n_column):
				self.buttons_board[i][j].pack(side="left")

	# def clicked(self, pos_x, pos_y):
	# 	print(pos_x, pos_y)




