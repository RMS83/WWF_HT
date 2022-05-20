import os
from pprint import pprint

PATH_DIR = 'cookbook'

def get_file_name(dir_=PATH_DIR):
    pre_full_path = os.path.join(os.getcwd(), dir_)
    file_name = os.listdir(path=pre_full_path)
    return file_name

def get_dict(file):
    dish_dict = {}
    for line in file:
        dish_ = line.strip()
        quantity = int(file.readline())
        rez = []
        for ing_ in range(quantity):
            lines = {}
            data = file.readline().strip().split('|')
            lines['ingredient_name'] = data[0]
            lines['quantity'] = data[1]
            lines['measure'] = data[2]
            rez.append(lines)
        file.readline()
        dish_dict[dish_] = rez
    return dish_dict

def get_shop_list_by_dishes(dishes, person_count, product_card):
    ingredient_dict = {}
    for dish in dishes:
        if dish in product_card:
            for ingredient in product_card[dish]:
                ingred_quantity = {}
                if ingredient['ingredient_name'] not in ingredient_dict.keys():
                    ingred_quantity['measure'] = ingredient['measure']
                    ingred_quantity['quantity'] = int(ingredient['quantity']) * person_count
                    ingredient_dict[ingredient['ingredient_name']] = ingred_quantity
                else:
                    ingred_quantity = ingredient_dict[ingredient['ingredient_name']]
                    ingred_quantity['quantity'] += int(ingredient['quantity']) * person_count
    return ingredient_dict

def get_cook_book(name_func=get_file_name()):
    cook_book = {}
    for name in name_func:
        with open(os.path.join(os.getcwd(), PATH_DIR, name), 'r', encoding='utf-8') as file_:
            pre_cook_book = get_dict(file_)
            for key, value in pre_cook_book.items():
                cook_book[key] = value
    return cook_book


print('cook_book', "=", get_cook_book())
pprint(get_shop_list_by_dishes(['Яичница', 'Омлет', 'Омлет'], 2, get_cook_book()))
