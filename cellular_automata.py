
import numpy as np
import random

def startmap(width, height, fill_chance):

    """
    this function creates a starting map with various cells being already alive, this map 
    will later be updated to create cellular automata
    """
    
    """
    width is how many tiles wide the map is
    height is the height of map
    fill_chance is the chance a cell is 'alive at start'
    """
    
    #creates an array filled with 0 that is width x height large
    map = np.zeros((width, height), order = 'F')
    
    #goes through every value in the empty map
    for pos, a in np.ndenumerate(map):
        #gets a random number from 0-100(this lines up with percentage)
        tile = random.randint(0, 100)
        
        #checks if the value is at or below the number we set
        if tile <= fill_chance:
            #sets the cell to 'alive'
            map[pos] = 1

    
    return map
    
def update(birth_req, death_req , map):
    """
    this function will check the cells surrounding to see if it will
    survive the next iterations or will 
    """
    
    """
    birth_req is the minimum amount of surrounding alive cells to turn alive(meant for dead cells)
    death_req is the minimum amount of surrounding alive cells to die(meant for alive cells)
    survive_req is the minimum amount of surrounding alive cells to stay alive()
    """
    #iterates through the map and return the position and element value
    for pos, value in np.ndenumerate(map):
    
        #splits the position into its x and y values
        pos_x, *rest, pos_y = pos
        
        #finds the sum of all surrounding cells
        #ps if its a border cell then it checks with a empty array 
        surrounding_cells = np.sum(map[pos_x - 1: pos_x + 2, pos_y - 1: pos_y + 2]) - map[pos_x, pos_y]
        #different method of finding nearby cells
        cross_cells = (np.sum(map[pos_x - 2: pos_x + 2, pos_y]) - map[pos_x,pos_y]) + (np.sum(map[pos_x, pos_y - 2: pos_y + 2]) - map[pos_x,pos_y])
        
        #checks if the cell is dead
        if value == 0:
            #checks if their is enough alive cells 
            if surrounding_cells <= birth_req or cross_cells <= 1:
                #there isnt enough so it stays dead
                continue
            #there are enough so it becomes alive
            map[pos] = int(1)
            
        #checks if the cell is alive
        if value == 1:
            #checks if their are too much alive cells
            if surrounding_cells > death_req:
                #there arent enough so it stays alive
                continue
            
            #there are too much so it becomes dead
            map[pos] = int(0)
         
    return map



    