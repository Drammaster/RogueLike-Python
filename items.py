def item_name(x):

    if x == 1:
        return("Hand Gun (-2)")
    elif x == 2:
        return("Bandage (+6)")
    elif x == 3:
        return("Bat (-5)")

def item_effect(y):

    if y == 1:
        return("ranged", 2)
    elif y == 2:
        return("heal", 6)
    elif y == 3:
        return("melee", 5)