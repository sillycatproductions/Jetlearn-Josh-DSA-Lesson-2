class Cats:
    def __init__(self, name, color, size, mood):
        
        self.name = name
        self.color = color
        self.size = size
        self.mood = mood

    def printingcat(self):
        print('My name is {} and I am a cat. I am {}. I am about {}cm and right now I feel {}.' .format(self.name, self.color, self.size, self.mood))

class Dobby(Cats):
    def __init__(self, name, color, size, mood, favfood):
        Cats.__init__(self, name, color, size, mood)
        self.favfood = favfood

    def printingcat(self):
        print('My name is {} and I am a cat. I am {}. I am about {}cm and right now I feel {}. My favourite food is {}!' .format(self.name, self.color, self.size, self.mood, self.favfood))


dobby = Dobby('Dobby','orange','40','happy','drink')
dobby.printingcat()
    