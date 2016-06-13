class Animal():
    name = 'Amy'
    noise = "Grunt"
    size = "Large"
    color = "Brown"
    hair = 'Covers body'
    def get_color(self):
        return self.color
    def make_noise(self):
        return self.noise


dog = Animal()
dog.make_noise()
dog.size = "small"
dog.color = "black"
dog.hair = "hairless"


class Dog(Animal):
    name = 'Jon'
    size = "small"
    color = "black"
    age = 19


jon = Dog()
jon.color = 'white'
jon.name = 'Jon Snow'

