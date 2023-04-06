

class SuperHero:
    people = 'people'
    name = 'name'
    nickname = 'nickname'
    superpower = 'superpower'
    health_points = 'health_points'
    catchphrase = 'catchphrase'


    def name1(self, name):
        self.name = name
        print(self.name)


    def hp(self, health_points):
        self.health_points = health_points
        print((int(self.health_points) * 2))


    def __init__(self, nickname, superpower, catchphrase):
        self.nickname = nickname
        self.superpower = superpower
        self.catchphrase = catchphrase

    def __str__(self):
        return F'я {self.nickname}\n'\
               F'моя сила-{self.superpower}\n'\
               F'{self.catchphrase}'
    def __len__(self):
        return len(self.catchphrase)


sh = SuperHero('Гон', 'вера', 'превзайду')

sh.name1('килуа')
sh.hp('100')

print(sh)
print(len(sh))
