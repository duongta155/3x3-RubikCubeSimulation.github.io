import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.ticker as plticker
import copy

#move Up clockwise
def moveUp():
    # get face color of the top patch
    col0 = top_patch[0].get_facecolor()
    col1 = top_patch[1].get_facecolor()
    col2 = top_patch[2].get_facecolor()
    col3 = top_patch[3].get_facecolor()
    col4 = top_patch[4].get_facecolor()
    col5 = top_patch[5].get_facecolor()
    col6 = top_patch[6].get_facecolor()
    col7 = top_patch[7].get_facecolor()
    col8 = top_patch[8].get_facecolor()

    for i in range(0,3):
        colF = front_patch[i+2*(i+1)].get_facecolor()
        colL = left_patch[i+2*(i+1)].get_facecolor()
        colB = back_patch[i+2*(i+1)].get_facecolor()
        colR = right_patch[i+2*(i+1)].get_facecolor()


        #set face color
        front_patch[i+2*(i+1)].set_facecolor(colR)
        left_patch[i+2*(i+1)].set_facecolor(colF)
        back_patch[i+2*(i+1)].set_facecolor(colL)
        right_patch[i+2*(i+1)].set_facecolor(colB)

    #set top face color
    top_patch[0].set_facecolor(col6)
    top_patch[1].set_facecolor(col3)
    top_patch[2].set_facecolor(col0)
    top_patch[3].set_facecolor(col7)
    top_patch[4].set_facecolor(col4)
    top_patch[5].set_facecolor(col1)
    top_patch[6].set_facecolor(col8)
    top_patch[7].set_facecolor(col5)
    top_patch[8].set_facecolor(col2)

#Move Right Clockwise
def moveRight():
    # get face color of the right patch
    col0 = right_patch[0].get_facecolor()
    col1 = right_patch[1].get_facecolor()
    col2 = right_patch[2].get_facecolor()
    col3 = right_patch[3].get_facecolor()
    col4 = right_patch[4].get_facecolor()
    col5 = right_patch[5].get_facecolor()
    col6 = right_patch[6].get_facecolor()
    col7 = right_patch[7].get_facecolor()
    col8 = right_patch[8].get_facecolor()

    for i in range(0,3):
        colF = front_patch[i+6].get_facecolor()
        colT = top_patch[i+6].get_facecolor()
        colB = back_patch[2-i].get_facecolor()
        colBo = bottom_patch[i+6].get_facecolor()
        # set face color
        top_patch[i+6].set_facecolor(colF)
        back_patch[2-i].set_facecolor(colT)
        bottom_patch[i+6].set_facecolor(colB)
        front_patch[i+6].set_facecolor(colBo)

    #set facecolor of the right patch
    right_patch[0].set_facecolor(col6)
    right_patch[1].set_facecolor(col3)
    right_patch[2].set_facecolor(col0)
    right_patch[3].set_facecolor(col7)
    right_patch[4].set_facecolor(col4)
    right_patch[5].set_facecolor(col1)
    right_patch[6].set_facecolor(col8)
    right_patch[7].set_facecolor(col5)
    right_patch[8].set_facecolor(col2)

#move Left Clockwise
def moveLeft():
    # get face color of the left patch
    col0 = left_patch[0].get_facecolor()
    col1 = left_patch[1].get_facecolor()
    col2 = left_patch[2].get_facecolor()
    col3 = left_patch[3].get_facecolor()
    col4 = left_patch[4].get_facecolor()
    col5 = left_patch[5].get_facecolor()
    col6 = left_patch[6].get_facecolor()
    col7 = left_patch[7].get_facecolor()
    col8 = left_patch[8].get_facecolor()

    for i in range(3):
        colF = front_patch[i].get_facecolor()
        colT = top_patch[i].get_facecolor()
        colB = back_patch[8-i].get_facecolor()
        colBo = bottom_patch[i].get_facecolor()
        #set face color
        top_patch[i].set_facecolor(colF)
        back_patch[8-i].set_facecolor(colT)
        bottom_patch[i].set_facecolor(colB)
        front_patch[i].set_facecolor(colBo)

    #set left patch color
    left_patch[0].set_facecolor(col2)
    left_patch[1].set_facecolor(col5)
    left_patch[2].set_facecolor(col8)
    left_patch[3].set_facecolor(col1)
    left_patch[4].set_facecolor(col4)
    left_patch[5].set_facecolor(col7)
    left_patch[6].set_facecolor(col0)
    left_patch[7].set_facecolor(col3)
    left_patch[8].set_facecolor(col6)

