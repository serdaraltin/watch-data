from interfaces import IStatistic
from .model_person import (
    Person,
    EnterExit,
    Gender,
    Age,
)




class Statistic(IStatistic):
    def __init__(self, *args, **kwargs):
        self.persons = []

    def push(self, person: Person):
        self.persons.append(person)

    def pop(self) -> Person:
        return self.persons.pop() if self.persons else None

    @property
    def enter(self):
        return sum(1 for p in self.persons if p.enter_exit.event_type == 'enter')

    @property
    def exit(self):
        return sum(1 for p in self.persons if p.enter_exit.event_type == 'exit')

    @property
    def female(self):
        return sum(1 for p in self.persons if p.gender.gender == 'female')

    @property
    def male(self):
        return sum(1 for p in self.persons if p.gender.gender == 'male')

    @property
    def total(self):
        return len(self.persons)

    @property
    def current(self):
        return self.enter - self.exit
    
    @property
    def current_female(self):
        return sum(1 for p in self.persons if p.gender.gender == 'female' and p.enter_exit.event_type == 'enter') - sum(1 for p in self.persons if p.gender.gender == 'female' and p.enter_exit.event_type == 'exit')
    
    @property
    def current_male(self):
        return sum(1 for p in self.persons if p.gender.gender == 'male' and p.enter_exit.event_type == 'enter') - sum(1 for p in self.persons if p.gender.gender == 'male' and p.enter_exit.event_type == 'exit')


    @property
    def age_distribution(self):
        age_groups = {
            "0-18": 0,
            "19-30": 0,
            "31-45": 0,
            "46-60": 0,
            "61+": 0
        }
        for person in self.persons:
            age_range = person.age.age_range
            if age_range in age_groups:
                age_groups[age_range] += 1
            else:
                pass # Loglama için
        return age_groups
    

