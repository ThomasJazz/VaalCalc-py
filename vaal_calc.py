import os
import pprint

dirpath = os.getcwd()
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

        stats_index = len(temp_lst)-1

        while (temp_lst[stats_index]):
            try:
                val1, val2 = temp_lst[stats_index].split(' ')
                assert(val1 in items)
                stats_index -= 1
                pass
            except Exception as e:
                stats_index += 1
                break

        mod_desc = temp_lst[:3]
        temp_index = 3
        while temp_index < stats_index:
            mod_desc[2] = mod_desc[2] + '\n' + temp_lst[temp_index]
            temp_index += 1

        item_weights = temp_lst[stats_index:]


        effid, ilvl_str, effect = mod_desc
        ilvl = int(ilvl_str)
        for i in item_weights:
            item, weight_str = i.split(' ')
            weight = int(weight_str)

            if (weight > 0):
                items[item][effid] = {'ilvl': ilvl, 'effect': effect, 'weight': weight}
                

print("Check out my fat dict bro")
#ilvl_weight_pools = []
ilvl = 55
stats_at_ilvl = []
for stat in items['amulet']:
    stat_info = items['amulet'][stat]
    if stat_info['ilvl'] <= ilvl:
        stats_at_ilvl.append(items['amulet'][stat])

pp.pprint(stats_at_ilvl)