#move Down CounterWise
def moveDown():
    # get face color of the bottom patch
    col0 = bottom_patch[0].get_facecolor()
    col1 = bottom_patch[1].get_facecolor()
    col2 = bottom_patch[2].get_facecolor()
    col3 = bottom_patch[3].get_facecolor()
    col4 = bottom_patch[4].get_facecolor()
    col5 = bottom_patch[5].get_facecolor()
    col6 = bottom_patch[6].get_facecolor()
    col7 = bottom_patch[7].get_facecolor()
    col8 = bottom_patch[8].get_facecolor()

    for i in range(3):
        colF = front_patch[i*3].get_facecolor()
        colL = left_patch[i*3].get_facecolor()
        colB = back_patch[i*3].get_facecolor()
        colR = right_patch[i*3].get_facecolor()
        #set face color
        left_patch[i*3].set_facecolor(colF)
        back_patch[i*3].set_facecolor(colL)
        right_patch[i*3].set_facecolor(colB)
        front_patch[i*3].set_facecolor(colR)

    # set bottom patch color
    bottom_patch[0].set_facecolor(col2)
    bottom_patch[1].set_facecolor(col5)
    bottom_patch[2].set_facecolor(col8)
    bottom_patch[3].set_facecolor(col1)
    bottom_patch[4].set_facecolor(col4)
    bottom_patch[5].set_facecolor(col7)
    bottom_patch[6].set_facecolor(col0)
    bottom_patch[7].set_facecolor(col3)
    bottom_patch[8].set_facecolor(col6)

def moveForward():
    # get face color of the front patch
    col0 = front_patch[0].get_facecolor()
    col1 = front_patch[1].get_facecolor()
    col2 = front_patch[2].get_facecolor()
    col3 = front_patch[3].get_facecolor()
    col4 = front_patch[4].get_facecolor()
    col5 = front_patch[5].get_facecolor()
    col6 = front_patch[6].get_facecolor()
    col7 = front_patch[7].get_facecolor()
    col8 = front_patch[8].get_facecolor()

    for i in range(0,3):
        colT = top_patch[i*3].get_facecolor()
        colR = right_patch[2-i].get_facecolor()
        colBo = bottom_patch[8-3*i].get_facecolor()
        colL = left_patch[i+6].get_facecolor()

        #set face color
        right_patch[2-i].set_facecolor(colT)
        bottom_patch[8-3*i].set_facecolor(colR)
        left_patch[i+6].set_facecolor(colBo)
        top_patch[i*3].set_facecolor(colL)

    # set front patch color
    front_patch[0].set_facecolor(col6)
    front_patch[1].set_facecolor(col3)
    front_patch[2].set_facecolor(col0)
    front_patch[3].set_facecolor(col7)
    front_patch[4].set_facecolor(col4)
    front_patch[5].set_facecolor(col1)
    front_patch[6].set_facecolor(col8)
    front_patch[7].set_facecolor(col5)
    front_patch[8].set_facecolor(col2)

def moveBack():
    # get face color of the back patch
    col0 = back_patch[0].get_facecolor()
    col1 = back_patch[1].get_facecolor()
    col2 = back_patch[2].get_facecolor()
    col3 = back_patch[3].get_facecolor()
    col4 = back_patch[4].get_facecolor()
    col5 = back_patch[5].get_facecolor()
    col6 = back_patch[6].get_facecolor()
    col7 = back_patch[7].get_facecolor()
    col8 = back_patch[8].get_facecolor()

    for i in range(0,3):
        colT = top_patch[3*i+2].get_facecolor()
        colR = right_patch[8-i].get_facecolor()
        colBo = bottom_patch[6-3*i].get_facecolor()
        colL = left_patch[i].get_facecolor()

        #set face color
        right_patch[8-i].set_facecolor(colT)
        bottom_patch[6-3*i].set_facecolor(colR)
        left_patch[i].set_facecolor(colBo)
        top_patch[3*i+2].set_facecolor(colL)

    # set back patch color
    back_patch[0].set_facecolor(col2)
    back_patch[1].set_facecolor(col5)
    back_patch[2].set_facecolor(col8)
    back_patch[3].set_facecolor(col1)
    back_patch[4].set_facecolor(col4)
    back_patch[5].set_facecolor(col7)
    back_patch[6].set_facecolor(col0)
    back_patch[7].set_facecolor(col3)
    back_patch[8].set_facecolor(col6)

