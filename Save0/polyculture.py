from utils import *
move_to_origin()
global traversalcount
traversalcount = 0

def getcomp():
    #coord = get_pos_x(), get_pos_y()
    toplant = get_companion()
    if not toplant == None:
        move_to(toplant[1][0],toplant[1][1])
    else: 
        return False
    try_plant(toplant[0])
    global traversalcount
    traversalcount+=1
    #move_to(coord[0],coord[1])
    return True

def polyculture():
    global traversalcount
    traversalcount = 0
    worldsize2 = get_world_size()*get_world_size()
    while True:
       if can_harvest():
                harvest()
                if (get_ground_type() == Grounds.Grassland):
                    till()       
                plant(random_elem((Entities.Carrot,Entities.Bush,Entities.Cactus,Entities.Pumpkin,Entities.Sunflower)))
                raise_water_level(.75)
                getcomp()
       elif not getcomp():
                move(East)
                traversalcount+=1
                if (num_items(Items.Power) < 15):
                    if (get_ground_type() == Grounds.Grassland):
                       till()
                    plant(Entities.Sunflower)
                    move(North)
                    traversalcount+=1
       if(traversalcount > worldsize2*4):
           soil_grid()
           clear()
           traversalcount = 0

polyculture()    