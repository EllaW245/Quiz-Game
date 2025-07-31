from tkinter import *
import random

root = Tk()
root.geometry("1200x800")
root.title("Randomized Boxes")

# 1. Create the boxes
box_colors = ["red", "blue", "green", "yellow"]
boxes = []
for color in box_colors:
    box = Button(root, width = 50, height = 10, background = color)
    boxes.append(box)

# 2. Define grid positions
grid_positions = [(80, 400), (80, 600), (500, 400), (500, 600)]

# 3. Randomize the order of grid positions
random.shuffle(grid_positions)


#4. Assign a position to each box
'''for box in boxes:
    box.place(enumerate(grid_positions))

# 4. Assign the positions of the boxes
for position, (xpos, ypos) in enumerate(grid_positions):
    for box in boxes: 
        box.configure(x=xpos, y=ypos)
        print(xpos, ypos)'''
'''for i, box in enumerate(boxes):
    xpos, ypos = grid_positions[i]
    box.place(x=xpos, y=ypos)'''
for i, (row, col) in enumerate(grid_positions):
    boxes[i].place(x=row, y=col)
    


root.mainloop()

       

