def moveShiftRight():
    # get face color of the right patch
    col0 = right_patch[0].get_facecolor()
    col1 = right_patch[1].get_facecolor()
    col2 = right_patch[2].get_facecolor()
    col3 = right_patch[3].get_facecolor()
    col4 = right_patch[4].get_facecolor()
    col5 = right_patch[5].get_facecolor()
    col6 = right_patch[6].get_facecolor()
    col7 = right_patch[7].get_facecolor()
    col8 = right_patch[8].get_facecolor()

    for i in range(3):
        colF = front_patch[8-i].get_facecolor()
        colBo = bottom_patch[8-i].get_facecolor()
        colB = back_patch[i].get_facecolor()
        colT = top_patch[8-i].get_facecolor()

        #set face color
        bottom_patch[8-i].set_facecolor(colF)
        back_patch[i].set_facecolor(colBo)
        top_patch[8-i].set_facecolor(colB)
        front_patch[8-i].set_facecolor(colT)

    # set facecolor of the right patch
    right_patch[0].set_facecolor(col2)
    right_patch[1].set_facecolor(col5)
    right_patch[2].set_facecolor(col8)
    right_patch[3].set_facecolor(col1)
    right_patch[4].set_facecolor(col4)
    right_patch[5].set_facecolor(col7)
    right_patch[6].set_facecolor(col0)
    right_patch[7].set_facecolor(col3)
    right_patch[8].set_facecolor(col6)


def moveShiftLeft():
    # get face color of the left patch
    col0 = left_patch[0].get_facecolor()
    col1 = left_patch[1].get_facecolor()
    col2 = left_patch[2].get_facecolor()
    col3 = left_patch[3].get_facecolor()
    col4 = left_patch[4].get_facecolor()
    col5 = left_patch[5].get_facecolor()
    col6 = left_patch[6].get_facecolor()
    col7 = left_patch[7].get_facecolor()
    col8 = left_patch[8].get_facecolor()

    for i in range(3):
        colF = front_patch[2-i].get_facecolor()
        colBo = bottom_patch[2-i].get_facecolor()
        colB = back_patch[i+6].get_facecolor()
        colT = top_patch[2-i].get_facecolor()

        #set face color
        bottom_patch[2-i].set_facecolor(colF)
        back_patch[i+6].set_facecolor(colBo)
        top_patch[2-i].set_facecolor(colB)
        front_patch[2-i].set_facecolor(colT)

    # set facecolor of the left patch
    left_patch[0].set_facecolor(col6)
    left_patch[1].set_facecolor(col3)
    left_patch[2].set_facecolor(col0)
    left_patch[3].set_facecolor(col7)
    left_patch[4].set_facecolor(col4)
    left_patch[5].set_facecolor(col1)
    left_patch[6].set_facecolor(col8)
    left_patch[7].set_facecolor(col5)
    left_patch[8].set_facecolor(col2)

def moveShiftUp():
    # get face color of the top patch
    col0 = top_patch[0].get_facecolor()
    col1 = top_patch[1].get_facecolor()
    col2 = top_patch[2].get_facecolor()
    col3 = top_patch[3].get_facecolor()
    col4 = top_patch[4].get_facecolor()
    col5 = top_patch[5].get_facecolor()
    col6 = top_patch[6].get_facecolor()
    col7 = top_patch[7].get_facecolor()
    col8 = top_patch[8].get_facecolor()

    for i in range(3):
        colF = front_patch[3*i+2].get_facecolor()
        colR = right_patch[3*i+2].get_facecolor()
        colB = back_patch[3*i+2].get_facecolor()
        colL = left_patch[3*i+2].get_facecolor()

        #set face color
        right_patch[3*i+2].set_facecolor(colF)
        back_patch[3*i+2].set_facecolor(colR)
        left_patch[3*i+2].set_facecolor(colB)
        front_patch[3*i+2].set_facecolor(colL)

    # set top face color
    top_patch[0].set_facecolor(col2)
    top_patch[1].set_facecolor(col5)
    top_patch[2].set_facecolor(col8)
    top_patch[3].set_facecolor(col1)
    top_patch[4].set_facecolor(col4)
    top_patch[5].set_facecolor(col7)
    top_patch[6].set_facecolor(col0)
    top_patch[7].set_facecolor(col3)
    top_patch[8].set_facecolor(col6)

