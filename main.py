# coding: utf-8
# Jeu de la vie de Anne-Soline (la vie de Anne-Soline)

# Utilisation de la librairie graphique tkinter
from tkinter import * 
import random
from grid_cell import GridCell

fenetre = Tk()
fenetre.title('Jeu de la vie - Projet Anne-Soline')

# Définition des constantes
WINDOW_SIZE = 720


# Définition des variables de jeu
pourcent_life = 20
game_speed = 100
game_loop_state = False
size_slider_state = NORMAL

grid_size = 30
cell_size = WINDOW_SIZE // grid_size
grid = []




# CANVAS GAME
canvas = Canvas(fenetre, width=WINDOW_SIZE, height=WINDOW_SIZE, background='white')

def game_loop():
	if game_loop_state:
		next_step()
	fenetre.after(game_speed, game_loop)

def next_step():
	global grid
	new_grid = grid

	temp_grid_states = [[False for i in range(grid_size)] for j in range(grid_size)]
	for y in range(0, grid_size):
		for x in range(0, grid_size):
			temp_grid_states[y][x] = grid[y][x].state

	for y in range(0, grid_size):
		for x in range(0, grid_size):
			alive_arround_count = 0
			for i in range(-1, 2):
				for j in range(-1, 2):
					if not (i == 0 and j == 0):
						if(x + i >= 0 and x + i < grid_size and y + j >= 0 and y + j < grid_size):
							if(temp_grid_states[y + j][x + i]):
								alive_arround_count += 1

			# CASE alive
			if(grid[y][x].state):
				if(not (alive_arround_count == 2 or alive_arround_count == 3)):
					grid[y][x].state = False
			# CASE dead
			else:
				if(alive_arround_count == 3):
					grid[y][x].state = True

	grid = new_grid

def blank_grid():
	rectangle = canvas.create_rectangle(0,0,WINDOW_SIZE,WINDOW_SIZE,fill="white")

def init_grid():
	blank_grid()
	global grid
	grid = [[None for i in range(grid_size)] for j in range(grid_size)]
	
	for y in range(0, grid_size):
		for x in range(0, grid_size):
			grid[y][x] = GridCell(canvas, x*cell_size, y*cell_size, cell_size, False)
	fill_with_random_values()

def fill_with_random_values():
	global grid
	current_completion = 0
	goal = int(pourcent_life * (grid_size * grid_size) / 100)
	while current_completion < goal:
		for line in grid:
			for cell in line:				
				if(current_completion >= goal):
					break
				if(not cell.state):
					if(current_completion >= goal):
						break
					pick = random.randint(1, 100)
					if(pick <= pourcent_life):
						cell.state = True
						current_completion += 1


# COMMANDS
def speed_command(val):
	global game_speed
	game_speed = int(val) * 10

def size_command(val):
	global grid_size, cell_size 
	grid_size = int(val)
	cell_size = WINDOW_SIZE // grid_size

def pourcent_life_command(val):
	global pourcent_life
	pourcent_life = int(val)

def stop_command():
	global game_loop_state, size_slider_state
	game_loop_state = False
	size_slider_state = NORMAL

def start_command():
	global game_loop_state, size_slider_state
	game_loop_state = True
	size_slider_state = DISABLED
	
def reset_command():
	global grid
	init_grid()

# INTERFACE
start_btn = Button(fenetre, text="Lancer", command=start_command)
stop_btn = Button(fenetre, text="Arrêter", command=stop_command)
reset_btn = Button(fenetre, text="Réinitialiser", command=reset_command)
exit_btn = Button(fenetre, text="Quitter", command=fenetre.quit)

## sliders
size_label = Label(fenetre, text="Taille de la grille")
size_slider = Scale(fenetre, from_=4, to=100, orient=HORIZONTAL, command=size_command, state=size_slider_state)
size_slider.set(grid_size)

pourcent_life_label = Label(fenetre, text="% de vie")
pourcent_life_slider = Scale(fenetre, from_=0, to=100, orient=HORIZONTAL, command=pourcent_life_command)
pourcent_life_slider.set(pourcent_life)

speed_label = Label(fenetre, text="Vitesse en ms")
speed_slider = Scale(fenetre, from_=10, to=300, orient=HORIZONTAL, command=speed_command)
speed_slider.set(game_speed / 10)

# PACK
canvas.pack(side=LEFT, padx=5, pady=5)
start_btn.pack(side=TOP, padx=5, pady=5)
stop_btn.pack(side=TOP, padx=5, pady=5)
reset_btn.pack(side=TOP, padx=5, pady=5)
exit_btn.pack(side=BOTTOM, padx=5, pady=(50, 10))
speed_slider.pack(side=BOTTOM, pady=(0, 30))
speed_label.pack(side=BOTTOM)
pourcent_life_slider.pack(side=BOTTOM, pady=(0, 30))
pourcent_life_label.pack(side=BOTTOM)
size_slider.pack(side=BOTTOM, pady=(0, 30))
size_label.pack(side=BOTTOM)

# RUN
init_grid()
fenetre.after(game_speed, game_loop)
fenetre.mainloop()