move(North)
move(East)
global end_ticks
end_ticks  = get_tick_count()
while True:
    if not (get_entity_type() == Entities.Hedge):
        plant(Entities.Bush)
        use_item(Items.Weird_Substance, num_unlocked(Unlocks.Mazes)*3)
    drecshons = [North, West, East, South]
    start_ticks = get_tick_count()
    while(True):
        rando = random()*4//1
        move(drecshons[rando])
        if (get_entity_type()==Entities.Treasure):
            harvest()
            end_ticks = get_tick_count()
            break   
    if (get_entity_type()==Entities.Treasure):
            harvest()
            end_ticks = get_tick_count()    
    print("Done in: ", (end_ticks - start_ticks)//1000," seconds maybe")            
        