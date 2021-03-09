from pprint import pprint
cookbook = dict()
def get_cookbook(file):
    with open(file) as f:
        for line in f:
            dish_name = line.strip()
            counter = int(f.readline())
            list_of_ingredient = []
            for i in range(counter):
                key = ['ingredient_name', 'quantity', 'measure']
                ingredient = f.readline().strip('\n').split(' | ')
                temp_dict = dict(zip(key, ingredient))
                list_of_ingredient.append(temp_dict)
            cookbook[dish_name] = list_of_ingredient
            f.readline()
        return cookbook

get_cookbook('recipes.txt')


def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for dish in dishes:
        for element in cookbook[dish]:
            quanty = int(element['quantity'])
            quanty = quanty * person_count
            element['quantity'] = quanty
            keys = element['ingredient_name']
            values = {'measure': element['measure'], 'quantity': element['quantity']}
            if element['ingredient_name'] in result:
                result[keys]['quantity'] += quanty
            else:
                result.update({keys: values})
    return result


pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 1))
