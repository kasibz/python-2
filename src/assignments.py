# define your methods here.
# ex1() - ex10()
import random

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
            
def ex6():
    class TaxMan:
        def __init__(self, items_list, tax) -> None:
            self.items_list = items_list
            self.tax = int(tax[0:len(tax)-1]) / 100
            self.total = 0
        
        def calc_total(self):
           total = sum(list(map(lambda i: i['price'], self.items_list)))
           sales_amt = total * self.tax
           self.total = sales_amt + total
           '''
           total is sum of all prices
           then apply the sales tax
           '''
        
        def get_total(self):
            return self.total

    items = [
        {"id": 1, "desc": "clock", "price": 1.00},
        {"id": 2, "desc": "socks", "price": 2.00},
        {"id": 3, "desc": "razor", "price": 3.00},
    ]

    tm = TaxMan(items, "10%")
    tm.calc_total()
    print(tm.get_total())


def ex7():
    class Calculator:
        def __init__(self, num_1, num_2) -> None:
            self.num_1 = num_1
            self.num_2 = num_2
            self.result = 0

        def add(self):
            self.result = self.num_1 + self.num_2
        
        def sub(self):
            self.result = self.num_1 - self.num_2

        def mul(self):
            self.result = self.num_1 * self.num_2

        def div(self):
            self.result = self.num_1 / self.num_2

        def get_result(self):
            return self.result
        
    calculator1 = Calculator(4, 3)
    calculator1.add()
    print(calculator1.get_result())

    calculator2 = Calculator(4, 3)
    calculator2.sub()
    print(calculator2.get_result())

    calculator3 = Calculator(2, 3)
    calculator3.mul()
    print(calculator3.get_result())

    calculator4 = Calculator(8, 2)
    calculator4.div()
    print(calculator4.get_result())

def ex8():
    class CarCollector:
        car_list = [
            {"id": 1, "price": 10000},
            {"id": 2, "price": 20000},
            {"id": 3, "price": 30000},
        ]
        car_dict = {
            1: "Ford",
            2: "Mazda",
            3: "Chevy"
        }

        @staticmethod
        def get_data():
            return list(map(CarCollector._combine, CarCollector.car_list))
        
        @staticmethod
        def _combine(c):
            retval = {
                **c,
                'make': CarCollector.car_dict[c['id']]
            }
            return retval
    print(CarCollector.get_data())

def ex9():

    class Character:

        def __init__(self, hit_points):
            self.hit_points = hit_points

        def fight(self, character):
            random_number = random.randint(1, 20)
            character.hit_points -= random_number
            if character.hit_points < 0:
                character.hit_points = 0
    
    class Fighter(Character):
        def __init__(self, hit_points):
            super().__init__(hit_points)
            self.name = "Fighter"
        
        def __repr__(self) -> str:
            return f"{self.name}: {self.hit_points} hit points."
    
    
    class Dwarf(Character):
        def __init__(self, hit_points):
            super().__init__(hit_points)
            self.name = "Dwarf"

        def __repr__(self) -> str:
            return f"{self.name}: {self.hit_points} hit points."
    f = Fighter(18)
    d = Dwarf(15)
    print(f)
    print(d)
    f.fight(d)
    d.fight(f)
    print(f)
    print(d)

def ex10():
    class Invoice:

        def __init__(self, data_string) -> None:
            self.invoice_id = data_string.split(",")[0]
            self.user_id = data_string.split(",")[1]
            self.amount = data_string.split(",")[2]
            self.paid = data_string.split(",")[3]

        def __repr__(self) -> str:
            return f"Invoice(invoice_id={self.invoice_id}, user_id={self.user_id}, amount={self.amount}, paid={self.paid})"
    
    data = [
        "1, 2322, 10.00, False",
        "2, 5435, 60.30, True",
        "3, 3433, 15.63, False",
        "4, 8439, 12.77, False",
        "5, 3424, 11.34, False",
    ]
    invoice_list = []
    for item in data:
        invoice_list.append(Invoice(item))
    
    print(invoice_list)