move(East)
next_x = 1
xy = get_pos_x(), get_pos_y()
change_hat(Hats.Dinosaur_Hat)


def move_around_board(board_size, action, action_items):
    # Assume the board is board_size * board_size or a perfect square
    for i in range(board_size):
        for i in range(board_size):
            action(action_items[0], action_items[1]) # do the action
            move(East)
        move(North)
        
        
def re_plant(plant_type, seed_type):
    if can_harvest():
        harvest()
    if get_ground_type() != Grounds.Soil:
        till()
    if seed_type != None and num_items(seed_type) == 0:
        trade(seed_type)    # Better way to do this but don't care as this is for simplicity
    plant(plant_type)
    
while num_items(Items.Carrot) < 1000: # Get a decent number of carrots
    move_around_board(get_board_size(), move_around_board, (Entities.Carrot,None))
    
def move_around_board(board_size, action, action_items):
    # Assume the board is board_size * board_size or a perfect square
    for i_1 in range(board_size):
        for i_2 in range(board_size):
            action(action_items[0], action_items[1]) # do the action
            move(East)
        move(North)

def re_plant(plant_type, seed_type):
    if can_harvest():
        harvest()
    if get_ground_type() != Grounds.Soil:
        till()
    if seed_type != None and num_items(seed_type) == 0:
        trade(seed_type)    # Better way to do this but don't care as this is for simplicity
    plant(plant_type)

to_plant = [Entities.Carrot, None]
while num_items(Items.Carrot) < 1000: # Get a decent number of carrots
    move_around_board(get_world_size(), re_plant, to_plant)