class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, heath_points, catchprase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = heath_points
        self.catchphrase = catchprase

    def name1(self, name):
        self.name = name
        print(self.name)

    def hp(self, health_points):
        self.health_points = health_points
        print((int(self.health_points) * 2))

    def __str__(self):
        return F'я {self.nickname}\n' \
               F'моя сила-{self.superpower}\n' \
               F'{self.catchphrase}'

    def __len__(self):
        return len(self.catchphrase)


sh = SuperHero('Гон', 'вера', 'превзайду',100 , "im genius" )


class Airhero(SuperHero):
    air = 'air'

    def __init__(self, name, nickname, superpower, heath_points, catchprase, damage, fly=False):
        super().__init__(name, nickname, superpower, heath_points, catchprase)
        self.damage = damage
        self.fly = fly

    def hp(self):
        self.fly = True
        return self.health_points ** 2

    def fly_sky(self):
        return f'fly in the {self.fly}_phrase'


class Earthhero(SuperHero):
    earth = 'earth'

    def __init__(self, name, nickname, superpower, heath_points, catchprase, damage, fly=False):
        super().__init__(name, nickname, superpower, heath_points, catchprase)
        self.damage = damage
        self.fly = fly

    def hp(self):
        self.fly = True
        return self.health_points ** 2

    def fly_sky(self):
        return f'fly in the {self.fly}_phrase'


thor = Airhero('thor', 'bog', 'grom', 200, 'хз', damage=300)
cap = Earthhero('cap', 'pon', 'hello', 150, 'ladno', damage=100)
print(f"{thor.hp()}\n,"
f'{thor.fly_sky()}\n',
f'{cap.hp()}\n',
f'{cap.fly_sky()}'
)

class Villian(Airhero):
    def __init__(self, name, nickname, superpower, heath_points, catchprase, damage, fly=False):
        super().__init__(name, nickname, superpower, heath_points, catchprase, damage, fly)
        SuperHero.people = 'monster'

    def gen_x(self): ...

    def crit(self, hero):
        return hero.damage ** 2


tanos = Villian('tanos', 'tanka', 'kamni', 900, 'pon', 50)
print(Villian.crit(tanos, thor))
print(Villian.crit(tanos, cap))
