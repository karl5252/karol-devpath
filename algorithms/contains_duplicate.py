# accepts list
# outputs bollean
# aim is to check if input has duplicates
def contains_duplicate(black_knight:list)->bool:
    arthur = set(black_knight)
    return len(arthur)!=len(black_knight)

#contains_duplicate([1, 2, 3, 4])
#False
#contains_duplicate([42])
#False
#contains_duplicate([1, 2, 3, 4, 1])
#True
       
def contains_duplicate_set(black_knight:list)->bool:
    limbs = set()
    for limb in black_knight:
        if limb in limbs:
            return True
        limbs.add(limb)
    return False

#contains_duplicate_set([1, 2, 3, 4, 1])
#True
#contains_duplicate_set([42])
#False
#contains_duplicate_set([1, 2, 3, 4])
#False
