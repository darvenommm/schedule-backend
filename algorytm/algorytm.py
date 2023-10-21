from bigtree import Node, print_tree, find, findall, find_attr, tree_to_dict, utils
import datetime
import random

audiencies = [
    {
        'name' : 1,
        'size': 20,
        'type': 'laboratory'
    },
    {
        'name' : 2,
        'size': 100,
        'type': 'lecture'
    },
    {
        'name' : 3,
        'size': 25,
        'type': 'practice'
    },
    {
        'name' : 4,
        'size': 50,
        'type': 'lecture'
    },
    {
        'name' : 5,
        'size': 30,
        'type': 'laboratory'
    },
    {
        'name' : 6,
        'size': 50,
        'type': 'lecture'
    },
    {
        'name' : 7,
        'size': 20,
        'type': 'practice'
    },
    {
        'name' : 8,
        'size': 20,
        'type': 'laboratory'
    },
    {
        'name' : 9,
        'size': 30,
        'type': 'practice'
    }, 
]

teachers = [
    {
        'name': 'Ivan',
        'prefered': [
            (datetime.datetime(2023, 9, 1), 1),
            (datetime.datetime(2023, 9, 17), 2),
            (datetime.datetime(2023, 9, 5), 2),
            (datetime.datetime(2023, 9, 3), 4),
            (datetime.datetime(2023, 9, 7), 4),
        ],
        'subject': 'math',
    },
    {
        'name': 'Alex',
        'prefered': [
            (datetime.datetime(2023, 9, 6), 1),
            (datetime.datetime(2023, 9, 15), 2),
            (datetime.datetime(2023, 9, 4), 2),
            (datetime.datetime(2023, 9, 12), 4),
            (datetime.datetime(2023, 9, 16), 5),
        ],
        'subject': 'programming',
    },
    {
        'name': 'Igor',
        'prefered': [
            (datetime.datetime(2023, 9, 13), 1),
            (datetime.datetime(2023, 9, 18), 2),
            (datetime.datetime(2023, 9, 1), 2),
            (datetime.datetime(2023, 9, 17), 4),
            (datetime.datetime(2023, 9, 19), 5),
        ],
        'subject': 'english',
    },
]

groups = [
    {
        'title': '1st',
        'size': 20,
        'subjects': {
            'math': {
                'practice': 30,
                'lecture': 30,
                'laboratory': 2
            },
            'programming':{
                'practice': 40,
                'lecture': 20,
                'laboratory': 2
            },
            'english':{
                'practice': 50,
                'lecture': 10,
                'laboratory': 2
            },
        },
    },
    {
        'title': '2st',
        'size': 30,
        'subjects': {
            'math':{
                'practice': 15,
                'lecture': 45,
                'laboratory': 2
            },
            'programming':{
                'practice': 40,
                'lecture': 20,
                'laboratory': 2
            },
            'english':{
                'practice': 50,
                'lecture': 10,
                'laboratory': 2
            },
        },
    },
]

root = Node('root')
start_date = datetime.datetime(2023, 9, 1)
end_date = datetime.datetime(2023, 12, 30)

semestr = (end_date - start_date).days

start_semestr_date = datetime.datetime(2023, 9, 1)

for date_index in range(semestr):
    date_node = Node(f'day{date_index + 1}', timeline=start_semestr_date.timestamp(), parent=root)
    start_semestr_date = (start_semestr_date + datetime.timedelta(days=1))

    for slot_index in range(1, 7):
        slot_node = Node(f'slot{slot_index}', slot_index=slot_index, parent=date_node)

        for audience in audiencies:
            audience_node = Node(f'audience{audience["name"]}', audience_data = audience, parent=slot_node)

conflicts = []

for teacher in teachers:
    for date, slot in teacher['prefered']:
        need_date_node = find_attr(root, 'timeline', date.timestamp())
        need_slot_node = find_attr(need_date_node, 'slot_index', slot)
        
        need_audiencies = list(findall(need_slot_node, lambda node: node.node_name.startswith('audience')))

        flag = False
        for audience in need_audiencies:
            if not audience.is_leaf:
                continue

            for group in groups:
                if group['size'] <= audience.get_attr('audience_data')['size']:
                    Node(f'{date.timestamp()} {slot} {teacher["name"]} {group["title"]}', value={
                        'date': date.timestamp(),
                        'slot': slot,
                        'teacher': teacher['name'],
                        'group': group['title'],
                    }, parent=audience)
                    group['subjects'][teacher['subject']][audience.get_attr('audience_data')['type']] -= 1
                    flag = True
                    break
            
            if flag:
                break

        if not flag:
            conflicts.append((teacher['name'], date, slot))

find_na = findall(root, lambda node: node.node_name.startswith('audience') and node.is_leaf)
counter = 0
cache = []
for clear_audience in find_na:
    random_group = random.choice(groups)
    random_subject = random.choice(list(random_group['subjects'].keys()))
    teacher = random.choice([teacher for teacher in teachers if teacher['subject'] == random_subject])
    slot = clear_audience.parent.get_attr('slot_index')
    day = clear_audience.parent.parent.get_attr('timeline')

    if (day, slot, teacher['name'], random_group['title']) in cache:
        continue
    else:
        cache.append((day, slot, teacher['name'], random_group['title']))

    if random_group['subjects'][random_subject][clear_audience.get_attr('audience_data')['type']] > 0:
        try:
            a = Node(f'{day} {slot} {teacher["name"]} {random_group["title"]}', value={
                'day': day,
                'slot': slot,
                'teacher': teacher['name'],
                'group': random_group['title'],
            }, parent=audience)
            random_group['subjects'][random_subject][clear_audience.get_attr('audience_data')['type']] -= 1
        except utils.exceptions.TreeError:
            pass

print_tree(root, all_attrs=True)