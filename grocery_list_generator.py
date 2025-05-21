from collections import defaultdict

def generate_grocery_list(meals_df):
    grocery_list = defaultdict(float)

    for ingredients in meals_df['ingredients']:
        items = ingredients.split(',')
        for item in items:
            parts = item.strip().rsplit(' ', 1)
            if len(parts) == 2:
                name, qty = parts
                try:
                    grocery_list[name] += float(qty)
                except:
                    grocery_list[name] += 1
            else:
                grocery_list[parts[0]] += 1

    return grocery_list
