#plant all pumpkins
global plants
global plant2
global oplant2
plants = Entities.Bush
plant2 = Entities.Tree
global makehay
makehay = True

global waittil
waittil = get_time()
oplant2 = plant2
global occurx
occurx = 2
global occury
occury = 2
change_hat(Hats.Straw_Hat)
#change_hat(Hats.Dinosaur_Hat) 
global movediry
movediry = North 
global movedirx
movedirx = East 

def plant_run(vplants = Entities.Bush, vplant2 = Entities.Tree, vmakehay = False,voccurx =2, voccury = 2):
   global plants
   plants = vplants
   global plant2
   plant2 = vplant2
   global makehay
   makehay = vmakehay
   global occurx
   occurx = voccurx
   global occury
   occury = voccury
   plant_plenty()

def plant_plenty():
 while(num_items(Items.Hay) < 100000):
    #change_hat(Hats.Dinosaur_Hat)
    for i in range(get_pos_x(),get_world_size(),1):
        #quick_print(i,get_pos_x(),get_pos_y(),get_world_size())
        if can_harvest():
           if(get_entity_type()==Entities.Cactus):
               from cactus_hunt import sortCactus
               if (sortCactus()>60):
                   harvest()
               if(measure() > 7):
                   harvest()
           else:
               harvest()
           if (not makehay and get_ground_type() == Grounds.Grassland):
               till()
           if (makehay and get_ground_type() == Grounds.Soil):
               till()
        else:
            use_item(Items.Fertilizer)
        if(get_water() < 0.01):
            use_item(Items.Water)
            if (get_ground_type() == Grounds.Soil):
              plant(Entities.Sunflower)
            global waittil
            if(get_time()>waittil and not use_item(Items.Fertilizer)):
                   print("No fertilizer!")
                   waittil = get_time() + 20
            #    use_item(Items.Water)  
        if (get_pos_x()%occurx and get_pos_y()%occury):
            if (num_items(Items.Power) < 15):
                if (get_ground_type() == Grounds.Grassland):
                   till()
                plant(Entities.Sunflower)
            else:
                if(not makehay and not plant(plant2)):
                    till() 
                    plant(plant2)
                elif makehay:
                    if(not get_ground_type() == Grounds.Grassland):
                        till()
        else:
            if(not makehay and not plant(plants)):
                    till() 
                    if(not plant(plants)):
                        till()
                        plant(plants)
            elif makehay:
                    if(not get_ground_type() == Grounds.Grassland):
                        till()
                #use_item(Items.Fertilizer)
        global movedirx
        global movediry
        if(not move(movedirx)):
           if movedirx == West:
               movedirx = West#East
           else:
               movedirx = West                
           move(movedirx)   
    if (not move(movediry)):
       if movediry == North:
               movediry = North#East
       else:
               movediry = North        
       move(movediry)
       
 change_hat(Hats.Straw_Hat)
 if can_harvest():
   harvest()
 move(movedirx)
 if can_harvest():
   harvest()
 move(movediry)
 
 
plant_plenty()