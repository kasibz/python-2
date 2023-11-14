# define your methods here.
# ex1() - ex10()
people_list = [
    {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
    {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
    {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
]


def ex1():
    people_list = [
        {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
        {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]

    def sort_people(p_lst, category, dir):
        if dir == 'asc':
            p_lst.sort(key=lambda p: p[category])
        elif dir == 'desc':
            p_lst.sort(key=lambda p: p[category], reverse=True)
    
    sort_people(people_list, 'weight', 'asc')
    print(people_list)

def ex2():

    pass
