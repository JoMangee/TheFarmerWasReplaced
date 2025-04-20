move(North)
move(East)




global end_ticks
end_ticks  = get_tick_count()
global been
been = set()
global nextmove
nextmove = North

def dofindnext(x,y):    
    print("looking for TREASURE at (",x,",",y,")")
    while (not get_pos_x()==x):
        if(not move(West)):
            if (not move(South)):
              #change_hat(Hats.Straw_Hat)
              move(East)
              #change_hat(Hats.Dinosaur_Hat) 
    while (not get_pos_y()==y):
        if (not move(South)):
            if (not move(North)):
              #change_hat(Hats.Straw_Hat)
              move(East)
              #change_hat(Hats.Dinosaur_Hat)


#dofindnext(7,0)
while True:
    plant(Entities.Bush)
    use_item(Items.Weird_Substance, num_unlocked(Unlocks.Mazes)*3)
    drecshons = [North, West, East, South]
    op_drecshons = {North:South, West:East, East:West, South:North}
    rotation = {North:East, East:South, South:West, West:North}
    start_ticks = get_tick_count()
    while(True):
        x, y = get_pos_x(), get_pos_y()
        been.add((x,y))
        if len(drecshons) > 0:
            rando = random()*len(drecshons)//1
            while (move(drecshons[rando])):
                #we moved ok
                lastmove = drecshons[rando]
                nextmove = rotation[lastmove] # rotate to right 
            move(nextmove)
            nextmove = drecshons[rando]
        if (get_entity_type()==Entities.Treasure):
            harvest()
            end_ticks = get_tick_count()
            break   
    if (get_entity_type()==Entities.Treasure):
            x, y = measure()
            harvest()
            end_ticks = get_tick_count()    
    print("Done in: ", (end_ticks - start_ticks)//1000)    
    dofindnext(x,y)
