# Define a static variable and access that through class name.

class Shape:
    cat='Geometrical'

    def __init__(self,type):
        self.type=type

    def show(self):
        print('Shape is of category: ',Shape.cat)
        print('And shape is: ',self.type)

tr=Shape('Triangle')
sq=Shape('Square')
cir=Shape('Circle')

tr.show()
sq.show()
cir.show()
    
    
