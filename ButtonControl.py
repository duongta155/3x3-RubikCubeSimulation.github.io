import matplotlib.pyplot as plt
import matplotlib.patches as patches
import tkinter as tk
from RubikStart import *

def write_slogan():
    print("Tkinter is easy to use!")

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()



plt.ylim(lins)
plt.xlim(lins)
plt.ion()
plt.show()
plt.pause(.5)

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(fill=tk.BOTH,expand=1)
reset = tk.Button(frame,
                   text="Reset",
                   command=reset)
reset.pack(fill=tk.BOTH,expand =1)
up = tk.Button(frame,
                   text="Up",
                   command=moveUp)
up.pack(side=tk.RIGHT, fill=tk.Y)

right = tk.Button(frame,
                   text="Right",
                   command=moveRight)
right.pack(side=tk.RIGHT, fill=tk.Y)

left = tk.Button(frame,
                   text="Left",
                   command=moveLeft)
left.pack(side=tk.RIGHT, fill=tk.Y)

down = tk.Button(frame,
                   text="Down",
                   command=moveDown)
down.pack(side=tk.RIGHT, fill=tk.Y)

front = tk.Button(frame,
                   text="Front",
                   command=moveFront)
front.pack(side=tk.RIGHT, fill=tk.Y)

back = tk.Button(frame,
                   text="Back",
                   command=moveBack)
back.pack(side=tk.RIGHT, fill=tk.Y)
back_reverse= tk.Button(frame,
                   text="Back Reverse",
                   command=moveShiftBack)
back_reverse.pack(fill=tk.X)
up_reverse= tk.Button(frame,
                   text="Up Reverse",
                   command=moveShiftUp)
up_reverse.pack(fill=tk.X)
right_reverse= tk.Button(frame,
                   text="Right Reverse",
                   command=moveShiftRight)
right_reverse.pack(fill=tk.X)
left_reverse= tk.Button(frame,
                   text="Left Reverse",
                   command=moveShiftLeft)
left_reverse.pack(fill=tk.X)
down_reverse= tk.Button(frame,
                   text="Down Reverse",
                   command=moveShiftDown)
down_reverse.pack(fill=tk.X)
front_reverse= tk.Button(frame,
                   text="Front Reverse",
                   command=moveShiftFront)
front_reverse.pack(fill=tk.X)
plt.show()
plt.pause(.1)
root.mainloop()
"""
str = ""
while True:
    str = input("Command: ")
    command(str)
    plt.show()
    plt.pause(.1)
    
"""
#write_slogan()
