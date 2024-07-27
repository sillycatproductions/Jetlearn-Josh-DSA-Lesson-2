class Monkey:
    __monkeyshomeadress = '123 ooh ooh aah aah avenue'
    def __init__(self, name, color, strength, flexibility):
        self.name = name
        self.color = color
        self.strength = strength
        self.flexibility = flexibility
    def getmonkey(self):
        print(self.__monkeyshomeadress)
    def showhim(self):
        print('OOH AAH AAH [my name is {}]! AAH AAH EEEEEAAAAHHH OOOH AAHA [i am {}]! RAAAAH AAAH OOOH OOOH EEEEH [i am {} strong]! EEEEEH AAAH KEYYYYY [i am {} flexible]!'.format(self.name, self.color, self.strength, self.flexibility))
    
oohaah = Monkey('ooh eeah aah','brown','very','super duper')
oohaah.showhim()
oohaah.getmonkey()