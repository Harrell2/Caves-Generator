from cellular_automata import startmap, update
import tcod
import numpy as np
from typing import Optional

#various states to be in depending on what key is pressed
class State:
    pass 
class EscapeState(State):
    pass 
class UpdateState(State):
    pass


class StateHandler(tcod.event.EventDispatch[State]):

    """this class handles which state the game should be"""
    
    #when clicking the x on window
    def ev_quit(self, event:tcod.event.Quit) -> Optional[State]:
        #closes the program
        raise SystemExit()
    
    #checks what key was presed
    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[State]:
        #sets the state as None when no key is pressed
        action: Optional[State] = None
        #holds what the key pressed was
        key = event.sym
        
        #the up arrow on keyboard
        if key == tcod.event.K_UP:
            action = UpdateState()
        
        #the escape key
        elif key == tcod.event.K_ESCAPE:
            action = EscapeState()
            
        return action


def map_render(console, map):

    """This function will go through the current map and render it on the window"""

    #loops through the map tracking its pos as the value
    for pos, value in np.ndenumerate(map):
        #splits pos into a x and y        
        pos_x, *rest, pos_y = pos
        #a value of 1 sets it as a 'wall' while a 0 makes it a 'floor'
        if value == 1:
            tile_gr = "#"
        else:
            tile_gr = "."
        console.print(x = pos_x - 1, y = pos_y - 1, string = tile_gr)

def main():
    map = startmap(82,52,47)
    screen_width = 80
    screen_height = 50
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )
    state_handler = StateHandler()
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset = tileset,
        title = "Cave",
        vsync = True,
    ) as context:
        console = tcod.Console(screen_width, screen_height, order = "F")
        
        while True:
            map_render(console,map)
            
            
            context.present(console)
            console.clear()
            for event in tcod.event.wait():
                action = state_handler.dispatch(event)
                
                if action is None:
                    continue
                    
                if isinstance(action,UpdateState):
                    update(5,1,map)
                    
                    
                elif isinstance(action,EscapeState):
                    raise SystemExit()
            
            

if __name__ == "__main__":
    main()
        