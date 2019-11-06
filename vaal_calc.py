import os

dirpath = os.getcwd()
implicit_list_path = dirpath + '/ref/implicit_list.txt'

items = {'amulet': {}, 'body_armour': {}, 'belt': {}, 'boots': {}, 'bow': {}, 'claw': {},
'dagger': {}, 'gloves': {}, 'helmet': {}, 'one_hand_axe': {}, 'one_hand_mace': {},'one_hand_sword': {},
'quiver': {}, 'ring': {}, 'sceptre': {}, 'shield': {}, 'staff': {},'two_hand_axe': {},
'two_hand_mace': {}, 'two_hand_sword': {}, 'wand': {}, 'default': {}}

# Read each line of implicit_list.txt
with open(implicit_list_path, 'r') as file: 
    for line in file:
        temp_lst = line.split('\t')
        mod_desc = temp_lst[:3]
        item_weights = temp_lst[3:]

        name, ilvl, effect = mod_desc
        for i in item_weights:
            item, weight_str = i.split(' ')
            weight = int(weight_str)

            if (weight > 0):
                items[item][effect] = {'ilvl': ilvl, 'name': name, 'effect': effect, 'weight': weight}
                print('Added: "{0}" to base: "{1}"'.format(effect, item))
                if 'total' in items[item]:
                    items[item]['total'] += weight
                else:
                    items[item]['total'] = weight

            

print("Check out my fat dict bro")
