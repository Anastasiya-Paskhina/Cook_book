cook_book = {}

with open ('menu.txt', encoding = 'utf8') as f:
    for line in f:
        name_of_dish = line.strip()
        amount_of_ingredient = f.readline().strip()
        list_ingredients = []
        ingredient = {}
        for i in range(int(amount_of_ingredient)):
            parametr_ingredient = f.readline().strip().split(' | ')
            ingredient['ingredient_name'] = parametr_ingredient[0]
            ingredient['quantity'] = parametr_ingredient[1]
            ingredient['measure'] = parametr_ingredient[2]
            list_ingredients.append(ingredient.copy())
            cook_book[name_of_dish] = list_ingredients
        f.readline()

#print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    zakaz = {}
    for name_of_dish in dishes:
        for parametr_ingredient in cook_book[name_of_dish]:
            ingredient = parametr_ingredient
            if  ingredient['ingredient_name'] not in zakaz:
                zakaz[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity':int(ingredient['quantity']) * person_count}
            else:
                zakaz[ingredient['ingredient_name']]['quantity'] += int(ingredient['quantity']) * person_count
    print(zakaz)

get_shop_list_by_dishes(['Фахитос', 'Омлет'], 5)

