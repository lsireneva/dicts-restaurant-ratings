"""Restaurant rating lister."""

def read_ratings(filename):
    """Return a list of words"""
    file = open(filename)

    res_dict = {}

    for line in file:
        line = line.rstrip().split(':')
        res_dict[line[0]] = line[1]
    
    print_dict(res_dict)    
    new_res_name = input('Would you like to add new restaurant? ')
    new_rating = input('Please add rating: ')

    res_dict[new_res_name] = new_rating

     
    return res_dict

def print_dict(dict):

    for res_name, rating in sorted (dict.items()):

        print(f'{res_name} is rated at {rating}.')

dict=read_ratings("scores.txt")
print_dict(dict)