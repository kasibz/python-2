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
    people_list = [
        {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
        {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]

    def filter_males(people_list):
        return list(filter(lambda p: p['sex'] == 'male', people_list))
    
    filtered_list = filter_males(people_list)
    print(filtered_list)
    

def ex3():
    people_list = [
        {'id': 2, 'name': 'bob',     'weight_kg': 90, 'height_meters': 1.7},
        {'id': 3, 'name': 'charlie', 'weight_kg': 80, 'height_meters': 1.8},
    ]
    def transform_person(p):
        retval = {
            **p,
            'bmi': round(p['weight_kg'] / p['height_meters'] ** 2, 1)
        }
        return retval

    def calc_bmi(people_list):

        return list(map(transform_person, people_list))

        
    new_people_list = calc_bmi(people_list)
    print(new_people_list)



def ex4():
    people_list = [
        {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
        {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]

    def get_people(people_list):
        # accept list of people, list comprehension with 
        return [p['name'] for p in people_list if p['age'] >= 15]
    
    print(get_people(people_list))

def ex5():
    class WordCounter:
        def __init__(self, sentence) -> None:
            self.sentence = sentence
            self.word_count = None


        def count_words(self):
            self.word_count = len(self.sentence.split(" "))

        def get_word_count(self):
            return self.word_count
        
        def get_shortest_word(self):
            return len(min((self.sentence.split(" ")), key=len))

        def get_longest_word(self):
            return len(max(self.sentence.split(" "), key=len))
    
    sentence = "This is a test of the emergency broadcast system"
    word_counter = WordCounter(sentence)
    word_counter.count_words()
    print(word_counter.get_word_count())    # Returns the number of all the words.
    print(word_counter.get_shortest_word()) # Returns the length of the shortest word.
    print(word_counter.get_longest_word()) 
            
