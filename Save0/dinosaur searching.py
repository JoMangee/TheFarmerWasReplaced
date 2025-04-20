size = get_world_size()//2
change_hat(Hats.Straw_Hat)
global next_x
next_x = size
global next_y
next_y = size

def dofindnext(x,y):    
    print("looking for apple at (",x,",",y,")")
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
    print("not looking anymore")
  
dofindnext(size,size)                      
def doplant():
    #Does some planting and harvesting
    if(get_entity_type() == Entities.Apple):
        next_x, next_y = measure()
        print(next_x, next_y)
        dofindnext(next_x,next_y)       
    if can_harvest():
        harvest()
    elif (get_ground_type() == Grounds.Grassland):
        till()
    if(get_water() < 0.01):
        use_item(Items.Water)
        #use_item(Items.Fertilizer)
    #plant(Entities.Pumpkin)

          
change_hat(Hats.Dinosaur_Hat)

while(True):
    for layer in range(1, 3):  # Layers around the center
        # Move to the starting position of the layer (top side)
        move(North)   
        for i in range(layer - 1):
            move(West)
            doplant()
        # Traverse the top side
        for i in range(2 * layer):
            move(East)
            doplant()
        # Traverse the right side
        for i in range(2 * layer):  
            move(South)
            doplant()
        # Traverse the bottom side
        for i in range(2 * layer):
            move(West)
            doplant()
        # Traverse the left side
        for i in range(2 * layer):
            move(North)
            doplant()
            
            
    dofindnext(next_x,next_y)