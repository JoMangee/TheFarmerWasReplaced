#clean up
from utils import *

def sortCactus():
    allus = 0
    if get_entity_type() == Entities.Cactus:
        us = measure() #check current postion
        them = measure(North)
        if (not them == None):
            allus += us + them
            if (us > them):
                swap(North)
        us = measure() #check current postion
        them = measure(East)
        if (not them == None):
            allus += us + them
            if (us > them):
                swap(East)
        us = measure() #check current postion
        them = measure(South)
        if (not them == None):
            allus += us + them
            if (us > them):
                swap(South)
        us = measure() #check current postion
        them = measure(West)
        if (not them == None):
            allus += us + them
            if (us > them):
                swap(West)
    return allus


def dohunting():
    move_to_origin()
    while(True):
        change_hat(Hats.Straw_Hat)
        world_size = get_world_size()
        entity = Entities.Cactus
        for i in range(world_size):
            for j in range(world_size):
                sortCactus()
                size = measure() 
                if(size!=None and size > 10):
                    try_harvest()
                try_plant(entity)
                move(West)
            move(South)
    
        for i in range(0,get_world_size(),1):
            for j in range(0,get_world_size(),1):
              if can_harvest():
                  if sortCactus()>60:
                      harvest()
                  elif (get_entity_type() != Entities.Cactus):
                      harvest()
              if (get_ground_type() == Grounds.Grassland):
                  till()
              planted = plant(entity)
              if(get_water() < 0.01):
                  use_item(Items.Water)
              move(South)
            move(West)  
        sortCactus()
    plant(Entities.Cactus)

dohunting()

     
        
    
    