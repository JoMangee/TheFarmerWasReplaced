from utils import *
rando = random()
worldsize = get_world_size()
traversalcount = 0
waittil = get_time()
while (True):
    if(get_water() < 0.01):
            use_item(Items.Water)
    if (random() > .5):
        if(move(North)):
               traversalcount+=1
        
        if can_harvest():
               harvest()
               if (get_ground_type() == Grounds.Grassland):
                   till()
               if (num_items(Items.Power) < 15):
                    if (get_ground_type() == Grounds.Grassland):
                       till()
                    plant(Entities.Sunflower)
               else:
                   plant(random_elem((Entities.Carrot,Entities.Tree,Entities.Cactus,Entities.Pumpkin,Entities.Sunflower)))
                   raise_water_level(.75)
               if(get_time()>waittil and not use_item(Items.Fertilizer)):
                   print("No fertilizer!")
                   waittil = get_time() + 20
                   use_item(Items.Weird_Substance)
   
    
    elif (random() > .8):
        if(move(West)):
               traversalcount+=1
        if can_harvest():
               harvest()
        if (get_ground_type() == Grounds.Grassland):
               till()       
        plant(random_elem((Entities.Carrot,Entities.Bush,Entities.Cactus,Entities.Pumpkin,Entities.Sunflower)))
        raise_water_level(.75)
    else:
        if can_harvest():
               harvest()
        if (get_ground_type() == Grounds.Grassland):
                till()
        plant(random_elem((Entities.Carrot,Entities.Tree,Entities.Cactus,Entities.Pumpkin,Entities.Sunflower)))
        raise_water_level(.75)
        use_item(Items.Weird_Substance)
        if(move(East)):
               traversalcount+=1
    if(traversalcount > worldsize*worldsize*3):
        soil_grid()
        clear()
        traversalcount = 0
        
        