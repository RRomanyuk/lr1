class Build:
    __type_build = None
    __year_build = None
    __city = None

    def __init__(self, type_build, year_build, city):
        self.type_build = type_build
        self.year_build = year_build
        self.city = city

    def get_info(self):
        print(f"Build: {self.type_build}, Year: {self.year_build}, City: {self.city}")
class School(Build):
    __floor = None
    __pupils = None

    def __init__(self, type_build, year, city, floor, pupils):
        super().__init__(type_build, year, city)
        self.floor = floor
        self.pupils = pupils
        self.get_info()

    def get_info(self):
        super().get_info()
        print("Floor:", self.floor, "Pupils:", self.pupils)

class House(Build):
    __people = None
    __rooms = None

    def __init__(self, type_build, year, city, people, rooms):
        super().__init__(type_build, year, city)
        self.__people = people
        self.__rooms = None

    def get_info(self):
        super().get_info()
        print("People:", self.__people, "Rooms:", self.__rooms)

school = School("School", 2000, "Cherkasy", 9, 200)
house = House("House", 2010, "Shpola", 5, 3)


#Декоратор
def validator(func):
    def wrapper(url):
        print("Before")
        func(url)
        print("After")
    return wrapper

@validator
def func():
    a = 5
    b = 5
    print(a + b)