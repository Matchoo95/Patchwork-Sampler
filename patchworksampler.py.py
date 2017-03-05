# PYTHON COURSEWORK: A PATCHWORK SAMPLER
# 769535
# TERM 1

from graphics import *


def main():

    patchWorkSize = 0
    colours = ["", "", ""]
    
    #get user inputs
    patchWorkSize, colours = userInputs()
    
    #draws patchwork and patches patches
    drawPatchwork(patchWorkSize, colours)
    

def userInputs():
    
    #sets available patchwork sizes
    availableSizes = ['5', '7', '9']
    
    
    patchWorkSize = input("Enter the number of size of the patchwork, " \
                            "available options are '5', '7' or '9': ")  
   
    #checks whether the previous user input is a valid patchwork size
    while patchWorkSize not in availableSizes or patchWorkSize.isalpha():
        patchWorkSize = input("Please input a valid measurements " \
                                "e.g. '5', '7' or '9': ")
    
    #sets available colours
    availableColours = ['red', 'green', 'blue', 'orange', 'magenta', 'cyan']
    
    #sets a colour list for adding the colours to
    colours = []   
    
    #asks the user to input a colour, repeats 3 times for 3 different colours
    for i in range(3):
        getColours = input("Enter a colour for the patch design, a list of " \
                            "available colours can be request by typing " \
                            "'colours', you can't have the same colour " \
                            "more than once: ")
        
        #checks if the colour is available or if it was already chosen
        while getColours not in availableColours or getColours in colours:
            getColours = input("Please enter a valid colour: ")
        
        #displays a list of colours if the user inputs "colours"
        if getColours == "colours":
            print(availableColours)
            
        #other whys adds the inputted colours to the colours list
        elif getColours in availableColours:
            colours.append(getColours)
            
        #if the user inputs anything else, then this asks for the colour again
        else:
            getColours = input("Please enter a valid colour: ")
                
    
    return int(patchWorkSize), colours
 
 
def drawPatchwork(patchWorkSize, colours):
    
    win = GraphWin("patchwork", (patchWorkSize * 100), (patchWorkSize * 100))
    win.setBackground("white")
    
    #sets coordinates
    x = 0
    y = 0
    
    #used to count through colours
    colour = 0 
    
    #determines where the diagonal pattern position should be
    diagonalPattern = patchWorkSize - 1
    
    #draws the border and patterns in the correct positions
    for j in range(patchWorkSize):
       
        for k in range(patchWorkSize):
            
            #draws square sections for the patterns to be in
            backgroundBorder = Rectangle(Point(x, y), Point(x + 100, y + 100))
            backgroundBorder.draw(win)
            
            #checks j + k is within the diagonal pattern
            if j + k == diagonalPattern:
                
                #if they are then draw patch one with the selected colour
                drawPatchOne(win, (x + 50), (y + 45), \
                            patchWorkSize, colours[colour])
                            
            else:
                
                #if they aren't then draw patch two with the selected colour
                drawPatchTwo(win, (x + 5), (y + 5), \
                            patchWorkSize, colours[colour])
                            
            
            colour += 1
            
            #resets the colour counter if it goes above 2
            if colour > 2:
                colour = 0
            
            #moves the loop across so that the next grid and pattern is drawn
            x += 100
            
        #resets x and moves downwards so that the next row can be drawn
        x = 0
        y += 100
    
    
    win.mainloop()
    


def drawPatchOne(win, x, y, patchWorkSize, colour): 

    radius = 55
    
    #creates 10 circles of different sizes and radius to create the pattern
    for l in range(10):
        
        #decreases the radius each iteration
        radius = radius - 5
        
        #increases the vertical size of each circle, each iteration
        y = y + 5
        
        centre = Point(x, y)
        loops = Circle(centre, radius)
        loops.setOutline(colour)
        loops.setWidth(1)
        loops.draw(win)



def drawPatchTwo(win, x, y, patchWorkSize, colour):
    
    #used to reset the value of y later on
    tempY = y
 
    #draws the squareCircles function in the correct pattern
    for m in range(3):
        
        for n in range(3):
            
            #grabs the squareCircles function to draw the basic shape
            squareCircles(win, x, y, colour)
            
            #changes the y coordinate for the next position of the shape
            y += 35
            
        #resets y and draws shape on each row by changing the x coordinate
        y = tempY
        x += 35



def squareCircles(win, x, y, colour):
    
    radius = 5
    
    #used to reset the value of y later on
    tempY = y
   
    #draws a 3 x 3 square of circles with the center being a white circle
    for o in range(3):
        
        for p in range(3):
            
            #draws a mini circle based on the x, y from drawPatchwork
            miniCircle = Circle(Point(x, y), radius)
            
            #if statement for finding the center circle and filling it white
            if o == 1 and p == 1:
                
                miniCircle.setFill("white")
                
            else:               
                
                miniCircle.setFill(colour)
            
            miniCircle.draw(win)
            
            #changes the y coordinate for the next position of the circle
            y += 10
            
        #resets y and draws circle on each row by changing the x coordinate
        y = tempY
        x += 10
  
main()