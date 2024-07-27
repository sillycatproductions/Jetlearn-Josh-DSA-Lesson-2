class Cars:
    def __init__(self,name,color,shape,speed,hp,fuel,features,size,capacity):
        
        self.name = name
        self.color = color
        self.shape = shape
        self.speed = speed
        self.hp = hp
        self.fuel = fuel
        self.features = features
        self.size = size
        self.capacity = capacity

    def set_shape(self,new_shape):
        self.shape = new_shape

    def showcar(self):
        print('I am {} and my color is {}. I am shaped like a {} and i go {}mph. I have {} horsepower and I can store {} fuel. I can {} and I am {}cm big. I can hold {} people'.format(self.name,  self.color, self.shape,  self.speed, 
        self.hp, 
        self.fuel,
        self.features ,
        self.size,
        self.capacity,
 ))

class Mercedes_Benz(Cars):
    def __init__(self,name,color,shape,speed,hp,fuel,features,size,capacity,weight,electricity):
        Cars.__init__(self,name,color,shape,speed,hp,fuel,features,size,capacity)
        self.weight = weight
        self.electricity = electricity
    def showcar(self):
        print('I am {} and my color is {}. I am shaped like a {} and i go {}mph. I have {} horsepower and I can store {} fuel. I can {} and I am {}cm big. I can hold {} people. I am {}kg heavy and I have {}J electricity'.format(self.name,  self.color, self.shape,  self.speed, 
        self.hp, 
        self.fuel,
        self.features ,
        self.size,
        self.capacity,
        self.weight,
        self.electricity
 ))

vroom = Mercedes_Benz('mercedes benz','blue','iphone9583','99999999','-19','no','drive','0.1','0','caseoh','4876478646784356784584584657343586453867')
vroom.set_shape('iphone9584')
vroom.showcar()