def moveShiftDown():
     # get face color of the bottom patch
     col0 = bottom_patch[0].get_facecolor()
     col1 = bottom_patch[1].get_facecolor()
     col2 = bottom_patch[2].get_facecolor()
     col3 = bottom_patch[3].get_facecolor()
     col4 = bottom_patch[4].get_facecolor()
     col5 = bottom_patch[5].get_facecolor()
     col6 = bottom_patch[6].get_facecolor()
     col7 = bottom_patch[7].get_facecolor()
     col8 = bottom_patch[8].get_facecolor()

     for i in range(3):
         colF = front_patch[3*i].get_facecolor()
         colR = right_patch[3*i].get_facecolor()
         colB = back_patch[3*i].get_facecolor()
         colL = left_patch[3*i].get_facecolor()

         #set face color
         right_patch[3*i].set_facecolor(colF)
         back_patch[3*i].set_facecolor(colR)
         left_patch[3*i].set_facecolor(colB)
         front_patch[3*i].set_facecolor(colL)

     # set bottom patch color
     bottom_patch[0].set_facecolor(col6)
     bottom_patch[1].set_facecolor(col3)
     bottom_patch[2].set_facecolor(col0)
     bottom_patch[3].set_facecolor(col7)
     bottom_patch[4].set_facecolor(col4)
     bottom_patch[5].set_facecolor(col1)
     bottom_patch[6].set_facecolor(col8)
     bottom_patch[7].set_facecolor(col5)
     bottom_patch[8].set_facecolor(col2)

def moveShiftForward():
    # get face color of the front patch
    col0 = front_patch[0].get_facecolor()
    col1 = front_patch[1].get_facecolor()
    col2 = front_patch[2].get_facecolor()
    col3 = front_patch[3].get_facecolor()
    col4 = front_patch[4].get_facecolor()
    col5 = front_patch[5].get_facecolor()
    col6 = front_patch[6].get_facecolor()
    col7 = front_patch[7].get_facecolor()
    col8 = front_patch[8].get_facecolor()

    for i in range(3):
        colT = top_patch[3*i].get_facecolor()
        colL = left_patch[6+i].get_facecolor()
        colBo = bottom_patch[8-3*i].get_facecolor()
        colR = right_patch[2-i].get_facecolor()

        #set face color
        left_patch[6+i].set_facecolor(colT)
        bottom_patch[8-3*i].set_facecolor(colL)
        right_patch[2-i].set_facecolor(colBo)
        top_patch[3*i].set_facecolor(colR)

    # set front patch color
    front_patch[0].set_facecolor(col2)
    front_patch[1].set_facecolor(col5)
    front_patch[2].set_facecolor(col8)
    front_patch[3].set_facecolor(col1)
    front_patch[4].set_facecolor(col4)
    front_patch[5].set_facecolor(col7)
    front_patch[6].set_facecolor(col0)
    front_patch[7].set_facecolor(col3)
    front_patch[8].set_facecolor(col6)

def moveShiftBack():
    # get face color of the back patch
    col0 = back_patch[0].get_facecolor()
    col1 = back_patch[1].get_facecolor()
    col2 = back_patch[2].get_facecolor()
    col3 = back_patch[3].get_facecolor()
    col4 = back_patch[4].get_facecolor()
    col5 = back_patch[5].get_facecolor()
    col6 = back_patch[6].get_facecolor()
    col7 = back_patch[7].get_facecolor()
    col8 = back_patch[8].get_facecolor()

    for i in range(3):
        colT = top_patch[2+3*i].get_facecolor()
        colL = left_patch[i].get_facecolor()
        colBo = bottom_patch[6-3*i].get_facecolor()
        colR = right_patch[8-i].get_facecolor()

        #set face color
        left_patch[i].set_facecolor(colT)
        bottom_patch[6-3*i].set_facecolor(colL)
        right_patch[8-i].set_facecolor(colBo)
        top_patch[2+3*i].set_facecolor(colR)

    # set bottom patch color
    back_patch[0].set_facecolor(col6)
    back_patch[1].set_facecolor(col3)
    back_patch[2].set_facecolor(col0)
    back_patch[3].set_facecolor(col7)
    back_patch[4].set_facecolor(col4)
    back_patch[5].set_facecolor(col1)
    back_patch[6].set_facecolor(col8)
    back_patch[7].set_facecolor(col5)
    back_patch[8].set_facecolor(col2)

def InputHandle(str):
    arr = str.lower().split()
    print(arr)
    for i in arr:
        if i == 'u': moveUp()
        if i == 'r': moveRight()
        if i == 'l': moveLeft()
        if i == 'd': moveDown()
        if i == 'f': moveForward()
        if i == 'b': moveBack()
        if i == "u'": moveShiftUp()
        if i == "r'": moveShiftRight()
        if i == "l'": moveShiftLeft()
        if i == "d'": moveShiftDown()
        if i == "f'": moveShiftForward()
        if i == "b'": moveShiftBack()


