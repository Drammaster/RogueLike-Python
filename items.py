def item_name(x):

    if x == 1:
        return("Hand Gun (-2)")
    elif x == 2:
        return("Bandage (+6)")

def item_effect(y):

    if y == 1:
        return("damage", 2)
    elif y == 2:
        return("heal", 6)