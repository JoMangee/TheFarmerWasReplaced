plant(Entities.Bush)
n_substance = get_world_size() * num_unlocked(Unlocks.Mazes)
n_substance = 3
use_item(Items.Weird_Substance, n_substance)

def check_treasure():
    if (get_entity_type() == Entities.Treasure):
        harvest()
        return True
    else:
        return False
         

while(True):
    if move(South):
        if(not check_treasure()):
            break
    elif move(West):  
        if(not check_treasure()):
            break      
    elif move(North):  
        if(not check_treasure()):
            break  
    elif move(East):  
        if(not check_treasure()):
            break  