

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
    
def update(birth_req, death_req , map, type):
    """
    this function will check the cells surrounding to see if it will
    survive the next iterations or will 
    """
    
    """
    birth_req is the minimum amount of surrounding alive cells to turn alive(meant for dead cells)
    death_req is the minimum amount of surrounding alive cells to die(meant for alive cells)
    type is what method of cave generation you want(0 makes large hollow, while 1 makes a cool pattern)
    """
    
    #creates a new copy of the map so that when changing cells it doesnt interfere with itself
    new_map = map
    
    #iterates through the map and return the position and element value
    for pos, value in np.ndenumerate(new_map):
    
        #splits the position into its x and y values
        pos_x, *rest, pos_y = pos
        
        #finds the sum of all surrounding cells
        surrounding_cells = np.sum(new_map[pos_x - 1: pos_x + 2, pos_y - 1: pos_y + 2]) - new_map[pos_x, pos_y]
        #different method of finding nearby cells
        cross_cells = (np.sum(map[pos_x - 2: pos_x + 2, pos_y]) - map[pos_x,pos_y]) + (np.sum(map[pos_x, pos_y - 2: pos_y + 2]) - map[pos_x,pos_y])
        
        if type == 0:
            cross_cells = 190
        
        #checks if the cell is dead
        if value == 0:
            #checks if their is enough alive cells 
            if surrounding_cells > birth_req or cross_cells <= 1:
                #there are are enough so it becomes alive
                map[pos] = 1
                
        #checks if the cell is alive
        if value == 1:
            #checks if their are too much alive cells
            if surrounding_cells < death_req:
                #there are too much so it becomes dead
                map[pos] = 0
            
  
            
 
    return map


    
