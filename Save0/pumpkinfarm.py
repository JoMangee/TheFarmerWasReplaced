from utils import * 
world_size = get_world_size()
soil_grid()
move_to_origin()
totalPumpkins = 0
while True:

    for i in range(world_size):
        for j in range(world_size):
            if can_harvest():
                totalPumpkins += 1
            else:
                totalPumpkins = 0
                raise_water_level(.75)
            if totalPumpkins >= world_size*world_size:
                harvest() 
            if (not get_ground_type() == Grounds.Soil):
               till()
            while(not get_entity_type() == Entities.Pumpkin):
              if not plant(Entities.Pumpkin):
                  harvest()
            move(East)
        move(North)
            