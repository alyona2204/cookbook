from pprint import pprint
with open('1.txt') as f:
    cookbook = dict()
    class Dict_cookbook:
        def __init__(self):
           self.name = f.readline().strip()
           self.ingr_count = int(f.readline().strip())
           self.ingr_list = dict()
           self.new = {}
           self.value = []

        def add_dict(self):
            for x in range(self.ingr_count):
                ingr_list = (f.readline().split('|'))
                ingr_list = [line.rstrip() for line in ingr_list]
                self.new = {'ingredient_name':(ingr_list[0]),'quantity': (ingr_list[1]),'measure': (ingr_list[2])}
                self.value.append(self.new)
            cookbook[self.name] = self.value
            return cookbook

    def dish_cookbook(*x):
        for arg in x:
            x = Dict_cookbook()
            x.name
            x.ingr_count
            x.add_dict()
            cookbook[x.name] = x.value
            x = f.readline().strip()
            return arg
    dish_cookbook('dish1')
    dish_cookbook('dish2')
    dish_cookbook('dish3')
    dish_cookbook('dish4')
    #pprint(cookbook)
    dishes = []




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
                    result[keys]['quantity'] += element['quantity']
                else:
                    result.update({keys: values})
        return result


    pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 1))
