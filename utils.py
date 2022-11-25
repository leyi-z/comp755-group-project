type_to_int_dict = {
    "normal":0,
    "fighting":1,
    "flying":2,
    "poison":3,
    "ground":4,
    "rock":5,
    "bug":6,
    "ghost":7,
    "steel":8,
    "fire":9,
    "water":10,
    "grass":11,
    "electric":12,
    "psychic":13,
    "ice":14,
    "dragon":15,
    "dark":16,
    "fairy":17,
}

type_to_int_dict_inv = {v:k for k,v in type_to_int_dict.items()}


def type_to_int(types):
    
    #type_to_int is a function takes a string parameter specifying either the type of the Pokemon or type of
    #move. This function converts the string to an integer for easier computation of type effectiveness
    #if the Pokemon does not have a 2nd type, the else statement returns -1
    
    if(type(types)==float):
        return -1
    elif types.lower() in type_to_int_dict.keys():
        return type_to_int_dict[types.lower()]
    else:
        return -1