#reset view of the Rubik
def reset():
    for i in range(9):
        front_patch[i].set_facecolor('red')
        right_patch[i].set_facecolor('yellow')
        back_patch[i].set_facecolor('orange')
        left_patch[i].set_facecolor('white')
        bottom_patch[i].set_facecolor('green')
        top_patch[i].set_facecolor('blue')

width = 3
height = 3
lins =(0,9)
front_patch = [0]*9
top_patch = [0]*9
right_patch = [0]*9
left_patch = [0]*9
bottom_patch = [0]*9
back_patch = [0]*9
intervals = 3
# define figure
fig1 = plt.figure()
# define faces
front_face = fig1.add_subplot(345, aspect='equal', title = "Front face")
top_face = fig1.add_subplot(341, aspect='equal', sharex=front_face, sharey=front_face, title = "Top face")
right_face = fig1.add_subplot(346, aspect='equal', sharex=front_face, sharey=front_face, title = "Right face")
bottom_face = fig1.add_subplot(349, aspect='equal', sharex=front_face, sharey=front_face, title = "Bottom face")
left_face = fig1.add_subplot(348, aspect='equal', sharex=front_face, sharey=front_face, title = "Left face")
back_face = fig1.add_subplot(347, aspect='equal', sharex=front_face, sharey=front_face, title = "Back face")

front_face.axes.get_xaxis().set_visible(False)
front_face.axes.get_yaxis().set_visible(False)
top_face.axes.get_xaxis().set_visible(False)
top_face.axes.get_yaxis().set_visible(False)
right_face.axes.get_xaxis().set_visible(False)
right_face.axes.get_yaxis().set_visible(False)
bottom_face.axes.get_xaxis().set_visible(False)
bottom_face.axes.get_yaxis().set_visible(False)
left_face.axes.get_xaxis().set_visible(False)
left_face.axes.get_yaxis().set_visible(False)
back_face.axes.get_xaxis().set_visible(False)
back_face.axes.get_yaxis().set_visible(False)

# define patches
front_patch[0] = patches.Rectangle((0,0), width, height, facecolor ='red', edgecolor = 'black')
front_patch[1]=patches.Rectangle((0,3), width, height, facecolor ='red', edgecolor = 'black')
front_patch[2]=patches.Rectangle((0,6), width, height, facecolor ='red', edgecolor = 'black')
front_patch[3]=patches.Rectangle((3,0), width, height, facecolor ='red', edgecolor = 'black')
front_patch[4]=patches.Rectangle((3,3), width, height, facecolor ='red', edgecolor = 'black')
front_patch[5]=patches.Rectangle((3,6), width, height, facecolor ='red', edgecolor = 'black')
front_patch[6]=patches.Rectangle((6,0), width, height, facecolor ='red', edgecolor = 'black')
front_patch[7]=patches.Rectangle((6,3), width, height, facecolor ='red', edgecolor = 'black')
front_patch[8]=patches.Rectangle((6,6), width, height, facecolor ='red', edgecolor = 'black')
for i in range(9):
    front_face.add_patch(front_patch[i])
    top_patch[i] = copy.copy(front_patch[i])
    top_patch[i].axes = None
    top_patch[i].set_transform(top_face.transData)
    top_patch[i].set_facecolor('blue')
    top_face.add_patch(top_patch[i])
    right_patch[i] = copy.copy(front_patch[i])
    right_patch[i].axes = None
    right_patch[i].set_transform(right_face.transData)
    right_patch[i].set_facecolor('yellow')
    right_face.add_patch(right_patch[i])
    left_patch[i] = copy.copy(front_patch[i])
    left_patch[i].axes = None
    left_patch[i].set_transform(left_face.transData)
    left_patch[i].set_facecolor('white')
    left_face.add_patch(left_patch[i])
    bottom_patch[i] = copy.copy(front_patch[i])
    bottom_patch[i].axes = None
    bottom_patch[i].set_transform(bottom_face.transData)
    bottom_patch[i].set_facecolor('green')
    bottom_face.add_patch(bottom_patch[i])
    back_patch[i] = copy.copy(front_patch[i])
    back_patch[i].axes = None
    back_patch[i].set_transform(back_face.transData)
    back_patch[i].set_facecolor('orange')
    back_face.add_patch(back_patch[i])

# yourvar = input('Enter a sequence of moves: ')
# InputHandle(yourvar)

moveRight()
moveUp()
moveLeft()
moveShiftForward()
moveDown()
moveLeft()
moveShiftDown()
moveShiftBack()

plt.ylim(lins)
plt.xlim(lins)
plt.show()
