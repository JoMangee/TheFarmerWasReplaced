while(True):
    for i in range(get_pos_x(),get_world_size(),1):
        #print(i,get_pos_x(),get_pos_y(),get_world_size())
        if can_harvest():
           harvest()
        if (get_pos_x()%2 and get_pos_y()%2):
            plant(Entities.Tree)
            if(get_water() < 0.1):
                use_item(Items.Fertilizer)     
        if (get_pos_x()%3 and get_pos_y()+1%2): 
           plant(Entities.Carrot)
        if (get_pos_x()%3): 
            till()
            plant(Entities.Grass)
            if can_harvest():
                harvest()
        if (get_pos_y()%2 or get_pos_y()%3): 
            plant(Entities.Pumpkin)
        if (get_pos_x()%5 or get_pos_y()%5): 
            plant(Entities.Sunflower)
        if(get_water() < 0.1):
            use_item(Items.Water) 
        if can_harvest():
            harvest()
        elif (get_ground_type() != Grounds.Soil):
            till()
            plant(Entities.Carrot)
        move(East)    
    if (get_ground_type() == Grounds.Grassland):
        plant(Entities.Tree)
        use_item(Items.Fertilizer)
    elif (get_ground_type() == Grounds.Soil):
        if (get_pos_x()%2): 
            plant(Entities.Carrot)
        else: 
            plant(Entities.Pumpkin)
            #use_item(Items.Fertilizer)
    if (get_entity_type() == Entities.Grass):
        till()
        plant(Entities.Carrot)
    move(North)
        

    
