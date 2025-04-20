wosize = get_world_size()
print("Looking for apples")

next_x = wosize // 2
next_y = wosize // 2
noapplecount = 1

def checkapple(applecount=1):
    global noapplecount
    global next_x 
    global next_y
    global wosize
    if noapplecount >= wosize * wosize * 2:
        change_hat(Hats.Straw_Hat)
        if get_ground_type() == Grounds.Grassland:
            till()
        change_hat(Hats.Dinosaur_Hat)
        noapplecount = 1
    if get_entity_type() == Entities.Apple:
        next_x, next_y = measure()
        quick_print("Apple at (",next_x,",",next_y,")?")
        #quick_print(next_x, next_y)
        if (next_x == wosize - 2 and next_y == 1):
            print("Next apple bad")
            return True, next_x, next_y, True
        noapplecount = 1 # Reset apple count
        return True, next_x, next_y, False
    else:
        if can_harvest():
            harvest()
        noapplecount = applecount + 1 #increment apple count
        return False, next_x, next_y, (next_x == wosize - 2 and next_y == 1)

change_hat(Hats.Dinosaur_Hat)
checkapple(noapplecount)

def setupright():
    global noapplecount
    noapplecount = 1
    change_hat(Hats.Straw_Hat)
    if wosize % 2:
        while get_pos_x() != wosize - 1:
            move(East)
            if checkapple(noapplecount)[0]:
                do_a_flip()
        while get_pos_y() != wosize - 1:
            move(North)
            if checkapple(noapplecount)[0]:
                do_a_flip()
        while get_pos_y() != 0:
            harvest()
            if get_ground_type() == Grounds.Grassland:
                till()
            plant(Entities.Pumpkin)
            move(South)
            if checkapple(noapplecount)[0]:
                do_a_flip()
    else:
        plant(Entities.Pumpkin)
    change_hat(Hats.Dinosaur_Hat)
    checkapple(noapplecount)

def wiggledown():
    while get_pos_y() > 2:
        move(East)
        checkapple(noapplecount)
        move(South)
        checkapple(noapplecount)
        move(West)
        checkapple(noapplecount)
        move(South)
        checkapple(noapplecount)
        move(East)

def dowriggle():
    global noapplecount
    global next_x
    global next_y
    if wosize%2:
        needawigglepos = wosize - 2
    else:
        needawigglepos = wosize - 1
    while get_pos_x() > 0:
        move(West)
        checkapple(noapplecount)
    while get_pos_y() < wosize - 1:
        move(North)
        checkapple(noapplecount)
    #do_a_flip()
    while get_pos_x() < needawigglepos:
        for _ in range(get_pos_y(), wosize - 1):
            move(North)
            checkapple(noapplecount)
        move(East)
        checkapple(noapplecount)
        for _ in range(get_pos_y(), 1, -1):
            
            if get_pos_x() == needawigglepos and get_pos_y() == wosize - 1:
                wiggledown()
            move(South)
            foundapple, next_x, next_y, badapple = checkapple(noapplecount)
            if (badapple):
                
                if (get_pos_y() == 1 and get_pos_x() == wosize - 1):
                   print("Getting rougue apple")
                   move(West)
                   foundapple, next_x, next_y, badapple = checkapple(noapplecount)
                   if (foundapple and not badapple):
                       move(South)
                       foundapple, next_x, next_y, badapple = checkapple(noapplecount)
        if (not badapple):
            move(East)
        foundapple, next_x, next_y, badapple = checkapple(noapplecount)
    move(South)
    checkapple(noapplecount)
    for _ in range(get_pos_x(), 0, -1):
        move(West)
        checkapple(noapplecount)
    if noapplecount >= wosize * wosize * 2:
        setupright()
    else:
        dowriggle()  # Ensure this recursion has a proper termination condition.

def trydoubleback():
    move(North)
    move(East)
    move(East)
    move(South)

def dofindnext(x, y):
    print("Apple at (",x,",",y,")?")
    while get_pos_x() != x:
        if not move(West):
            break
    while get_pos_y() != y:
        if not move(South):
            break
    print("Not looking anymore")

# Main execution
setupright()
dowriggle()
trydoubleback()
dofindnext(next_x, next_y)
dowriggle()

while get_pos_x() < wosize:
    if not move(East):
        print("Hit the edge", get_pos_x(), get_pos_y())
        trydoubleback()
        dofindnext(3, 3)
        dowriggle()

move(North)
move(East)
move(East)
move(South)
