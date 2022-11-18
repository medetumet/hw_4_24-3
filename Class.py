class Hero:
    def __init__(self, name, abyliti):
        self.name=name
        self.abyliti=abyliti


class Hero_super(Hero):
    def __init__(self, name, abyliti):
        super().__init__(name, abyliti)

    def __str__(self):
        return self.name
    def info(self):
        print(f'{self.name} it is super hero')



