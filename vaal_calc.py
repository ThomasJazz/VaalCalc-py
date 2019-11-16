import os
import pprint
from library import method_helper

helper = method_helper.MethodHelper()

dirpath = os.getcwd()
output_file = dirpath + '/out/vaal_probabilities.csv'
implicit_list_path = dirpath + '/ref/implicit_list.txt'
pp = pprint.PrettyPrinter(indent=1)

items = {'amulet': {}, 'body_armour': {}, 'belt': {}, 'boots': {}, 'bow': {}, 'claw': {},
'dagger': {}, 'fishing_rod': {}, 'gloves': {}, 'helmet': {}, 'axe': {}, 'mace': {},'sword': {},
'quiver': {}, 'ring': {}, 'rapier': {}, 'sceptre': {}, 'shield': {}, 'staff': {},'two_hand_weapon': {},
'one_hand_weapon': {}, 'wand': {}, 'default': {}}

# Read each line of implicit_list.txt
with open(implicit_list_path, 'r') as file: 
    for line in file:
        temp_lst = line.split('\t')
        for index in range(0, len(temp_lst)):
            temp_lst[index] = temp_lst[index].replace('\n', '')

        mods_index = len(temp_lst)-1

        # Need this because of 2 mod implicits
        while (temp_lst[mods_index]):
            try:
                val1, val2 = temp_lst[mods_index].split(' ')
                assert(val1 in items)
                mods_index -= 1
            except Exception as e:
                mods_index += 1
                break

        mod_desc = temp_lst[:3]
        temp_index = 3
        while temp_index < mods_index:
            mod_desc[2] = mod_desc[2] + '\n' + temp_lst[temp_index]
            temp_index += 1

        item_weights = temp_lst[mods_index:]


        effid, ilvl_str, effect = mod_desc
        ilvl = int(ilvl_str)
        for i in item_weights:
            item, weight_str = i.split(' ')
            weight = int(weight_str)

            if (weight > 0):
                items[item][effid] = {'ilvl': ilvl, 'effect': effect, 'weight': weight}
            

# Calculate the mod weight pools for each item level
ilvl_weight_pools = {}
for item in items:
    for mod in items[item]:
        attributes = items[item][mod]
        ilvl = attributes['ilvl']
        weight = attributes['weight']
        
        if not(item in ilvl_weight_pools):
            ilvl_weight_pools[item] = {ilvl: 0}
        
        if not(ilvl in ilvl_weight_pools[item]):
            ilvl_weight_pools[item][ilvl] = 0

for item in items:
    if item == 'default':
        continue

    for ilvl in ilvl_weight_pools[item]:
        for mod in items[item]:
            if items[item][mod]['ilvl'] <= ilvl:
                ilvl_weight_pools[item][ilvl] += items[item][mod]['weight']

# To be written to .csv
output = []
output.append(['item_base', 'mod', 'mod_ilvl', 'ilvl', 'chance_at_ilvl'])

# Calculate chances at all ilvl's for every implicit
for item in items:
    if item == 'default':
        continue
    
    print(f'\tItem: {item}')
    for mod in items[item]:
            mod_eff = items[item][mod]['effect']
            mod_ilvl = items[item][mod]['ilvl']
            mod_weight = items[item][mod]['weight']

            for ilvl in ilvl_weight_pools[item]:
                if ilvl >= mod_ilvl:
                    poolsize = ilvl_weight_pools[item][ilvl]
                    chance = float(float(mod_weight) / float(poolsize))

                    print(f'\tMod: {mod_eff}\n\t\tilvl: {ilvl}')
                    print('\t\tChance: {:.2%}'.format(chance))
                    output.append([item, mod_eff, mod_ilvl, ilvl, chance])
            

helper.export_list_to_csv(output_file, output)
print(f'Data output to: {output_file}')