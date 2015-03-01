from modules import *
from Tkinter import *
from tkFont import Font

grid = zeros(16).reshape(4,4)
add_new_tile(grid)
add_new_tile(grid)	
score = 0
can_play = True
intList = []
size = 480


def key_listener(event):
	key = '{}'.format(event.keysym)
	print key

if __name__ == '__main__':
	root = Tk()
	root.geometry("480x480")
	gridSize = 480
	for (m, n), value in ndenumerate(grid):
	    frame = Frame(root, width=size/4-2, height=size/4-2)
	    font = Font(family='Helvetica', weight='bold', size=size/16	)
	    frame.pack_propagate(0)
	    frame.place(x=n*size/4+1, y=m*size/4+1)
	    label = Label(frame, text=int(value), font=font, fg='#ffffff', bg='#000000')
	    label.pack(fill=BOTH, expand=True)
	root.bind('<Key>', lambda event: key_listener(event))
	root.mainloop()


	'''
	while can_play==True or score>=2048:
		print grid
		direction = raw_input("Enter direction: ")
		prev = grid
		grid = move_board(grid, direction)
		if (grid == prev).all():
			pass
		else:
			add_new_tile(grid)
			can_play = has_next(grid)

'''


